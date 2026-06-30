import re
from collections import Counter
from typing import List
from data.keywords import CATEGORY_MAP
from utils.text_utils import keyword_exists, find_keywords_in_text


def extract_jd_keywords(jd_text: str) -> List[str]:
    """Flat keyword extraction used for the legacy ATS score + skill gap view."""
    jd_lower = jd_text.lower()
    all_known = [kw for cat_list in CATEGORY_MAP.values() for kw in cat_list]
    jd_skills = find_keywords_in_text(jd_lower, all_known)

    words = re.findall(r'\b[a-zA-Z]{3,}\b', jd_text)
    word_freq = Counter(w.lower() for w in words)
    stopwords = {"the", "and", "for", "with", "you", "our", "will", "are",
                 "this", "that", "have", "from", "your", "not", "but", "was",
                 "can", "all", "they", "which", "been", "has", "its", "more",
                 "who", "what", "when", "how", "also", "both", "must", "should",
                 "work", "team", "role", "skills", "experience", "ability"}
    extra_keywords = [w for w, freq in word_freq.most_common(30)
                       if w not in stopwords and len(w) > 3 and freq >= 2]
    return list(set(jd_skills + extra_keywords))


def calculate_ats_score(resume_text: str, jd_keywords: List[str]):
    matched = [kw for kw in jd_keywords if keyword_exists(resume_text, kw)]
    missing = [kw for kw in jd_keywords if not keyword_exists(resume_text, kw)]
    score = round((len(matched) / len(jd_keywords)) * 100, 1) if jd_keywords else 0
    return score, matched, missing
