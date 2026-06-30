from typing import Dict, List

TECH_SKILLS: List[str] = [
    "python", "java", "c++", "c#", "javascript", "typescript", "r", "scala",
    "go", "rust", "sql", "bash", "machine learning", "deep learning",
    "neural network", "nlp", "natural language processing", "computer vision",
    "reinforcement learning", "supervised learning", "unsupervised learning",
    "transfer learning", "llm", "large language model", "generative ai",
    "genai", "rag", "retrieval augmented generation", "prompt engineering",
    "fine-tuning", "transformers", "bert", "gpt", "data structures",
    "algorithms", "object oriented programming", "operating systems",
    "competitive programming", "statistics", "linear algebra"
]
FRAMEWORKS_AND_LIBRARIES: List[str] = [
    "tensorflow", "pytorch", "keras", "scikit-learn", "opencv", "huggingface",
    "xgboost", "lightgbm", "pandas", "numpy", "matplotlib", "seaborn",
    "fastapi", "flask", "django", "streamlit", "react", "react.js",
    "node.js", "nodejs", "express", "vue", "angular", "tailwind css",
    "langchain", "langgraph", "chromadb", "vector database", "vector search",
    "embeddings", "sentence transformers", "spacy", "nltk", "axios", "vite"
]
CLOUD_AND_DEVOPS: List[str] = [
    "aws", "azure", "gcp", "google cloud", "docker", "kubernetes",
    "ci/cd", "ci cd", "jenkins", "terraform", "ansible", "mlops",
    "spark", "hadoop", "airflow", "mlflow", "serverless", "lambda",
    "ec2", "s3", "cloud computing"
]
TOOLS_AND_PLATFORMS: List[str] = [
    "git", "github", "gitlab", "linux", "postman", "vs code", "vscode",
    "jupyter notebook", "jupyter", "jira", "confluence", "figma",
    "ollama", "openai api", "groq api", "version control", "slack",
    "data pipeline", "uvicorn"
]
SOFT_SKILLS: List[str] = [
    "leadership", "communication", "teamwork", "problem solving",
    "problem-solving", "project management", "agile", "scrum",
    "collaboration", "critical thinking", "time management",
    "adaptability", "analytical", "presentation", "mentoring"
]
CERTIFICATIONS: List[str] = [
    "aws certified", "azure certified", "gcp certified", "pmp",
    "certified scrum master", "csm", "comptia", "ccna", "ckad", "cka",
    "coursera certificate", "deep learning specialization",
    "machine learning specialization", "google certified"
]
EDUCATION_KEYWORDS: List[str] = [
    "bachelor", "b.tech", "btech", "master", "m.tech", "mtech", "phd",
    "computer science", "engineering", "information technology",
    "data science", "artificial intelligence", "electronics",
    "university", "institute of technology", "college"
]
CATEGORY_MAP: Dict[str, List[str]] = {
    "Tech Skills": TECH_SKILLS,
    "Frameworks": FRAMEWORKS_AND_LIBRARIES,
    "Cloud/DevOps": CLOUD_AND_DEVOPS,
    "Tools": TOOLS_AND_PLATFORMS,
    "Soft Skills": SOFT_SKILLS,
    "Certifications": CERTIFICATIONS,
    "Education": EDUCATION_KEYWORDS,
}