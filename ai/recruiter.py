from groq import Groq
def generate_recruiter_evaluation(
    client: Groq,
    resume_text: str,
    jd_text: str,
    final_score: float,
    application_type: str
) -> str:
    """Simulates a recruiter's shortlist decision."""
    prompt = f"""You are a recruiter reviewing this candidate for a {application_type} role.

RESUME:
{resume_text[:3000]}

JOB DESCRIPTION:
{jd_text[:2000]}

COMPUTED MATCH SCORE: {final_score}%

Provide your evaluation in this exact structure:
1. **Shortlist Probability (%)** - your own estimate, can differ from the computed score above, with one line of reasoning
2. **Top reasons to shortlist** - 3 bullet points, specific to this resume
3. **Top concerns** - 3 bullet points, specific to this resume
4. **Final recommendation** - one paragraph, direct and honest

Be realistic and specific - avoid generic filler. Reference actual resume content.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=900,
    )
    return response.choices[0].message.content
