from typing import Dict

WEIGHT_PROFILES:Dict[str, Dict[str, float]]={
    "Campus Placement":{
        "Education": 0.20, "Tech Skills": 0.35, "Frameworks": 0.15,
        "Cloud/DevOps": 0.10, "Tools": 0.05, "Soft Skills": 0.10,
        "Certifications": 0.05,
    },
    "Internship": {
        "Tech Skills": 0.40, "Frameworks": 0.20, "Cloud/DevOps": 0.10,
        "Tools": 0.10, "Soft Skills": 0.10, "Education": 0.05,
        "Certifications": 0.05,
    },
    "Off-Campus Application": {
        "Tech Skills": 0.45, "Frameworks": 0.20, "Cloud/DevOps": 0.15,
        "Tools": 0.10, "Soft Skills": 0.05, "Education": 0.03,
        "Certifications": 0.02,
    },
    "Experienced Hire": {
        "Tech Skills": 0.35, "Frameworks": 0.20, "Cloud/DevOps": 0.20,
        "Tools": 0.10, "Soft Skills": 0.10, "Certifications": 0.05,
    },
}
