import unicodedata
from menus.table import show_error

def search_author(books, author):
    search_author = None
    author = author.lower().strip()

    if len(author.replace(" ", "")) == 0:
        show_error("debes especificar un author para buscar")
        return search_author
    # Autor sin tildes
    author_normalized = unicodedata.normalize('NFKD', author).encode('ascii','ignore').decode('utf-8')

    books_author = []
    for book in books:
      book_normalized = unicodedata.normalize('NFKD', book["author"].lower()).encode('ascii', 'ignore').decode('utf-8')
      if book_normalized.find(author_normalized) != -1:
            books_author.append(book)  

    if not books_author:
        show_error(f"author no encontrado: {author}")
        return search_author

    return books_author

