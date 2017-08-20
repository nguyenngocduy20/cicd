# How to use this image #
## Build Docker image using Dockerfile ##
First, you need to build Docker image using Dockerfile.
Assume that you are in root directory: `./`
Example Dockerfile:
```
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
```

Using this command to build Docker image:
```
docker build -t my-django:python3 .
```

## Run container based on image buit recently ##
After building your own image, run container for first use:
```
docker run -dit --name django-app -p 8000:8000 -v $PWD:/usr/src/app/k8s_django/ my-django:python3
```
