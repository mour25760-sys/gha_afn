from django import forms
from .models import Employee, Room, Guest, Booking, Gallery
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput) 
    confirmpass = forms.CharField(widget=forms.PasswordInput) 
    class Meta: 
        model = User 
        fields = [ 'username', 'email', 'password' ] 
        def clean(self): 
            cleaned_data = super().clean() 
            password = cleaned_data.get('password') 
            confirmpass = cleaned_data.get('confirmpass') 
            if password != confirmpass: 
                raise forms.ValidationError("كلمتا المرور غير متطابقتين") 
            return cleaned_data

class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المستخدم'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور'}))    


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        # widgets = {
        # #     'name': forms.CharField(attrs={'class': 'form-control mb-2'}),
        # #     'phone': forms.CharField(attrs={'class': 'form-control mb-2'}),
        # #     'job_title': forms.CharField(attrs={'class': 'form-control mb-2'}),
        # #     'email': forms.EmailField(attrs={'class': 'form-control mb-2'}),
        # #     'salary': forms.DecimalField(attrs={'class': 'form-control mb-2'}),
        # }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الغرفة'}),
            'room_type': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'passport_id', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم النزيل'}),
            # 'room_type': forms.Select(attrs={'class': 'form-control'}),
            # 'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest', 'room', 'check_in', 'check_out']
        widgets = {
            'guest': forms.Select(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
            'check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image_url', 'video_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان الصورة/الفيديو'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'رابط الصورة من جوجل'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'رابط الفيديو من يوتيوب'}),
        }
