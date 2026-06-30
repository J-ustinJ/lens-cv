from typing import Dict
def check_resume_structure(resume_text: str) -> Dict[str, bool]:
    text = resume_text.lower()
    return {
        "Contact Info": any(w in text for w in ["email", "phone", "linkedin", "@"]),
        "Education": any(w in text for w in ["education", "university", "degree", "bachelor", "master", "b.tech", "b.e"]),
        "Experience": any(w in text for w in ["experience", "internship", "worked", "engineer", "developer", "analyst"]),
        "Skills": any(w in text for w in ["skills", "technologies", "tools", "proficient"]),
        "Projects": any(w in text for w in ["project", "built", "developed", "created", "implemented"]),
    }
