from django.urls import path
app_name = 'contact'

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('export/xlsx', views.export, name='export_xlsx'),
    path('add/', views.add, name='add'),
    path('edit/<int:contact_id>', views.edit, name='edit'),
    path('del/<int:contact_id>', views.delete, name='delete'),
]