from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Room
from .forms import ClientForm, RoomForm

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'list-clients.html', {'clients': clients})

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client-details.html', {'client': client})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
        else:
          return render(request, 'add-client.html',{'error_msg': form.errors})
    else:
        form = ClientForm()
    return render(request, 'add-client.html', {'form1': form})

def client_update(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('reservation:client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client-update.html', {'form1': form, 'client': client})

def client_delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('reservation:client_list')
    return render(request, 'list-clients.html', {'client': client})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'list-room.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room-details.html', {'room': room})

def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reservation:room_list')
    else:
        form = RoomForm()
    return render(request, 'add-room.html', {'form1': form})

def room_update(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('reservation:room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'room-update.html', {'form1': form, 'room': room})

def room_delete(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.delete()
        return redirect('reservation:room_list')
    return render(request, 'list-room.html', {'room': room})
