from django.contrib import admin
from .models import Employee, Room, Guest, Booking
from django.contrib import admin 
# from .models import User 

# admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Booking)
# Register your models here.