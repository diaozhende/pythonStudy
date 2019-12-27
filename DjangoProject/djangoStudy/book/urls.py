from django.urls import path, re_path
from book import views

urlpatterns = [
    path('index', views.index),
    path('index_html', views.index_template),
    path('book_home', views.book_home),
    re_path(r'^bookRoleInfo/(\d+)$', views.bookRoleInfo),
    path('getTest', views.toBookGetTest),
    path('getServlet', views.bookGetTest),
    path('postServlet', views.bookPostTest)
]
