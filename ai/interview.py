from groq import Groq
def generate_interview_questions(client: Groq, resume_text: str, jd_text: str) -> str:
    prompt = f"""Based on this resume and job description, generate 8 likely interview questions
the candidate should prepare for. Mix technical and behavioral questions.
Reference specific projects/skills from the resume where relevant.

RESUME:
{resume_text[:3000]}

JOB DESCRIPTION:
{jd_text[:2000]}

Format as a numbered list. For technical questions, briefly note what the interviewer is testing for.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=800,
    )
    return response.choices[0].message.content