from django.contrib import admin

# Register your models here.
kube-master1@kube-master1:~/kube-workspaces/kubernetes/django$ docker exec -it f3b cat /usr/src/app/k8s_django/firstApp/apps.py
from django.apps import AppConfig


class FirstappConfig(AppConfig):
    name = 'firstApp'
