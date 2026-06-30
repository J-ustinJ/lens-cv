import re
from typing import List

from data.aliases import ALIASES


def normalize_text(text: str) -> str:
    text = text.lower()

    for canonical, aliases in ALIASES.items():
        for alias in aliases:
            pattern = rf"\b{re.escape(alias)}\b"
            text = re.sub(pattern, canonical, text)

    return text


def split_jd_sections(jd_text: str):
    """
    Splits the JD into Required Skills and Preferred Skills sections.
    Returns:
        required_text, preferred_text
    """
    text = jd_text.lower()
    required_text = text
    preferred_text = ""
    if "preferred" in text:
        parts = re.split(r"preferred.*?:", text, maxsplit=1)
        required_text = parts[0]
        if len(parts) > 1:
            preferred_text = parts[1]
    return required_text, preferred_text


def keyword_exists(text: str, keyword: str) -> bool:
    text = text.lower()
    keyword = keyword.lower()
    # Exact keyword
    pattern = rf"\b{re.escape(keyword)}\b"
    if re.search(pattern, text):
        return True
    # Alias check
    aliases = ALIASES.get(keyword, [])
    for alias in aliases:
        alias_pattern = rf"\b{re.escape(alias.lower())}\b"
        if re.search(alias_pattern, text):
            return True
    return False


def find_keywords_in_text(text: str, keyword_list: List[str]) -> List[str]:
    return [kw for kw in keyword_list if keyword_exists(text, kw)]

