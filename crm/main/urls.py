from django.urls import path
from . import views
from .views import LoginUser, logout_user

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),

    path('zayavlenie', views.zayavlenie, name='zayavlenie'),
    path('zayavlenie_FL', views.zayavlenie_FL, name='zayavlenie_FL'),
    path('zayavlenie_UL', views.zayavlenie_UL, name='zayavlenie_UL'),
    path('zayavlenie_GOS', views.zayavlenie_GOS, name='zayavlenie_GOS'),
    path('<int:pk>/card-delete_FL', views.CardsDeleteView_FL.as_view(), name='card-delete_FL'),
    path('<int:pk>/card-update_FL', views.CardsUpdateView_FL.as_view(), name='card-update_FL'),

    path('<int:pk>/card-delete_UL', views.CardsDeleteView_UL.as_view(), name='card-delete_UL'),
    # path('<int:pk>/card-update_UL', views.CardsUpdateView_UL.as_view(), name='card-update_UL'),


    path('spisok_zayavit_FL', views.spisok_zayavit_FL, name='spisok_zayavit_FL'),
    path('spisok_zayavit_UL', views.spisok_zayavit_UL, name='spisok_zayavit_UL'),
    # path('spisok_zayavit_GOS', views.spisok_zayavit_GOS, name='spisok_zayavit_GOS'),

    path('objects_card', views.objects_card, name='objects_card'),
    path('objects_list', views.objects_list, name='objects_list'),
    path('objects_search', views.objects_search, name='objects_search'),
    path('objects_registration', views.objects_registration, name='objects_registration'),

    path('statistik', views.statistik, name='statistik'),
    path('statistik_operator', views.statistik_operator, name='statistik_operator'),
    path('statistik_works', views.statistik_works, name='statistik_works'),
    path('statistik_analiz', views.statistik_analiz, name='statistik_analiz'),

    path('print', views.print_o, name='print'),
    path('print_report', views.print_report, name='print_report'),
    path('print_doc', views.print_doc, name='print_doc'),

    path('operators', views.operators, name='operators'),
    path('settings', views.settings, name='settings'),
    path('sites', views.sites, name='sites'),

    ]