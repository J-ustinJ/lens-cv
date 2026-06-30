from sklearn.metrics.pairwise import cosine_similarity
from utils.model import model
def calculate_semantic_score(resume_text: str, jd_text: str) -> float:
    embeddings = model.encode([resume_text, jd_text])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(float(similarity) * 100, 1)
