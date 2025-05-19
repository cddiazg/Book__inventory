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

# books = [
#     { 
#     "id" : 1,
#     "title" : 'Cien años de soledad',
#     "author" : 'Gabriel garcia marquez',
#     "publication_year" : 2024,
#     "category" : 'no ficcion',
#     "status" : 'borrowed',
#     "loan" : {"nombre": 'Daniel',"fecha_prestamo" : '2025-05-16'} 
#     },
#     { 
#     "id" : 2,
#     "title" : 'docientos años de soledad',
#     "author" : 'Gabriel garcia marquez',
#     "publication_year" : 2023   ,
#     "category" : 'no ficcion',
#     "status" : 'borrowed',
#     "loan" : {"nombre": 'Daniel',"fecha_prestamo" : '2025-05-16'} 
#     }
# ]


# print(search_author(books, " "))