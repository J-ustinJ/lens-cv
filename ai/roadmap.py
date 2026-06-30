from typing import List
from groq import Groq
def generate_learning_roadmap(client: Groq, missing_keywords: List[str], jd_text: str) -> str:
    prompt = f"""A candidate is missing these skills/keywords for a job they want: {', '.join(missing_keywords[:10])}

JOB DESCRIPTION CONTEXT:
{jd_text[:1500]}

Create a focused 2-3 week learning roadmap to close the most important gaps.
Prioritize by impact. For each item give: what to learn, one concrete resource type (course/doc/project idea), and estimated time.
Keep it realistic and concise - a numbered list, not an essay.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=700,
    )
    return response.choices[0].message.content
