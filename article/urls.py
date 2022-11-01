from django.contrib import admin
from django.urls import path #include는 import하지 않아도 됨 

urlpatterns = [ #이하는 모두 상위 프로젝트의 urls.py에서 관리하던 articles의 url    
    path('dinner/<str:name>', views.dinner, name="dinner"),     
    path('review/', views.review),    
    path('create_review/', views.create_review),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete', views.delete, name="delete"),
    path('<int:pk>/edit', views.delete, name="edit"),
    path('<int:pk>/update/', views.update, name="update"),
]
