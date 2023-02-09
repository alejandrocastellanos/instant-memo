from django.shortcuts import render

from .models import Notes


def list_notes(request):
    notes = Notes.objects.all().order_by('create_date')
    if request.method == 'POST':
        title = request.POST['title']
        text_note = request.POST['text_note']
        color_note = request.POST['color_note']
        gallery = Notes(title=title, text_note=text_note,color_note=color_note)
        gallery.save()
    return render(request, 'notes/index.html', {'notes': notes})


def edit_note(request, id):
    if request.method == 'POST':
        Notes.objects.filter(id=id).update(title=request.POST.get('title'), text_note=request.POST.get('text_note'))
        notes = Notes.objects.all().order_by('create_date')
        return render(request, 'notes/index.html', {'notes': notes})
    notes = Notes.objects.get(id=id)
    return render(
        request,
        'notes/detail.html',
        {
            'id': notes.id,
            'text_note': notes.text_note,
            'title': notes.title,
            'save': True
        }
    )


def delete_note(request, id):
    Notes.objects.filter(id=id).delete()
    notes = Notes.objects.all().order_by('create_date')
    return render(request, 'notes/index.html', {'notes': notes})
