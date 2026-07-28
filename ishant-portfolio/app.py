"""
Ishant Kumar Gupta — Portfolio
A small Flask app serving a responsive, IDE-themed developer portfolio.

Run:
    python app.py
Then open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Data: certifications (NPTEL + Google Cloud)
# ---------------------------------------------------------------------------
CERTS = [
    {
        "title": "The Joy of Computing using Python",
        "org": "IIT Madras (NPTEL) · Elite",
        "score": "90%",
        "duration": "Jul–Oct 2025",
        "short": "PY",
        "img": "images/certs/nptel_python.png",
        "file": "nptel_joy_of_computing_python.png",
    },
    {
        "title": "Data Mining",
        "org": "IIT Kharagpur (NPTEL) · Elite",
        "score": "81%",
        "duration": "Jan–Mar 2026",
        "short": "DM",
        "img": "images/certs/nptel_datamining.png",
        "file": "nptel_data_mining.png",
    },
    {
        "title": "Fundamentals of Object Oriented Programming",
        "org": "IIT Roorkee (NPTEL) · Elite",
        "score": "80%",
        "duration": "Jan–Apr 2026",
        "short": "OOP",
        "img": "images/certs/nptel_oop.png",
        "file": "nptel_oop.png",
    },
    {
        "title": "Entrepreneurship and IP Strategy",
        "org": "IIT Kharagpur (NPTEL) · Elite",
        "score": "78%",
        "duration": "Jul–Sep 2025",
        "short": "IP",
        "img": "images/certs/nptel_ipstrategy.png",
        "file": "nptel_ip_strategy.png",
    },
    {
        "title": "Soft Skills",
        "org": "IIT Roorkee (NPTEL) · Elite",
        "score": "72%",
        "duration": "Jul–Oct 2024",
        "short": "SS",
        "img": "images/certs/nptel_softskills.png",
        "file": "nptel_soft_skills.png",
    },
    {
        "title": "Introduction to Exercise Physiology & Sports Performance",
        "org": "IIT Madras (NPTEL) · Elite",
        "score": "64%",
        "duration": "Aug–Oct 2024",
        "short": "EX",
        "img": "images/certs/nptel_exercisephysio.png",
        "file": "nptel_exercise_physiology.png",
    },
    {
        "title": "German - I",
        "org": "IIT Madras (NPTEL) · Elite",
        "score": "60%",
        "duration": "Jan–Apr 2025",
        "short": "DE",
        "img": "images/certs/nptel_german.png",
        "file": "nptel_german_1.png",
    },
    {
        "title": "Data Base Management System",
        "org": "IIT Kharagpur (NPTEL)",
        "score": "51%",
        "duration": "Jan–Mar 2025",
        "short": "DB",
        "img": "images/certs/nptel_dbms.png",
        "file": "nptel_dbms.png",
    },
    {
        "title": "Google Cloud Career Launchpad — Computing Foundations",
        "org": "Google Cloud",
        "score": None,
        "duration": "Issued Jan 2026",
        "short": "GC",
        "img": "images/certs/google_cloud.jpg",
        "file": "google_cloud_foundations.jpg",
    },
]

# ---------------------------------------------------------------------------
# Data: internships
# ---------------------------------------------------------------------------
INTERNSHIPS = [
    {
        "role": "Data Science Intern — Deep Learning & Computer Vision",
        "company": "Celebal Technologies",
        "location": "Remote",
        "duration": "18 May 2026 – 18 Jul 2026 (2 months)",
        "summary": "Completed a 2-month data science internship focused on applying deep learning and computer vision techniques to real-world satellite imagery analysis — from dataset preparation and transfer learning to building a deployable, interactive application. The internship gave practical exposure to the full lifecycle of an ML project, not just model training in isolation.",
        "project_name": "Satellite Land-Use Classification & Change Detection",
        "points": [
            "Built an end-to-end computer vision system to classify land-use types from satellite imagery and detect changes between two images of the same location over time.",
            "Used transfer learning with a ResNet-18 backbone (pretrained on ImageNet), fine-tuned in two phases — frozen backbone → selectively unfrozen deeper layers — on the EuroSAT dataset, improving validation accuracy from ~80% to over 95%.",
            "Designed a spatial, block-based train/validation split to prevent geographic data leakage, a common but often overlooked pitfall in satellite ML pipelines.",
            "Extended the model beyond classification by extracting image embeddings and using cosine similarity to detect and localize changes between before/after image pairs, visualized through a custom patch-based heatmap.",
            "Deployed the complete pipeline as an interactive Streamlit dashboard, letting users upload image pairs, view live predictions, adjust change-detection sensitivity, and inspect spatial heatmaps in real time.",
        ],
        "skills": ["PyTorch", "Transfer Learning", "CNNs (ResNet-18)", "Computer Vision", "Model Evaluation", "Data Leakage Prevention", "Streamlit", "Python"],
        "img": "images/internships/celebal.jpg",
        "file": "celebal_internship_certificate.jpg",
    },
    {
        "role": "Python & Machine Learning Intern",
        "company": "Kistechno Software Pvt. Ltd.",
        "location": "Jaipur, India",
        "duration": "16 Jun 2025 – 31 Jul 2025 (45 days)",
        "points": [
            "Architected supervised ML models using Scikit-learn, achieving a 15% increase in prediction accuracy through hyperparameter tuning.",
            "Optimized data pipelines with Pandas & NumPy, reducing cleaning time by 30% for datasets exceeding 50k rows.",
            "Produced automated EDA reports using Matplotlib and Seaborn to surface critical business KPIs.",
        ],
        "img": "images/internships/kistechno.jpg",
        "file": "kistechno_internship_certificate.jpg",
    },
    {
        "role": "Front-End Development Intern",
        "company": "Aerophantom",
        "location": "Mansarovar, Jaipur, Rajasthan",
        "duration": "8 Jul 2024 – 22 Jul 2024 (15 days)",
        "points": [
            "Developed high-performance responsive web pages using Bootstrap, improving mobile-user accessibility by 20%.",
            "Conducted cross-device testing and code minification, cutting page load latency by 25%.",
            "Integrated clean, modular UI components while collaborating in an Agile development environment.",
        ],
        "img": "images/internships/aerophantom.jpg",
        "file": "aerophantom_internship_certificate.jpg",
    },
]


@app.route("/")
def home():
    return render_template("index.html", active="home")


@app.route("/certifications")
def certifications():
    return render_template("certifications.html", active="certifications", certs=CERTS)


@app.route("/internships")
def internships():
    return render_template("internships.html", active="internships", internships=INTERNSHIPS)


@app.route("/competitions")
def competitions():
    return render_template("competitions.html", active="competitions")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    # debug=True is fine for local development; hosting platforms set PORT,
    # so we automatically turn debug off when running on a real host.
    debug_mode = "PORT" not in os.environ
    app.run(debug=debug_mode, host="0.0.0.0", port=port)
