import email
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject.settings')

from django import setup
setup()

from ModelApp.models import Person

# すべて取得
persons = Person.objects.all()
for person in persons:
  print(person.id,person,person.saraly)

# person = Person.objects.get(first_name = 'Taro')
person = Person.objects.get(pk=3)
print(person.id,person)

# filter(絞り込み、エラーにならない、複数取得可能)
print('*' * 100)
persons = Person.objects.filter(first_name = 'Taro').all()
print(persons)

for person in persons:
  print(person.id,person)