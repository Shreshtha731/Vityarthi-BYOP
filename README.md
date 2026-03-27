# Vityarthi-BYOP
# SkillPath: Career & Project Intelligence Platform

## Overview
SkillPath is a web application designed to help students bridge the gap between learning isolated technical skills and achieving specific career goals. Users can search for a target career path and instantly receive recommended projects to build and skills to acquire. 

## Problem Statement
Students often lack clear, actionable roadmaps for portfolio building. SkillPath centralizes career requirements and suggests practical, real-world project ideas tailored to specific industry roles.

## Prerequisites
* Python 3.10+
* PostgreSQL

## Installation & Setup
1. **Clone the repository:**
   `git clone <your-github-repo-url>`
   `cd skillpath-byop`
2. **Set up a virtual environment:**
   `python -m venv venv`
   `source venv/bin/activate`  # On Windows use: venv\Scripts\activate
3. **Install dependencies:**
   `pip install -r requirements.txt`
4. **Database Configuration:**
   Ensure PostgreSQL is running. Create a database named `skillpath_db`. 
   Update the `DATABASES` dictionary in `core/settings.py` with your local Postgres credentials.
5. **Apply Migrations:**
   `python manage.py migrate`
6. **Run the Server:**
   `python manage.py runserver`
7. Access the application at `http://127.0.0.1:8000/`