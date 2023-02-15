from django.urls import path
from .import views
urlpatterns = [
    path('', views.page1, name='home page'),
    path('2/',views.page2,name='page 2'),
    path('3/',views.page_html, name="html"),
    # path('4/',views.page_tb,name="table"),
    path('form/',views.form,name="form"),
    path('6/',views.form1,name="form"),
]
