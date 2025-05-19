def search_author(books, author):
    search_author = None

    if len(author.replace(" ", ""))== 0:
        print("Error debes especificar un author para buscar")
        return search_author
    
    for book in books:
        if author.lower() == book["author"].lower() :
                return book["title"]

    print(f"Error author no encontrado: {author}")
    return search_author    

books = [
    { 
    "id" : 1,
    "title" : 'Cien años de soledad',
    "author" : 'Gabriel garcia marquez',
    "publication_year" : 2024,
    "category" : 'no ficcion',
    "status" : 'borrowed',
    "loan" : {"nombre": 'Daniel',"fecha_prestamo" : '2025-05-16'} 
    },
    { 
    "id" : 2,
    "title" : 'docientos años de soledad',
    "author" : 'Gabriel garcia marquez',
    "publication_year" : 2023   ,
    "category" : 'no ficcion',
    "status" : 'borrowed',
    "loan" : {"nombre": 'Daniel',"fecha_prestamo" : '2025-05-16'} 
    }
]


print(search_author(books, "gabriel garcia marquez"))