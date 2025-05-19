from datetime import datetime
import uuid

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
        print("Año inválido. Debe ser entre 1500 y", current_year)
        return []

    valid_categories = ["Ficción", "No ficción", "Infantil", "Educativo"]
    if category not in valid_categories:
        print("Categoría inválida. Debe ser una de las siguientes:", valid_categories)
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
        "year": year,
        "category": category,
        "status" : "Disponible",
        "loan" : {}
    }

    print("Libro agregado correctamente.")
    return books + [libro]
