from django.urls import path,include
from .views import TaskList,TaskDetail,TaskCreate, TaskUpdate,TaskDelete,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',RegisterPage.as_view(),name="register"),
    path('login/',CustomLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
    path('',TaskList.as_view(),name="tasklist"),
    path('task/<int:pk>/',TaskDetail.as_view(),name="taskdetail"),
    path('task/create/',TaskCreate.as_view(),name="taskcreate"),
    path('task/update/<int:pk>/',TaskUpdate.as_view(),name="taskupdate"),
    path('task/delete/<int:pk>/',TaskDelete.as_view(),name="taskdelete"),
    
]
