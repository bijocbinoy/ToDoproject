
from django.urls import path, include

from .import views

urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdeatil/<int:id>/',views.TaskDetailview.as_view(),name='cbvdetail'),
]