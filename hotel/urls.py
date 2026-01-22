from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_page , name='homepage'),
    path('booking_list/', views.booking_list , name='bookpage'),
    path('booking_edit/<int:id>/', views.booking_edit , name='editbookpage'),
    path('hotel/management/', views.hellow_page , name='hellow_page'),
    path('employee_list/', views.employee_list , name='employeelist'),
    path('gallery_page/', views.gallery_page  , name='gallerypage'),
    path('room_list/', views.room_list  , name='roomlist'),
    path('room_add/', views.add_room  , name='room_add'),
    path('room/edit/<int:id>/', views.room_edit  , name='room_edit'),
    path('new_booking/', views.new_booking  , name='newbooking'),
    path('employees/edit/<int:id>/', views.employee_edit  , name='employee_edit'),
    path('employee_add/', views.employee_add  , name='employee_add'),
    path('employee/delete/<int:id>/', views.employee_delete  , name='employee_delete'),
    path('room/delete/<int:id>/', views.room_delete  , name='room_delete'),
    path('booking/delete/<int:id>/', views.booking_delete  , name='booking_delete'),
    path('add/media/', views.add_media  , name='add_media'),
    path('media/list/', views.media_list  , name='media_list'),
    path('edit/media/<int:id>/', views.edit_media  , name='edit_media'),
    path('delete/media/<int:id>/', views.delete_media  , name='delete_media'),
    path('register/', views.register_view, name='register'), 
    path('login/', views.login_view, name='login'),
    path('add/guest/', views.guest_add  , name='guest_add'),
    path('guest/list/', views.guest_list  , name='guest_list'),
    path('edit/guest/<int:id>/', views.guest_edit  , name='guest_edit'),
    path('delete/guest/<int:id>/', views.guest_delete  , name='guest_delete'),
    # path('logout/', logout_view, name='logout'),





    # path('logout/', userlogout, name='logout'),
    
    # path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    # path('employees/add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    # path('employees/edit/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_edit'),
    # path('employees/delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    # path('gallery/', views.gallery_view, name='gallery'),
]