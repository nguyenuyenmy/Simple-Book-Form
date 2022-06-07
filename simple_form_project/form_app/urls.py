from django.urls import path
from form_app import views

#TEMPLATE TAGGING
app_name = 'form_app'

urlpatterns = [
    path('author/<int:pk>/edit/', views.AuthorEditPopup, name='AuthorEdit'),
    path('author/<int:pk>/delete/', views.AuthorDeletePopup, name='AuthorDelete'),
    path('author/', views.author, name='author'),
]