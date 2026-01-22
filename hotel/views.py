from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        confirm = request.POST.get('confirm') 

        if password != confirm: 
            return render(request, 'register.html', { 'error': 'كلمتا المرور غير متطابقتين' }) 

        if User.objects.filter(username=username).exists(): 
            return render(request, 'register.html', { 'error': 'اسم المستخدم موجود مسبقًا' }) 

        User.objects.create_user( username=username, password=password ) 
        return redirect('login.html') 
    return render(request, 'register.html') 
    
    
def login_view(request): 
    if request.user.is_authenticated:
        pass
    if request.method == "POST": 
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate( request, username=username, password=password ) 
        if user is not None: 
            login(request, user) 
            return redirect('hellow_page') 
        else: 
            return render(request, 'login.html', { 'error': 'اسم المستخدم أو كلمة المرور غير صحيحة' }) 
    return render(request, 'login.html')
    
    
def logout_view(request): 
    logout(request) 
    return redirect('login.html')


def home_page(request):
    return render(request, "home.html")


@login_required(login_url= 'login')
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, "hotel_managment/booking_list.html", {'bookings': bookings})

@login_required(login_url= 'login')
def booking_edit(request, id):
    booking_ed = Booking.objects.get(id = id)
    form = BookingForm(instance = booking_ed)
    if request.method == "POST":
        form = BookingForm(request.POST, instance = booking_ed)
        if form.is_valid():
            form.save()
            return messages.success(request, 'it is done successfully.')
            return redirect('bookpage')
        else:   
            form = BookingForm()
    return render(request, "hotel_managment/edit_booking.html", {'form': form})       

 
@login_required(login_url= 'login')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "hotel_managment/employee_list.html", {'employees': employees}) 

def gallery_page(request):
    gallerys = Gallery.objects.all()
    return render(request, "gallery.html", {'gallerys': gallerys}) 


@ login_required(login_url= 'login')
def room_list(request): 
    rooms = Room.objects.all()
    return render(request, "hotel_managment/room_list.html", {'rooms': rooms})

 
@login_required(login_url= 'login')
def add_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successful.')
            return redirect('roomlist')
        else:   
            form = RoomForm()     
    # rooms = Room.objects.all()

    # if request.method == "POST":
    #     r_number = request.POST.get('number')
    #     r_type = request.POST.get('room_type')
    #     r_price = request.POST.get('price')
       

    #     Room.objects.create(
    #         number=r_number,
    #         room_type=r_type,
    #         price=r_price
    #     )
    #     return redirect('roomlist')
     
    return render(request, "hotel_managment/room_add.html", {'form': form})    

 
@login_required(login_url= 'login')
def new_booking(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            #  return messages.success(request, 'successful.')
            return redirect('bookpage')
        else:   
            form = BookingForm()
    
    # rooms = Room.objects.all()

    # if request.method == "POST":
    #     guest = request.POST.get('guest_name')
    #     room_id = request.POST.get('room')
    #     check_in = request.POST.get('check_in')
    #     check_out = request.POST.get('check_out')
       
    #     selected_room = Room.objects.get()
    #     Booking.objects.create(
    #         guest_name=guest_name,
    #         room=selected_room,
    #         check_in_date=check_in,
    #         check_out_date=check_out
    #     )
    #     return redirect('bookpage')    
    return render(request, "hotel_managment/new_booking.html", {'form': form})


@login_required(login_url= 'login')
def hellow_page(request):

    return render(request, "hotel_managment/hellow_page.html")

@login_required(login_url= 'login')
def employee_edit(request, id):
    # employee_obj = get.object_or_404(Employee)
    employee_ed = Employee.objects.get(id = id)
    form = EmployeeForm(instance = employee_ed)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance = employee_ed)
        if form.is_valid():
            form.save()
            messages.success(request, 'it is done successfully.')
            return redirect('employeelist')
        else:   
            form = EmployeeForm()
    return render(request, "hotel_managment/employee_edit.html", {'form': form})

 
