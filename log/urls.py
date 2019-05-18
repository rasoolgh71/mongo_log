from django.urls import path
from . import views
from log.views import LogView,Home

urlpatterns = [
    # path('get_upload/', views.get_upload_file, name='get_upload'),
    # path('datatable/', SoldierDataTableView.as_view(), name='DatatableSoldier'),
    # path('create_soldiers_1/', show.as_view(), name='create_soldiers_1'),
    path('create_Log/', LogView.as_view(), name='create_Log'),
    path('', Home.as_view(), name='home'),
]
