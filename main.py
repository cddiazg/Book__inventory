from menus import table as tbl

from utils.validations import to_valid_int
# from books.add_books import add_book
from books.show_books import show_all_books

def menu_actions(action: int, data: list):
  match action:
    case 1:
      show_all_books(data)
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
  data = []
  
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
    
    menu_actions(opt, data)
  
if __name__ == "__main__":
  start()