@login_required(login_url= 'login')
def employee_add(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successful.')
            return redirect('employeelist')
        else:   
            form = EmployeeForm()

    #     emp_name = request.POST.get('name')
    #     emp_phone = request.POST.get('phone')
    #     emp_job = request.POST.get('job_title')
    #     emp_salary = request.POST.get('salary')
    
    #     Employee.objects.create(
    #         name=emp_name,
    #         phone=emp_phone,
    #         job_title=emp_job,
    #         salary=emp_salary
    #     )
    #     return redirect('employeelist')


    return render(request, "hotel_managment/employee_add.html", {'form' : form})

 
@login_required(login_url= 'login')
def employee_delete(request, id):
    employee_ed = Employee.objects.get(id = id)
    if request.method == "POST":
        employee_ed.delete()
        return redirect('employeelist')
    
    return render(request, "hotel_managment/employee_delete.html", {'employee_ed': employee_ed})

 
@login_required(login_url= 'login')
def room_edit(request, id):
    room_ed = Room.objects.get(id = id)
    form = RoomForm(instance = room_ed)
    if request.method == "POST":
        form = RoomForm(request.POST, instance = room_ed)
        if form.is_valid():
            form.save()
            messages.success(request, 'it is done successfully.')
            return redirect('roomlist')
        else:   
            form = RoomForm()
    return render(request, "hotel_managment/room_edit.html", {'form' : form })

 
@login_required(login_url= 'login')
def room_delete(request, id):
    room_ed = Room.objects.get(id = id)
    if request.method == "POST":
        room_ed.delete()
        return redirect('roomlist')
    
    return render(request, "hotel_managment/room_delete.html", {'room_ed': room_ed})

 
@login_required(login_url= 'login')
def booking_delete(request, id):
    booking_ed = Booking.objects.get(id = id)
    if request.method == "POST":
            booking_ed.delete()
            return redirect('bookpage')
    
    return render(request, "hotel_managment/booking_delete.html", {'booking_ed': booking_ed}) 

 
@login_required(login_url= 'login')
def add_media(request):
    form = GalleryForm()
    if request.method == "POST":
        form = GalleryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successful.')
            return redirect('gallerypage')
        else:   
            form = GalleryForm()
    
    return render(request, "hotel_managment/add_media.html", {'form' : form})

 
@login_required(login_url= 'login')
def media_list(request):
    gallerys = Gallery.objects.all()
    return render(request, "hotel_managment/media_list.html", {'gallerys' : gallerys})

@login_required(login_url= 'login')
def edit_media(request, id):
    gallery_ed = Gallery.objects.get(id = id)
    form = GalleryForm(instance = gallery_ed)
    if request.method == "POST":
        form = GalleryForm(request.POST, instance = gallery_ed)
        if form.is_valid():
            form.save()
            messages.success(request, 'it is done successfully.')
            return redirect('media_list')
        else:   
            form = GalleryForm()
    return render(request, "hotel_managment/edit_media.html", {'form' : form})

 
@login_required(login_url= 'login')
def delete_media(request, id):
    gallery_ed = Gallery.objects.get(id = id)
    if request.method == "POST":
            gallery_ed.delete()
            return redirect('media_list')

    return render(request, "hotel_managment/media_delete.html", {'gallery_ed': gallery_ed})

@login_required(login_url= 'login')
def guest_edit(request, id):
    guest_ed = Guest.objects.get(id = id)
    form = GuestForm(instance = guest_ed)
    if request.method == "POST":
        form = GuestForm(request.POST, instance = guest_ed)
        if form.is_valid():
            form.save()
            messages.success(request, 'it is done successfully.')
            return redirect('guest_list')
        else:   
            form = GuestForm()
    return render(request, "hotel_managment/guest_edit.html", {'form': form})

@login_required(login_url= 'login')
def guest_delete(request, id):
    guest_ed = Guest.objects.get(id = id)
    if request.method == "POST":
            guest_ed.delete()
            return redirect('guest_list')

    return render(request, "hotel_managment/guest_delete.html", {'guest_ed': guest_ed})


@login_required(login_url= 'login')
def guest_add(request):
    form = GuestForm()
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successful.')
            return redirect('guest_list')
        else:
            pass   
            # form = GuestForm() 
    return render(request, "hotel_managment/guest_add.html", {'form': form})

@ login_required(login_url= 'login')
def guest_list(request): 
    guests = Guest.objects.all()
    return render(request, "hotel_managment/guest_list.html", {'guests': guests})
          
# class EmployeeListView(ListView):
#     model = Employee
#     template_name = 'employee_list.html'
#     context_object_name = 'employees'


# class EmployeeCreateView(CreateView):
#     model = Employee
#     fields = '__all__'
#     template_name = 'employee_form.html'
#     success_url = reverse_lazy('employee_list') 

# class EmployeeUpdateView(UpdateView):
#     model = Employee
#     fields = '__all__'
#     template_name = 'employee_form.html' 
#     success_url = reverse_lazy('employee_list')


# class EmployeeDeleteView(DeleteView):
#     model = Employee
#     template_name = 'delete_confirm.html'
#     success_url = reverse_lazy('employee_list')


# def gallery_view(request):
#     items = Gallery.objects.all()
#     return render(request, 'gallery.html', {'items': items})

# def home_view(request):
#     return render(request, 'home.html')       