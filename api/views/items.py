from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers.item import ItemSerializer
from ..models.item import Item

class ItemsView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        request.data['author'] = request.user.id
        item = ItemSerializer(data=request.data)
        if item.is_valid():
            item.save()
            return Response(item.data, status=status.HTTP_201_CREATED)
        else:
            return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)  

    def get(self, request):
        # filter for mangos with our user id
        items = Item.objects.all()
        data = ItemSerializer(items, many=True).data
        return Response(data)

class ItemView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        Item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        data = ItemSerializer(item).data
        return Response(data)
    
    def put(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        updated_item = ItemSerializer(item, data=request.data)
        if updated_item.is_valid():
            updated_item.save()
            return Response(updated_item.data)
        else:
            return Response(updated_item.errors, status=status.HTTP_400_BAD_REQUEST)