class Book:
    def __init__(self, title, isbn):
        self._title = None
        self._isbn = None
        self.title = title
        self.isbn = isbn

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise RuntimeError("Title must not be empty.")
        self._title = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        original = value
        value = value.replace("-", "").replace(" ", "")  # Remove hyphens and spaces
        if len(value) != 13:
            raise RuntimeError("ISBN must be a 13-digit number.")
        
        # Validate checksum
        modified_digits = []
        for i, digit in enumerate(value):
            digit_value = int(digit)
            if i % 2 == 0:
                modified_digits.append(digit_value)
            else:
                modified_digits.append(digit_value * 3)
        
        if sum(modified_digits) % 10 != 0:
            raise RuntimeError("Invalid ISBN.")
        
        self._isbn = original
     
#book = Book('Watchmen', '978-1779501127')