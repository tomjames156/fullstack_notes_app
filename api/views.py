from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
from .models import Note
from .serializers import NoteSerializer
from .utils import *

# Create your views here.

@api_view(['GET'])
def initial(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(["GET", "POST"])
def get_notes(request):
    if request.method == 'GET':
        return getNotesList(request)
    elif request.method == "POST":
        return createNote(request)

@api_view(['GET', 'PUT', 'DELETE'])
def get_note(request, pk):
    if request.method == 'GET':
        return getNoteDetail(request, pk)
    elif request.method == 'PUT':
        return updateNoteText(request, pk)
    elif request.method == 'DELETE':
        return deleteNote(request, pk)