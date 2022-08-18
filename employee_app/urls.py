from django.urls import path
from .views import EmployeeView
urlpatterns = [
    path('add_emp/', EmployeeView.as_view(), name='add-emp'),
    path('list_emp/', EmployeeView.as_view(), name='list_emp'),
    path('list_emp/<int:id>', EmployeeView.as_view(), name='list_emp_by_id'),
    path('update_emp/<int:id>', EmployeeView.as_view(), name='update_employee'),
    path('delete/<int:id>', EmployeeView.as_view(), name='delete_employee'),
    path('delete/', EmployeeView.as_view(), name='delete'),
    path('filter_emp/<str:emp_fname>', EmployeeView.as_view(), name='filter_emp')
]
