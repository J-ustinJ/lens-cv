from typing import Dict, List
from sklearn.metrics.pairwise import cosine_similarity
from data.keywords import CATEGORY_MAP
from utils.text_utils import normalize_text, keyword_exists, split_jd_sections, find_keywords_in_text
from utils.model import model

def semantic_skill_exists(resume_embedding, skill: str, threshold: float = 0.45):
    skill_embedding = model.encode([skill])[0]
    similarity = cosine_similarity([resume_embedding],[skill_embedding])[0][0]
    return similarity>=threshold

def extract_category_keywords_from_jd(jd_text: str) -> Dict[str, List[str]]:
    required = {}
    for category, keyword_list in CATEGORY_MAP.items():
        found=find_keywords_in_text(jd_text, keyword_list)
        if found:
            required[category] = found
    return required


def extract_preferred_keywords(jd_text: str):
    _, preferred_text = split_jd_sections(jd_text)
    preferred = {}
    for category, keyword_list in CATEGORY_MAP.items():
        found = find_keywords_in_text(preferred_text, keyword_list)
        if found:
            preferred[category] = found
    return preferred


def calculate_category_scores(resume_text: str, jd_text: str) -> Dict[str, Dict]:
    resume_text = normalize_text(resume_text)
    jd_text = normalize_text(jd_text)
    required_text, preferred_text = split_jd_sections(jd_text)
    jd_required = extract_category_keywords_from_jd(required_text)
    jd_preferred = extract_preferred_keywords(jd_text)
    category_scores: Dict[str, Dict] = {}
    resume_embedding = model.encode([resume_text])[0]
    for category, required_keywords in jd_required.items():
        if category == "Soft Skills":
            matched = [kw for kw in required_keywords if semantic_skill_exists(resume_embedding, kw)]
            missing = [kw for kw in required_keywords if not semantic_skill_exists(resume_embedding, kw)]
        else:
            matched = [kw for kw in required_keywords if keyword_exists(resume_text, kw)]
            missing = [kw for kw in required_keywords if not keyword_exists(resume_text, kw)]
        preferred_keywords = jd_preferred.get(category, [])
        preferred_matched = [kw for kw in preferred_keywords if keyword_exists(resume_text, kw)]
        required_weight = 2
        preferred_weight = 1
        earned = (len(matched) * required_weight + len(preferred_matched) * preferred_weight)
        possible = (len(required_keywords) * required_weight + len(preferred_keywords) * preferred_weight)
        score = round((earned / possible) * 100, 1) if possible else 0
        category_scores[category] = {
            "score": score,
            "matched": matched,
            "missing": missing,
            "preferred_matched": preferred_matched,
            "preferred_missing": [kw for kw in preferred_keywords if kw not in preferred_matched],
        }
    return category_scores

