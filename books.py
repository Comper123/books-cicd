import json
import argparse


def load_books(filename):
    file = open(filename, "r", encoding="utf-8")
    books = json.load(file)
    file.close()
    return books


def search_books(books, author):
    result = []

    for book in books:
        if author in book["author"]:
            result.append(book)

    return result


def main():
    parser = argparse.ArgumentParser(description="Поиск книг")
    parser.add_argument("filename", help="Файл с книгами")
    parser.add_argument("--author", required=True, help="Автор книги")
    args = parser.parse_args()

    books = load_books(args.filename)
    found_books = search_books(books, args.author)

    for book in found_books:
        print(book["title"], "-", book["author"])


if __name__ == "__main__":
    main()