from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tasks import views

urlpatterns = [
    path('api/tasks/', views.get_all_tasks),
    path('api/tasks/<int:id>', views.get_task)
]

urlpatterns = format_suffix_patterns(urlpatterns)