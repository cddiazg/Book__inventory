from menus import table as tbl

from utils.validations import to_valid_int
from books.add_books import add_book
from books.show_books import show_all_books, show_borrowed_books, show_available_books

def menu_show_books(books: list):
  show_all_books(books)
  filters = [
    "Todos",
    "Disponible",
    "Prestado",
    "volver",
  ]
  
  opt = 0
  back = filters.index("volver") + 1
  while opt != back:
    tbl.show_menu(filters, "Opciones de filtro:")
    opt = to_valid_int(input("Selecciona una opción: "))
    if opt == None:
      tbl.show_info("Opción no válida")
      continue
    
    if opt == filters.index("Disponible") + 1:
      show_available_books(books)
    elif opt == filters.index("Prestado") + 1:
      show_borrowed_books(books)
    elif opt == filters.index("Todos") + 1:
      show_all_books(books)

def menu_actions(action: int, books: list):
  new_books = books.copy()
  match action:
    case 1:
      menu_show_books(books)
    case 2:
      pass
    case 3:
      pass
    case 4:
      pass
    case 5:
      pass
    case _:
      tbl.show_error("Opción no válida")
  return new_books

def start():
  # First menu
  title = "Inventario de libros"
  main_options = [
    "Mostrar libros",
    "Agregar libro",
    "Buscar libro",
    "Modificar libro",
    "Eliminar libro",
    "Salir"
  ]
  books = []
  
  flag = True
  while flag:
    tbl.show_menu(main_options, title)
    opt = to_valid_int(input("Selecciona una opción: "))
    if opt == None:
      tbl.show_info("Opción no válida")
      continue
    
    if opt == main_options.index("Salir") + 1:
      tbl.show_info("Saliendo...")
      flag = False
      continue
    
    books = menu_actions(opt, books)
  
if __name__ == "__main__":
  start()