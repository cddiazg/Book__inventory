from menus import table as tbl

def show_all_books(books: list):
    if not books or len(books) == 0:
      tbl.show_info("No hay libros para mostrar.")
      return
    
    tbl.show_books_in_table(books, "Listado general de libros")
    
def show_borrowed_books(books: list):
    if not books or len(books) == 0:
      tbl.show_info("No hay libros para mostrar.")
      return
    
    borrowed_books = [book for book in books if book['status'] == "Prestado"]
    if not borrowed_books or len(borrowed_books) == 0:
      tbl.show_info("No hay libros prestados.")
      return
    
    tbl.show_books_in_table(borrowed_books, "Listado de libros prestados")
    
def show_available_books(books: list):
    if not books or len(books) == 0:
      tbl.show_info("No hay libros para mostrar.")
      return
    
    available_books = [book for book in books if book['status'] == "Disponible"]
    if not available_books or len(available_books) == 0:
      tbl.show_info("No hay libros disponibles.")
      return
    
    tbl.show_books_in_table(available_books, "Listado de libros disponibles")