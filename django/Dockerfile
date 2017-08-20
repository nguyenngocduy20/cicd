FROM django:python3

WORKDIR /usr/src/app
EXPOSE 8000
RUN python -m django --version
RUN django-admin startproject k8s_django
WORKDIR /usr/src/app/k8s_django
RUN ls -laR
RUN python manage.py startapp firstApp
COPY . .
RUN ls -laR
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]