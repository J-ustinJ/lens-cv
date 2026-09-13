import time
import streamlit as st
from groq import Groq
from utils.pdf_utils import extract_text_from_pdf
from utils.resume_structure import check_resume_structure
from analysis.category_match import calculate_category_scores
from analysis.weights import calculate_weighted_match_score
from analysis.ats import extract_jd_keywords, calculate_ats_score
from analysis.semantic import calculate_semantic_score
from analysis.skill_gap import get_skill_gap

from ai.recruiter import generate_recruiter_evaluation
from ai.feedback import generate_feedback
from ai.interview import generate_interview_questions
from ai.roadmap import generate_learning_roadmap
from ui.styles import inject_global_styles
from ui.layout import render_header, render_sidebar, render_inputs, render_hiring_context_and_button
from ui.charts import build_radar_chart, get_match_grade
from ui.score_cards import circular_score

# Page Config
st.set_page_config(
    page_title="LensCV",
    page_icon="🔍",
    layout="wide"
)
inject_global_styles()

# UI: Header, Sidebar, Inputs
render_header()
groq_api_key = render_sidebar()
resume_file, jd_text = render_inputs()
application_type, analyze_btn = render_hiring_context_and_button()

# Analysis
if analyze_btn:
    if not resume_file:
        st.error("Please upload your resume.")
    elif not jd_text.strip():
        st.error("Please paste a job description.")
    elif not groq_api_key.strip():
        st.error("Please enter your Groq API key in the sidebar.")
    else:
        loading = st.container()
        with loading:
            st.markdown("## 🧠 LensCV AI")
            st.info("Analyzing your resume... This might take a while.")
            progress = st.progress(0)
            status = st.empty()

            # Step 1
            status.write("📄 Extracting resume...")
            resume_text = extract_text_from_pdf(resume_file)
            progress.progress(15)
            if not resume_text.strip():
                st.error("Could not extract text. Make sure PDF is not a scanned image.")
                st.stop()

            # Step 2
            status.write("🧩 Matching categories...")
            category_scores = calculate_category_scores(resume_text, jd_text)
            final_score, active_weights = calculate_weighted_match_score(category_scores, application_type)
            progress.progress(35)

            # Step 3
            status.write("🎯 Calculating ATS score...")
            jd_keywords = extract_jd_keywords(jd_text)
            ats_score, matched, missing = calculate_ats_score(resume_text, jd_keywords)
            progress.progress(50)

            # Step 4
            status.write("🧠 Computing semantic similarity...")
            semantic_score = calculate_semantic_score(resume_text, jd_text)
            progress.progress(65)

            # Step 5
            status.write("🔍 Finding skill gaps...")
            skill_gaps = get_skill_gap(resume_text, missing)
            progress.progress(80)

            # Step 6
            status.write("📑 Checking resume structure...")
            structure_check = check_resume_structure(resume_text)
            combined_score = round(0.4 * ats_score + 0.6 * semantic_score, 1)
            progress.progress(100)
            status.success("✅ Analysis Complete!")

        time.sleep(0.5)
        loading.empty()
        st.divider()

        # Top-level scores
        st.subheader("📊 Overall Scores")
        grade, label = get_match_grade(final_score)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            circular_score(final_score, "🏆 Recruiter", grade)
        with col2:
            circular_score(ats_score, "🎯 ATS", "")
        with col3:
            circular_score(semantic_score, "🧠 Semantic", "")
        with col4:
            circular_score(combined_score, "⭐ Combined", "")

        st.divider()

        # ── Category Breakdown ──
        st.subheader("🧩 Category Breakdown")
        st.caption(f"Weights shown are redistributed across categories actually present in the JD, for a **{application_type}** context.")

        if category_scores:
            metric_cols = st.columns(len(category_scores))
            for i, (cat, data) in enumerate(category_scores.items()):
                with metric_cols[i]:
                    weight = active_weights.get(cat, 0)
                    st.metric(cat, f"{data['score']}%", help=f"Weight in final score: {weight}%")

            st.divider()
            radar_col, insight_col = st.columns([1, 1])

            with radar_col:
                st.plotly_chart(build_radar_chart(category_scores), use_container_width=True)

            with insight_col:
                st.markdown("**Active Weight Distribution**")
                for cat, weight in active_weights.items():
                    st.markdown(f"- **{cat}**: {weight}%")
                st.caption("Categories with no JD keywords are excluded and never penalized.")
        else:
            st.info("No recognizable category keywords found in the job description.")

        st.divider()

        # ── Detailed Match Insights ──
        st.subheader("🔎 Detailed Match Insights")
        for cat, data in category_scores.items():
            with st.expander(f"{cat} — {data['score']}% match"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("### ✅ Required Skills")
                    st.markdown("**Matched**")
                    if data["matched"]:
                        for kw in sorted(data["matched"]):
                            st.success(kw)
                    else:
                        st.write("None")
                    st.markdown("**Missing**")
                    if data["missing"]:
                        for kw in sorted(data["missing"]):
                            st.error(kw)
                    else:
                        st.success("None")
                with col2:
                    st.markdown("### ⭐ Preferred Skills")
                    st.markdown("**Matched**")
                    if data["preferred_matched"]:
                        for kw in sorted(data["preferred_matched"]):
                            st.success(kw)
                    else:
                        st.write("None")
                    st.markdown("**Missing**")
                    if data["preferred_missing"]:
                        for kw in sorted(data["preferred_missing"]):
                            st.warning(kw)
                    else:
                        st.success("None")
        st.divider()

        # ── AI-generated sections ──
        try:
            client = Groq(api_key=groq_api_key)

            with st.spinner("🤖 Generating recruiter evaluation..."):
                recruiter_eval = generate_recruiter_evaluation(
                    client, resume_text, jd_text, final_score, application_type
                )
            st.subheader("🕴️ Recruiter Simulation")
            st.markdown(recruiter_eval)

            st.divider()

            with st.spinner("🤖 Generating AI feedback..."):
                feedback = generate_feedback(client, resume_text, jd_text, missing)
            with st.expander("💬 AI Feedback", expanded=False):
                st.markdown(feedback)

            st.divider()

            with st.spinner("🤖 Generating interview questions..."):
                questions = generate_interview_questions(client, resume_text, jd_text)
            with st.expander("🎤 Likely Interview Questions", expanded=False):
                st.markdown(questions)

            st.divider()

            with st.spinner("🤖 Generating learning roadmap..."):
                roadmap = generate_learning_roadmap(client, missing, jd_text)
            with st.expander("🗺️ Learning Roadmap", expanded=False):
                st.markdown(roadmap)

        except Exception as e:
            st.error(f"Groq API error: {e}")
            st.info("Check that your API key is correct and you have remaining quota.")

        st.divider()

        # ── Resume Structure Check ──
        st.subheader("🏗️ Resume Structure Check")
        cols = st.columns(len(structure_check))
        for i, (section, found) in enumerate(structure_check.items()):
            with cols[i]:
                if found:
                    st.success(f"✅ {section}")
                else:
                    st.error(f"❌ {section}")

        st.divider()

        # ── Legacy skill gap (semantic ranked) ──
        with st.expander("🔍 Skill Gap Analysis"):
            st.caption("Legacy view: flat missing keywords ranked by semantic distance from your resume.")
            if skill_gaps:
                for skill, sim in skill_gaps:
                    sim_pct = round(float(sim) * 100, 1)
                    col_s, col_b2 = st.columns([2, 3])
                    with col_s:
                        st.markdown(f"`{skill}`")
                    with col_b2:
                        st.progress(int(sim_pct), text=f"{sim_pct}% relevance to your resume")
            else:
                st.success("No significant skill gaps found!")
