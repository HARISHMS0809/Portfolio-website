from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

projects = [
    {
        "id": 0,
        "title": "RAG-Based Employee Onboarding Assistant",
        "category": "AI/Web Development",
        "year": "2025",
        "description": "AI-powered web app analyzing offer and joining letters using Retrieval-Augmented Generation (RAG). Deployed on Microsoft Azure with Docker CI/CD pipeline.",
        "tech": ["Flask", "FAISS", "Sentence-Transformers", "Docker", "Azure"],
        "link": "#"
    },
    {
        "id": 1,
        "title": "Arduino-Based CAN Protocol Implementation",
        "category": "Embedded Systems",
        "year": "2025",
        "description": "Real-time vehicle control system using Arduino and CAN bus protocol. Integrated collision avoidance, speed monitoring, and emergency alert systems.",
        "tech": ["Arduino", "CAN Protocol", "Embedded C"],
        "link": "#"
    },
    {
        "id": 2,
        "title": "Failure Prediction in Industrial Machinery",
        "category": "Machine Learning",
        "year": "2024",
        "description": "Predictive maintenance system using ML models for fault detection. Published at Springer ICICC 2025 Conference.",
        "tech": ["Python", "Scikit-learn", "Machine Learning"],
        "link": "https://github.com/HARISHMS08"
    },
    {
        "id": 3,
        "title": "Honey Adulteration Detection",
        "category": "Machine Learning",
        "year": "2023",
        "description": "ML model achieving 92% accuracy in detecting honey adulteration using spectral data analysis and supervised learning algorithms.",
        "tech": ["Python", "SVM", "Random Forest", "XGBoost"],
        "link": "#"
    }
]

contacts = {
    "email": "harishms.info@gmail.com",
    "phone": "+91 6304713067",
    "linkedin": "https://linkedin.com/in/harish-murugesan-sivakumar",
    "github": "https://github.com/HARISHMS08",
    "leetcode": "https://leetcode.com/HARISHMS08",
    "website": "https://harishms.info"
}

skills = {
    "languages": ["Python","Java", "Embedded C"],
    "web": ["HTML", "CSS", "JavaScript"],
    "data_science": ["Machine Learning", "Scikit-learn", "Deep Learning", "SQL", "MongoDB"],
    "tools": ["VS Code", "GitHub", "Docker", "Jenkins", "Azure DevOps", "MATLAB"]
}

education = [
    {
        "school": "Vellore Institute of Technology",
        "degree": "B.Tech in Electronics and Communication Engineering",
        "period": "Sept 2021 – May 2025",
        "details": "CGPA: 8.22"
    },
    {
        "school": "Sri Chaitanya Junior College",
        "degree": "Higher Secondary Certificate (XII)",
        "period": "2019 – 2021",
        "details": "Percentage: 82.2%"
    },
    {
        "school": "Prakasam Vidyalaya E. M. School",
        "degree": "Secondary Certificate (X)",
        "period": "2019 – 2021",
        "details": "GPA: 9.5"
    }

]

experience = [
    {
        "company": "Bharat Heavy Electricals Limited (BHEL)",
        "position": "Intern",
        "period": "Aug 2023 – Sept 2023",
        "location": "Visakhapatnam, Andhra Pradesh",
        "highlights": [
            "Designed and implemented a flap gate control system using Arduino",
            "Developed an automated number plate recognition system",
            "Strengthened skills in microcontroller programming and real-time system optimization"
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects, contacts=contacts, skills=skills, education=education, experience=experience)

if __name__ == '__main__':
    app.run(debug=True)