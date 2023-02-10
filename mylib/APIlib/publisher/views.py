from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Publisher
from .serlializers import PublisherSerializer
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework import status


@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by name': '/?publisher=name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/publisher/pk/delete'
	}
	return Response(api_urls)

@api_view(['POST'])
def add_items(r):
	item = PublisherSerializer(data=r.data)

	if Publisher.objects.filter(**r.data).exists():
		raise serializers.ValidationError('this data is existed')

	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(r):
	if r.query_params:
		items = Publisher.objects.filter(**r.query_params.dict())
	else:
		items = Publisher.objects.all()
	if items:
		serializer = PublisherSerializer(items, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(r, pk):
	item = Publisher.objects.get(pk=pk)
	data = PublisherSerializer(instance=item, data=r.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def delete_items(r, pk):
	item = get_object_or_404(Publisher, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)
