import email
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject.settings')

from django import setup
setup()

from ModelApp.models import Person
p = Person(
  first_name = 'Taro',last_name= 'Sato',
  birthday = '2000-02-02',email='test@gmail.com',
  saraly=100000,memo='memomemo test',web_site='google.com'
)
p.save()
