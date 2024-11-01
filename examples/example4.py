# Пример лямбда-функции
def book_list(books, function):
    for book in books:
        print(function(book))

books = ['Tom Sawyer', 'The Little Prince', 'Romeo and Juliet']

book_list(books, lambda book: book.swapcase() + ' - прочитано')