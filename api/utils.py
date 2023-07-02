from .models import Note
from rest_framework.response import Response
from .serializers import NoteSerializer

def getNotesList(request):
    notes = Note.objects.all().filter(body__gt=0).order_by('-last_updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

def createNote(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

def getNoteDetail(request, pk):
    note = Note.objects.get(pk=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

def updateNoteText(request, pk):
    note = Note.objects.get(pk=pk)
    serializer = NoteSerializer(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def deleteNote(request, pk):
    note = Note.objects.get(pk=pk)
    note.delete()
    return Response('Successfully deleted')