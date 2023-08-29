from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logoutPage, name="logout"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("createVacansy/", views.createVacansy, name="createVacansy"),
    path("allVacansy/", views.vacancies, name="AllVacansy"),
    path("allVacansy/<int:pk>/apply/", views.applyVacansy, name="applyVacansy"),
    path("allVacansy/<int:pk>/", views.vacansyDetail, name="vacancyDetail"),
    path("delete/<int:pk>/", views.deleteVacansy, name="delete"),
    path("update/<int:pk>/", views.updateVacansy, name="update"),
    path("forum", views.FAQ, name="forum"),
    path("deleteMessage/<int:pk>/", views.deleteMessage, name="deleteMess"),
    path(
        "choose_freelancer/<int:vacancy_id>/",
        views.choose_freelancer,
        name="choose_freelancer",
    ),
    path('done/<int:pk>/',views.doneVacansy,name='done')
]
