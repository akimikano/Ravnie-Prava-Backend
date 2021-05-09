import os
import mutagen
from django.core.files.uploadedfile import UploadedFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE','vmeste.settings')

import django
django.setup()

from base.models import Entry
from bookkeeping.models import BookKeeping
from edu.models import EduEntry
from employment.models import EmpEntryPhoto, EmpEntryAudio, Course
from info.models import New, InfoEntry


def add_data():
    entries = Entry.objects.all()
    for e in entries:
        if e.audio_file:
            audio_info = mutagen.File(e.audio_file).info
            e.audio_duration = int(audio_info.length)
        if e.audio_file_kg:
            audio_info = mutagen.File(e.audio_file_kg).info
            e.audio_duration_kg = int(audio_info.length)
        e.save()

    entries = BookKeeping.objects.all()
    for e in entries:
        if e.audio_file:
            audio_info = mutagen.File(e.audio_file).info
            e.audio_duration = int(audio_info.length)
            e.save()
        if e.audio_file_kg:
            audio_info = mutagen.File(e.audio_file_kg).info
            e.audio_duration_kg = int(audio_info.length)
            e.save()

    entries = EduEntry.objects.all()
    for e in entries:
        if e.audio_file:
            audio_info = mutagen.File(e.audio_file).info
            e.audio_duration = int(audio_info.length)
        if e.audio_file_kg:
            audio_info = mutagen.File(e.audio_file_kg).info
            e.audio_duration_kg = int(audio_info.length)
        e.save()

    entries = EmpEntryPhoto.objects.all()
    for e in entries:
        if e.audio_file:
            audio_info = mutagen.File(e.audio_file).info
            e.audio_duration = int(audio_info.length)
        if e.audio_file_kg:
            audio_info = mutagen.File(e.audio_file_kg).info
            e.audio_duration_kg = int(audio_info.length)
        e.save()


    entries = EmpEntryAudio.objects.all()
    for e in entries:
        if e.audio_file:
            audio_info = mutagen.File(e.audio_file).info
            e.audio_duration = int(audio_info.length)
        if e.audio_file_kg:
            audio_info = mutagen.File(e.audio_file_kg).info
            e.audio_duration_kg = int(audio_info.length)
        e.save()

    
    entries = Course.objects.all()
    for e in entries:
        if e.audio_file:
            audio_info = mutagen.File(e.audio_file).info
            e.audio_duration = int(audio_info.length)
            e.save()

    
    entries = New.objects.all()
    for e in entries:
        if e.audio_file:
            audio_info = mutagen.File(e.audio_file).info
            e.audio_duration = int(audio_info.length)
        if e.audio_file_kg:
            audio_info = mutagen.File(e.audio_file_kg).info
            e.audio_duration_kg = int(audio_info.length)
        e.save()

    
    entries = InfoEntry.objects.all()
    for e in entries:
        if e.audio_file:
            audio_info = mutagen.File(e.audio_file).info
            e.audio_duration = int(audio_info.length)
        if e.audio_file_kg:
            audio_info = mutagen.File(e.audio_file_kg).info
            e.audio_duration_kg = int(audio_info.length)
        e.save()




if __name__ == "__main__":
    add_data()