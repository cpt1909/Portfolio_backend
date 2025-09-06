from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app, origins=[
    "https://thaarakenthcp.vercel.app",
    "http://localhost:3000",
])



@app.route('/')
def index():
    client = MongoClient(os.getenv("DB_CONNECTION_STRING"))

    db = client["portfolio"]

    projects = db["projects"]
    skills = db["skills"]
    certifications = db["certifications"]
    education = db["education"]

    projectsData = [
        i for i in projects.find(
            {}, {
                "_id": 0,
                "sno": 0,
                }
            ).sort({"sno": 1})
    ]

    skillsData = [
        i for i in skills.find(
            {}, {
                "_id": 0,
                "sno": 0,
            }
        ).sort({"sno": 1})
    ]

    certificationsData = [
        i for i in certifications.find(
            {},{
                "_id": 0,
                "sno": 0,
            }
        ).sort({"sno": 1})
    ]

    educationData = [
        i for i in education.find(
            {},{
                "_id": 0,
                "sno": 0,
            }
        ).sort({"sno": -1})
    ]

    data = {
            "project" : projectsData,
            "skill" : skillsData,
            "certification": certificationsData,
            "education": educationData,
            }
    
    return jsonify(data)

if __name__ in "__main__":
    app.run(debug=True)