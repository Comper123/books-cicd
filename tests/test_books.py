import unittest

from books import search_books


class TestBooks(unittest.TestCase):
    def setUp(self):
        self.books = [
            {"title": "Капитанская дочка", "author": "Александр Пушкин"},
            {"title": "Евгений Онегин", "author": "Александр Пушкин"},
            {"title": "Война и мир", "author": "Лев Толстой"}
        ]
    
    def test_author_search_ignores_case(self):
        result = search_books(self.books, "пушкин")
        self.assertEqual(len(result), 2)

    def test_exact_author(self):
        result = search_books(self.books, "Лев Толстой")
        self.assertEqual(len(result), 1)

    def test_partial_author(self):
        result = search_books(self.books, "Толст")
        self.assertEqual(len(result), 1)

    def test_unknown_author(self):
        result = search_books(self.books, "Чехов")
        self.assertEqual(len(result), 0)

    def test_empty_list(self):
        result = search_books([], "Пушкин")
        self.assertEqual(result, [])

    def test_two_books_found(self):
        result = search_books(self.books, "Александр")
        self.assertEqual(len(result), 2)

    def test_found_book_title(self):
        result = search_books(self.books, "Толстой")
        self.assertEqual(result[0]["title"], "Война и мир")

    def test_uppercase_query(self):
        result = search_books(self.books, "ПУШКИН")
        self.assertEqual(len(result), 2)

    def test_lowercase_author_in_data(self):
        books = [{"title": "Книга", "author": "иван иванов"}]
        result = search_books(books, "ИВАНОВ")
        self.assertEqual(len(result), 1)

    def test_other_books_not_returned(self):
        result = search_books(self.books, "Толстой")
        self.assertNotEqual(result[0]["author"], "Александр Пушкин")
        
        
if __name__ == "__main__":
    unittest.main()