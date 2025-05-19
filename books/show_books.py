from menus import table as tbl

def show_all_books(books: list):
    if not books or len(books) == 0:
      tbl.show_info("No hay libros para mostrar.")
      return
    
    tbl.show_books_in_table(books, "Listado general de libros")