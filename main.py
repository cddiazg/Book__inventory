from books.add_books import add_book

def menu():
  print("1. Agregar libros")
  add_book("titulo", "author", "fecha")
  
menu()