def book_lend(books, id_book):
    search_book = None

    if id_book is None or len(id_book) == 0:
        print("Error debes especificar un ID para buscar")
        return search_book
    
    for book in books:
        if id_book.lower() == book["id"].lower():
            if book["status"] == "Prestado":
                return book["loan"]
            else: 
                return {}

    print(f"Error id no encontrado: {id_book}")
    return search_book    