# 1. Initialize the project folder and git
mkdir skillpath-byop
cd skillpath-byop
git init

# 2. Set up the virtual environment and install Django
(most important step to isolate the project from global system)
python -m venv venv
source venv/bin/activate
pip install django psycopg2-binary
pip freeze > requirements.txt

# 3. Create the Django project and app
django-admin startproject core .
python manage.py startapp pathways

# 4. Make your first commit
echo "venv/" > .gitignore
git add .
git commit -m "Initial commit: Setup Django project and pathways app"