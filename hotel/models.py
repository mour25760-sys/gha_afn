from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     ROLE_CHOICES = (
#         ('admin', 'Admin'),
#         ('staff', 'Staff'),
#         ('user', 'User'),
#     )
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user', null=True)
#     groups = models.ManyToManyField('auth.Group', related_name='hotel_user_groups', blank=True) 
#     user_permissions = models.ManyToManyField('auth.Permission', related_name='hotel_user_permission', blank=True) 
#     address = models.CharField( null=True, max_length=10) 
#     def __str__(self):
#         return self.username

class Employee(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='اسم الموظف')
    email = models.EmailField(max_length=50, unique=True, null=True, verbose_name='حساب الموظف')
    phone = models.CharField(max_length=13, null=True, verbose_name='رقم هاتف الموظف')
    job_title = models.CharField(max_length=100, null=True, verbose_name='الوظيفة')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='راتب الموظف')
    def __str__(self):
        return self.name


class Room(models.Model):
    room_types = (('single', 'Single'), ('duble', 'Duble'), ('suite', 'Suite'))
    number = models.CharField(max_length=10, unique=True, null=True, verbose_name='رقم الغرفة')
    room_type = models.CharField(max_length=8, choices=room_types, null=True, verbose_name='نوع الغرفة')
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, verbose_name='سعر الغرفة') 
    is_available = models.BooleanField(default=True, null=True, verbose_name='إتاحة الغرفة')
    def __str__(self):
        return self.number


class Guest(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='اسم النزيل')
    passport_id = models.CharField(max_length=20, null=True, verbose_name='رقم جواز النزيل')
    email = models.EmailField(max_length=50, unique=True, null=True, verbose_name='حساب النزيل')
    phone = models.CharField(max_length=13, null=True, verbose_name='رقم جوال النزيل')
    decument = models.FileField(upload_to='decument', null=True, verbose_name='صورة بطاقة النزيل')
    def __str__(self): 
        return self.name


class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    def __str__(self):
        return self.guest

class Gallery(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='عنوان الصورة')
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name='رابط الصورة')
    video_url = models.URLField(blank=True, null=True, verbose_name='رابط الفيديو')
    def __str__(self):
        return self.title    

# Create your models here.
