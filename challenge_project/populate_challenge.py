import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","challenge_project.settings")

import django
django.setup()

## fake pop script
import random
from users_app.models import UserModel
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_user():
    fakeFirst = fakegen.first_name()
    fakeLast = fakegen.last_name()
    fakeemail = fakegen.email
    t = UserModel.objects.get_or_create(first_name=fakeFirst, 
                                        last_name = fakeLast, 
                                        email = fakeemail)[0]
    t.save()

    return t

def populate(N=5):
    for i in range(N):
        add_user()

if __name__ == '__main__':
    print("populating users")
    populate(20)
    print("populating complete")