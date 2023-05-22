from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.index, name = 'index'),
    path('machines/',views.machine_list_view, name='machines'),
    path('machine/<pk>', views.machine_detail_view ,name='machine-detail'),
    path('add-machine' , views.machine_add_form , name='add-machine'),
    path('delete-machine' , views.machine_delete_form , name='delete-machine'),
    path('personnes/',views.personne_list_view, name='personnes'),
    path('personne/<pk>', views.personne_detail_view , name='personne-detail'),
    path('add-personne' , views.personne_add_form , name='add-personne'),
    path('delete-personne' , views.personne_delete_form , name='delete-personne'),
    path('groupes/',views.groupe_list_view, name='groupes'),
    path('groupe/<pk>', views.groupe_detail_view ,name='groupe-detail'),
    path('add-groupe' , views.groupe_add_form , name='add-groupe'),
    path('delete-groupe' , views.groupe_delete_form , name='delete-groupe'),
]


