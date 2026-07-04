import streamlit as st


def render_header(logo_path: str = r"C:\Users\Justin\Downloads\logox.png"):
    col1, col2, col3 = st.columns([1, 8, 3])

    with col1:
        st.image(logo_path, width=110)
    with col2:
        st.title("LensCV")
        st.caption("Analyze. Improve. Stand Out.")
    with col3:
        for text in ["Fine-tuned specially for", "Computer Science roles."]:
            st.markdown(f"""
<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@700&display=swap" rel="stylesheet">

<p style="
    font-family:'Comfortaa', sans-serif;
    font-size:30px;
    font-weight:700;
    font-style:italic;
">
{text}
</p>
""", unsafe_allow_html=True)

    st.divider()


def render_sidebar() -> str:
    with st.sidebar:
        st.header("⚙️ Settings")
        st.success("✅ AI features are enabled")
        st.caption("Powered by Groq")
    return st.secrets["GROQ_API_KEY"]


def render_inputs():
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📤 Upload Resume")
        resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

    with col2:
        st.subheader("📋 Paste Job Description")
        jd_text = st.text_area("Paste the job description here", height=180,
                                placeholder="e.g. We are looking for a Python developer...")

    return resume_file, jd_text


def render_hiring_context_and_button():
    col1, col2 = st.columns([1, 1])  # 50% - 50%

    with col1:
        application_type = st.selectbox(
            "Hiring Context",
            [
                "Campus Placement",
                "Internship",
                "Off-Campus Application",
                "Experienced Hire"
            ],
            help="This changes how categories are weighted."
        )

    with col2:
        st.write("")  # pushes button down slightly
        analyze_btn = st.button(
            "🔍 Analyze Resume",
            type="primary",
            use_container_width=True
        )

    return application_type, analyze_btn
