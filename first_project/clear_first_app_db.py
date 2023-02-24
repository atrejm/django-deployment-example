import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","first_project.settings")

import django
django.setup()

from first_app.models import AccessRecord, Webpage, Topic

def destroyDB():
    print("Destroying Database...")
    AccessRecord.objects.all().delete()
    Webpage.objects.all().delete()
    Topic.objects.all().delete()

if __name__ == '__main__':
    destroyDB()