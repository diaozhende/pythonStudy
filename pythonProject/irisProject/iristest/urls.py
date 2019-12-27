from django.urls import path, include, re_path
from iristest import views
urlpatterns = [
    path('knn/',views.iris_knn)
]