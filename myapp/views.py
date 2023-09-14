from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response
# Create your views here.

class PersonListCreateAPI(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self, request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_data = {
            'success': True,
            'message': 'Person created successfully',
            'data': serializer.data
        }

        return Response(response_data)
        

class PersonDetail(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        response_data = {
            'success' : True,
            'data' : serializer.data    
        } 

        return Response(response_data)

class PersonUpdateAPIView(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception= True)
            serializer.save()

            response_data = {
                'success': True,
                'message': 'Person updated successfully',
                'data': {
                    'id': instance.pk,
                    'name': instance.name
                }
            }
            return Response(response_data)

        except Exception as e:
            response_data = {
                'success' : False,
                'message' : 'Failed to update person',
                'error': str(e)
            }
            return Response(response_data)


    
                    
class PersonDeleteAPIView(generics.DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        response_data = {
            'success' : True,
            'message' : 'Person deleted successfully'
        } 

        return Response(response_data)
    