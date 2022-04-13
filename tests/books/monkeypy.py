from http import client
import pytest
from library.books.models import *

@pytest.mark.django_db
def test_author_with_monkey(monkeypatch):
    author = Author.objects.create(name='nombre', last_name='apellido')



def model_count_mock():
    return 4

print(dir(Author.objects))
print(dir(Author.objects))
print(type(Author.objects.all()))
monkeypatch.setattr(Author.objects, 'count', model_count_mock)

assert Author.objects.count() == 4
print('Haciendo el monkeypatch')