from menus.table import show_error
def search_author(books, author):
    search_author = None

    if len(author.replace(" ", "")) == 0:
        show_error("debes especificar un author para buscar")

        return search_author
    books_author = []
    for book in books:
        if author.lower() == book["author"].lower() :
            books_author.append(book)
    if len(books_author) == 0:
        show_error(f"author no encontrado: {author}")
        return search_author        
    return books_author