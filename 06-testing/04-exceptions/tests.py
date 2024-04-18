import pytest
from book import Book

# Test valid book creation
@pytest.mark.parametrize("title, isbn", [
    ('Watchmen', '978-1779501127'),
    ('1984', '978-0451524935'),
    ('To Kill a Mockingbird', '978-0446310789'),
    ('The Great Gatsby', '978-0743273565'),
    ('The Catcher in the Rye', '978-0316769488'),
    ('Moby Dick', '978-1503280786'),
])
def test_valid_creation(title, isbn):
    # Create the book
    book = Book(title, isbn)
    # Assert that title and isbn are set correctly
    assert book.title == title
    assert book.isbn == isbn

# Test creation with invalid title
@pytest.mark.parametrize("isbn", [
    ('978-1779501127'),  # Empty title
    ('978-0451524935'),
    ('978-0446310789'),  # Empty title
    ('978-0743273565'),  # Empty title
    ('978-0316769488'),  # Single character title
    ('978-1503280786'),  # Empty title
])
def test_creation_with_invalid_title(isbn):
    # Check that creating the book with an invalid title raises a RuntimeError
    with pytest.raises(RuntimeError):
        Book("", isbn)

# Test creation with invalid ISBN
@pytest.mark.parametrize("title, isbn", [
    ('Watchmen', '978-1779501126'),
    ('1984', '9780735611331'),
    ('To Kill a Mockingbird', '978-04463107'),        # Invalid ISBN length
    ('The Great Gatsby', '978-07432731010101'),       # Invalid ISBN length
    ('The Catcher in the Rye', '978-03167694'),       # Invalid ISBN checksum
    ('Moby Dick', '978-15030786'),                   # Invalid ISBN length
])
def test_creation_with_invalid_isbn(title, isbn):
    # Check that creating the book with an invalid ISBN raises a RuntimeError
    with pytest.raises(RuntimeError):
        Book(title, isbn)
