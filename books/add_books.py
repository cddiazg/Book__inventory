from datetime import datetime
import uuid
def add_book(books, title, author, year, category):
      
    current_year = datetime.now().year
    if year < 1500 or year > current_year:
        print("Año inválido. Debe ser entre 1500 y", current_year)
        return []

    valid_categories = ["Ficción", "No ficción", "Infantil", "Educativo"]
    if category not in valid_categories:
        print("Categoría inválida. Debe ser una de las siguientes:", valid_categories)
        return []

    libro = {
        "id": str(uuid.uuid4()),
        "title": title,
        "author": author,
        "year": year,
        "category": category,
        "status" : "Disponible",
        "loan" : {}
    }

    print("Libro agregado correctamente.")
    return books + [libro]

libros = add_book([], "Cien años de soledad", "Gabriel García Márquez", 1967, "Ficción")
libros2 = add_book(libros, "El Señor de los Anillos", "J.R.R. Tolkien", 1954, "Ficción")
print(libros)
print(libros2)

