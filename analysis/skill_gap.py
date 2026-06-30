from typing import List
from sklearn.metrics.pairwise import cosine_similarity
from utils.model import model
def get_skill_gap(resume_text: str, missing_keywords: List[str], top_n: int = 8):
    if not missing_keywords:
        return []
    resume_embedding = model.encode([resume_text])[0]
    missing_embeddings = model.encode(missing_keywords)
    similarities = cosine_similarity([resume_embedding], missing_embeddings)[0]
    ranked = sorted(zip(missing_keywords, similarities), key=lambda x: x[1])
    return ranked[:top_n]
