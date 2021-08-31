from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import *
from .serializers import *
from .utils import *


@api_view(["GET"])
def list_slot(request):
    slots = Slot.objects.all()
    serializer = SlotSerializers(slots, many=True)
    data = success_response(serializer.data)
    return Response(data)


@api_view(["PUT"])
def update_slot(request,pk):
    slot=get_object_or_404(Slot,pk=pk)
    serializer = SlotSerializers(data=request.data,instance=slot)
    if serializer.is_valid():
        serializer.save()
        return Response(success_response(serializer.data))
    else:
        return Response(failure_response(serializer.errors))


@api_view(["POST"])
def create_slot(request):
    serializer = SlotSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(success_response(serializer.data))
    else:
        return Response(failure_response(serializer.errors))


@api_view(["POST"])
def park_slot(request):
    slots = Slot.objects.all()
    serializer = SlotSerializers(data=request.data)
    if serializer.is_valid():
        car_no = request.data.get("car_id")
        slot = slots.filter(vacant=True).first()
        if slot:
            slot.car_id = car_no
            slot.vacant = False
            slot.save()
        return Response(success_response(serializer.data))
    else:
        return Response(failure_response(serializer.errors))


@api_view(["DELETE"])
def unpark_slot(request, pk):
    slots = get_object_or_404(Slot, pk=pk)
    # serializer = SlotSerializers(slots)
    slots.car_id = None
    slots.vacant = True
    slots.save()
    return Response(success_response(msg="Car UnPark Successfully!"))


@api_view(["DELETE"])
def delete_slot(request, pk):
    slots = get_object_or_404(Slot, pk=pk)
    # serializer = SlotSerializers(slots)
    slots.delete()
    return Response(success_response(msg="Slot Deleted Successfully!"))
