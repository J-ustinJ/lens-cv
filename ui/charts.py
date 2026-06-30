from typing import Dict

import plotly.graph_objects as go


def get_match_grade(score: float):
    if score >= 95:
        return "A+", "🌟 Exceptional Match"
    elif score >= 90:
        return "A", "🟢 Excellent Match"
    elif score >= 80:
        return "B+", "🟢 Strong Match"
    elif score >= 70:
        return "B", "🔵 Good Match"
    elif score >= 60:
        return "C+", "🟡 Fair Match"
    elif score >= 50:
        return "C", "🟠 Moderate Match"
    elif score >= 40:
        return "D", "🔴 Weak Match"
    else:
        return "F", "⚫ Poor Match"


def build_radar_chart(category_scores: Dict[str, Dict]) -> go.Figure:
    categories = list(category_scores.keys())
    scores = [category_scores[c]["score"] for c in categories]

    # Close the loop for a proper radar shape
    categories_closed = categories + [categories[0]]
    scores_closed = scores + [scores[0]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=scores_closed,
        theta=categories_closed,
        fill='toself',
        name='Match Score',
        line=dict(color='#6366f1', width=2),
        fillcolor='rgba(99, 102, 241, 0.25)',
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(size=10)),
        ),
        showlegend=False,
        margin=dict(l=40, r=40, t=40, b=40),
        height=420,
    )
    return fig