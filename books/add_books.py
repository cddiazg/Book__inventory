from datetime import datetime
import uuid

from menus.table import show_error, show_info,show_sucess 

# Function to generate a unique ID for each book
def generate_id(prefix: str = "LIB-", lenght: int = 5):
    random_part =uuid.uuid4().hex[:lenght].upper()
    return f"{prefix}{random_part}"

def get_id_history(books):
    ids = set()
    for book in books:
        ids.add(book["id"])
    return ids
      
def add_book(books, title, author, year, category):     
    current_year = datetime.now().year
    if year < 1500 or year > current_year:
        show_error("Año inválido. Debe ser entre 1500 y", current_year)
        return []

    id_book = ""
    id_history = get_id_history(books)
    while id_book == "":
        id_book = generate_id()
        if id_book in id_history:
            id_book = ""
        
    libro = {
        "id": id_book,
        "title": title,
        "author": author,
        "pub_year": current_year,
        "category": category,
        "status" : "Disponible",
        "loan" : {}
    }
    show_sucess("Libro agregado correctamente.")
    return books + [libro]