from django.urls import path
from .import views

urlpatterns=[
    path("reg_user/",view=views.reg_user),
    path("all_users/",view=views.all_users),
    path("update_user/<int:id>",view=views.update_user),
    path("delete_user/<int:id>",view=views.delete_user)
]