from http import client
import pytest
from library.books.models import *

@pytest.mark.django_db
@pytest.mark.parametrize(
    'nombre, apellido',
    (
        ('Paulo', 'Coelho'),
        ('Haruki', 'Murakami'),
        ('Rey', 'Julien'),
    )
)
def test_author_name(nombre, apellido):
    
    author = Author.objects.create(name=nombre, last_name=apellido)
    print('this is my authors name:', author.name)
    assert author.last_name == 'Coelho'
    assert Author.objects.all().count() == 1
    author.delete()
    assert Author.objects.all().count() == 0

@pytest.mark.django_db
@pytest.mark.parametrize(
    'libro, genero',
    (
        ('HarryPotter', 'Magic'),
        ('Crepusculo', 'Drama'),
        ('LaBiblia', 'Yisus'),
    )
)

def test_book_gendre(libro, genero):
    book = BooksGenres.objects.create(name=libro, genres=genero)
    print('this is my books gendre:', book.genre)
    assert book.genres == 'Magic'
    assert Book.objects.all().count() == 1
    book.delete()


@pytest.mark.django_db
def test_book_create(book, publish_year, genres):
	book = Book.objects.create_book('book1', '1994', 'love')
	count = Book.objects.all().count()
	print(count)
	assert Book.objects.count() == 1
	user.delete()

@pytest.mark.django_db
def test_no_book():
	count = Book.objects.all().count()
	print(count)
	assert Book.objects.count() == 0

@pytest.fixture
def book_1(db):
    return Book.objects.create_book('test-book')
    
@pytest.mark.django_db
def test_set_check_price(book_1):
    book_1.set_price('new-price')
    print('my book', book_1)
    assert book_1.check_price('new-price') is True
    book_1.delete()

def test_new_book(test_new_book):
	print(new_book.name)
	assert new_book.name == 'BookName'




@pytest.mark.parametrize(
	'libro, autor',
	(
		(Twilight, Sandy),
		(Hungergames, Josepic)
		(Stranger, Camus),
		(Goodcats, Sasha)
	)
)
def test_sum(libro, autor):
	print('Books and autors:', ())
	assert book_name(libro) == 'Twilight'
    assert book_name(libro) == 'Hungergames'
    assert book_author(autor) == 'Camus'
    assert book_author(autor) == 'Sasha'
