import pytest
from library.books.models import *

@pytest.mark.django_db
@pytest.mark.parametrize(
    'nombre, apellido',
    (
        ('Paulo', 'Coelho'),
        ('Haruki', 'Murakami'),
        ('Rey', 'Julien')
    )
)
def test_author_name():
    author = Author.objects.create(name=nombre, last_name=apellido)
    print('this is my authors name:', author.name)
    assert author.last_name == 'Coelho'
    assert Author.objects.all().count() == 1
    author.delete()
    assert Author.objects.all().count() == 0
