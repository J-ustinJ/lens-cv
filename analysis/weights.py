from typing import Dict, Tuple
from data.weights import WEIGHT_PROFILES

def get_active_weights(category_scores: Dict[str, Dict], application_type: str) -> Dict[str, float]:
    #Takes the base weight profile for the hiring context, drops any category not present in category_scores (i.e. not mentioned
    # in the JD at all), then redistributes the dropped weight proportionally among the
    # remaining active categories so the total is always 100%.
    base_weights = WEIGHT_PROFILES[application_type]

    # Only categories that are both in the profile AND actually required by the JD
    active_categories = [cat for cat in base_weights if cat in category_scores]

    if not active_categories:
        return {}

    raw_total = sum(base_weights[cat] for cat in active_categories)
    if raw_total == 0:
        # Fallback: equal split if something odd happens
        equal_share = 1.0 / len(active_categories)
        return {cat: round(equal_share * 100, 1) for cat in active_categories}

    # Redistribute proportionally so active weights sum to 100%
    active_weights = {
        cat: round((base_weights[cat] / raw_total) * 100, 1)
        for cat in active_categories
    }
    return active_weights


def calculate_weighted_match_score(category_scores: Dict[str, Dict],application_type: str) -> Tuple[float, Dict[str, float]]:
    #Combines per-category scores using context-aware, redistributed weights.
    #Returns (final_score, active_weights).
    active_weights = get_active_weights(category_scores, application_type)
    if not active_weights:
        return 0.0, {}

    final_score = 0.0
    for category, weight_pct in active_weights.items():
        category_score = category_scores[category]["score"]
        final_score += category_score * (weight_pct / 100)

    return round(final_score, 1), active_weights
