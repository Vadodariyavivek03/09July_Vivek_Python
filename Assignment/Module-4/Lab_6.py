import os

project_name = "hospital"
app_name = "doctor"

os.system(f"django-admin startproject {project_name}")

os.chdir(project_name)

os.system(f"python manage.py startapp {app_name}")

print(f"Django project '{project_name}' and app '{app_name}' created successfully.")
