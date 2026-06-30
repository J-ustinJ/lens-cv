from typing import List
from groq import Groq

def generate_feedback(client: Groq, resume_text: str, jd_text: str, missing_keywords: List[str]) -> str:
    prompt = f"""You are an expert technical recruiter and resume coach.
RESUME:
{resume_text[:3000]}
JOB DESCRIPTION:
{jd_text[:2000]}
MISSING KEYWORDS: {', '.join(missing_keywords[:15])}
Give specific, actionable feedback in this format:
1. Top 3 strengths of this resume for this JD (be specific, reference actual content)
2. Top 3 weaknesses / gaps for this JD
3. 3 concrete rewrite suggestions - show a "before" snippet from the resume and an "after" improved version that naturally incorporates missing keywords without lying about experience

Keep it concise and practical. Do not invent experience the candidate doesn't have - only suggest rephrasing existing experience using better terminology.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=1200,
    )
    return response.choices[0].message.content
