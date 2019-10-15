from django.urls import path
#делаем свой список урлов для приложения
from .views import index, by_rubric, BbCreateView, add, add_save, add_and_save
from .views import index2, index3, index4, index5

urlpatterns =[
                #path('add/',BbCreateView.as_view(), name='add'),
                #path('add/save/', add_save, name='add_save'),
                #path('add/', add, name='add'),
                path('index2/', index2, name='index2'),
                path('index3/', index3, name='index3'),
                path('index4/', index4, name='index4'),
                path('index5/', index5, name='index5'),
                path('add/', add_and_save, name='add'),
                path('<int:rubric_id>/', by_rubric, name='by_rubric'),
                path('', index, name='index')
              ]