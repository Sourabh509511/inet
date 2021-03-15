from django.urls import path
from . import views

urlpatterns = [
    path('allcategory', views.allcategoryview.as_view()),
    path('createcategory', views.createcategory.as_view()),
    path('grandfather', views.grandfather_category_view.as_view()),
    path('father/<int:id>', views.fatherandchild_category_view.as_view()),
]
