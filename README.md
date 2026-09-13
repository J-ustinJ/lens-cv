# Resume Analyzer

A multi-dimensional, recruiter-style resume evaluation engine built with Streamlit, Sentence Transformers, and Groq LLaMA 3.3 70B.

---
## Live Demo
Try Demo now : [lens-cv-kgrlgfdcrpnwi6xfhv7y4z](https://lens-cv.streamlit.app/)
## Features

### Scoring System
- **Recruiter Match Score** — weighted category score tailored to your hiring context
- **ATS Keyword Score** — exact keyword match against the job description
- **Semantic Match Score** — cosine similarity between resume and JD embeddings
- **Category Breakdown** — per-category scores across 7 dimensions: Tech Skills, Frameworks, Cloud/DevOps, Tools, Soft Skills, Certifications, Education
- **Dynamic Weight Redistribution** — categories absent from the JD are excluded and never penalize the candidate; remaining weights are redistributed to always total 100%

### Hiring Contexts
Four scoring profiles with different category weights:
- **Campus Placement** — Education weighted higher
- **Internship** — Projects and Tech Skills weighted highest
- **Off-Campus Application** — Tech Skills dominate
- **Experienced Hire** — Education matters least; Cloud/DevOps weighted up

### AI Features (Groq)
- **AI Feedback** — strengths, weaknesses, and before/after rewrite suggestions
- **Interview Questions** — 8 questions tailored to your resume and JD
- **Learning Roadmap** — focused 2-3 week plan to close skill gaps
- **Recruiter Simulation** — shortlist probability, reasons to shortlist, concerns, and final verdict

### Visualization
- **Radar Chart** — Plotly radar showing all active category scores at a glance

### Other
- Resume structure check (Contact, Education, Experience, Skills, Projects)
- Semantic skill gap analysis ranked by distance from your resume
- Detailed matched/missing keywords per category in expandable sections

---

## Tech Stack

| Component | Library |
|---|---|
| UI | Streamlit |
| PDF Parsing | pdfplumber |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Semantic Similarity | scikit-learn cosine_similarity |
| LLM (feedback, questions, roadmap, recruiter) | Groq llama-3.3-70b-versatile |
| Visualization | Plotly |

---

## Setup

### 1. Clone or download the project

```bash
git clone <your-repo-url>
cd resume-analyzer
```

### 2. Install dependencies

```bash
pip install streamlit pdfplumber sentence-transformers scikit-learn groq plotly
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### 3. Get a Groq API key

- Go to [console.groq.com](https://console.groq.com)
- Sign up and create a free API key
- Free tier is sufficient for development

### 4. Run the app

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## Usage

1. **Enter your Groq API key** in the left sidebar
2. **Upload your resume** as a PDF (text-based, not scanned)
3. **Paste the job description** in the text area
4. **Select your hiring context** (Campus Placement / Internship / Off-Campus / Experienced Hire)
5. Click **Analyze Resume**

Results are displayed in order:
- Overall scores
- Category breakdown + radar chart
- Detailed per-category matched/missing keywords
- Recruiter simulation
- AI feedback
- Interview questions
- Learning roadmap
- Resume structure check
- Skill gap analysis

---

## Project Structure

```
resume-analyzer/
├── app.py              # Main application
├── requirements.txt    # Dependencies
└── README.md           # This file
```

---

## How Scoring Works

### Category Scoring
Each of the 7 categories has a curated keyword list. For a given JD:
1. Keywords from each category that appear in the JD become the "required" set for that category
2. The candidate's resume is checked against those required keywords
3. Score per category = matched / required × 100

### Dynamic Weight Redistribution
Each hiring context has a base weight profile across the 7 categories. If the JD doesn't mention any keywords from a category (e.g. no certifications), that category is removed from scoring entirely and its weight is redistributed proportionally among the remaining active categories. Final weights always sum to 100%.

### Final Recruiter Match Score
`final_score = Σ (category_score × active_weight)`

---

## Limitations

- PDF must be text-based (not a scanned image). Scanned PDFs return no extractable text.
- Keyword matching is case-insensitive exact string match — synonyms not in the keyword dictionaries won't be caught by the ATS score (though semantic score partially covers this).
- Groq free tier has rate limits — if you hit them, wait a minute and retry.
- The model (`all-MiniLM-L6-v2`) downloads ~80MB on first run, then is cached locally.
---

## License

MIT
