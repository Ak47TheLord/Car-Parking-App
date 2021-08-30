from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.views.decorators.csrf import csrf_exempt
from .decorators import unauthenticated_user, allowed_user


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/include/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'account/include/profile.html')


def homeView(request):
    context = {
        'home_active': 'active'
    }
    return render(request, 'account/include/home.html', context)


@allowed_user(allowed_roles=['admin'])
@csrf_exempt
def parkView(request):
    all_slot = Slot.objects.all()
    park_form = ParkForm()
    if request.method == 'POST':
        park_form = ParkForm(request.POST)
        if park_form.is_valid():
            car_no = park_form.cleaned_data.get("car_id")
            slot = all_slot.filter(vacant=True).first()
            if slot:
                print(slot.vacant)

                print(car_no)
                slot.car_id = car_no
                slot.vacant = False
                slot.save()
                # Car No. -- has been parked successfully at Slot No. --
                txt = f"{car_no} has been parked successfully at {slot.id}"
                messages.success(request, txt)
                return redirect('parkView')

            else:
                messages.error(request, 'Space is not vacant for parking')
    context = {
        'park_form': park_form,
        'slots': all_slot,
        'parkin_active': 'active'

    }
    return render(request, 'account/include/parkin.html', context)


@allowed_user(allowed_roles=['admin'])
@login_required
@csrf_exempt
def slots(request):
    all_slot = Slot.objects.all()
    unpark_form = ParkForm()
    # if request.method == 'POST':
    #     unpark_form = ParkForm(request.POST)
    #     if unpark_form.is_valid():
    #         car_id = unpark_form.cleaned_data['car_id']
    #         slot = all_slot.filter(car_id=car_id).first()
    #         if slot:
    #             slot.vacant = True
    #             slot.car_id = None
    #             slot.save()
    #             txt = f"{car_id} has been un-parked successfully at {slot.id}"
    #             messages.success(request, txt)
    #             return redirect('un-park')
    #         else:
    #             messages.error(request, 'Space is not vacant for parking')
    context = {
        'unpark_form': unpark_form,
        'slots': all_slot,
        'slot_active': 'active'

    }
    return render(request, 'account/include/unpark.html', context)


@allowed_user(allowed_roles=['admin'])
def unpark_slot(request, slot_id):
    slot = Slot.objects.get(pk=slot_id)
    slot.car_id = None
    slot.vacant = True
    slot.save()
    return redirect("slots")

# @csrf_exempt
# def unparkD(request, slot_id=id):
#     all_slot = Slot.objects.all()
#     if request.method == 'POST':
#         unpark_form = ParkForm(request.POST)
#         if unpark_form.is_valid():
#             slot_id = unpark_form.cleaned_data['slot_id']
#             slot = all_slot.filter(id=slot_id).first()
#             if slot:
#                 slot.vacant = True
#                 slot.car_id = None
#                 slot.save()
#                 txt = f"{slot.car_id} has been un-parked successfully at {slot.id}"
#                 messages.success(request, txt)
#                 return redirect('un-park')
#             else:
#                 messages.error(request, 'Space is not vacant for parking')
#                 context = {
#                     'unpark_form': unpark_form,
#                     'slots': all_slot,
#
#                 }
#                 return render(request, 'account/include/unpark.html', context)

# def unpark(request, slot_id=id):
#     slot = Slot.objects.get(id=slot_id)
#     if slot:
#         Slot.vacant = True
#         Slot.car_id = None
#         return render(request, 'account/include/unpark.html', {
#             'slot': slot
#         })
#     else:
#         return messages.error(request, 'Invalid Slot')
#
#
# def information(request, Type, value):
#     Slot.obj = None
#     if Type == 'Car':
#         Slot.obj = Slot.objects.filter(car_id=value)
#         return render(request, 'account/include/profile.html', {
#             'car-id': Slot.obj.car - id,
#             'slot': Slot.obj.id
#         })
#     elif Type == 'Slot':
#         Slot.obj = Slot.objects.filter(id=value)
#         return render(request, 'account/include/profile.html', {
#             'car-id': Slot.obj.car - id,
#             'slot': Slot.obj.id
#         })
#     if Slot.obj:
#         return messages(request, "All Slots Filled")
