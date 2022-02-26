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
# p.save()


# class method create
# Person.objects.create(
#   first_name = 'Jiro',last_name= 'Sato',
#   birthday = '2000-02-02',email='test-jiro@gmail.com',
#   saraly=100000,memo='memomemo test',web_site='amazon.com'
# )

# get_or_create(取得 or 作成)
obj,created = Person.objects.get_or_create(
  first_name = 'Saburo',last_name= 'Sato',
  birthday = '2000-02-02',email='test-jiro@gmail.com',
  saraly=100000,memo='memomemo test',web_site='amazon.com'
)

print(obj)
print(created)