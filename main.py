from menus import table

from utils.validations import to_valid_int
# from books.add_books import add_book

def menu_actions(action: int):
  match action:
    case 1:
      pass
    case 2:
      pass
    case 3:
      pass
    case 4:
      pass
    case 5:
      pass
    case _:
      table.show_error("Opción no válida")

def start():
  # First menu
  title = "Inventario de libros"
  exit = ["Salir"]
  main_options = ["Agregar libro", "Eliminar libro", "Buscar libro", "Modificar libro", "Mostrar libros"] + exit
  # table.show_table(title, options)
  # table.show_error("No se pudo cargar el inventario")
  flag = True
  while flag:
    table.show_menu(main_options, title)
    opt = to_valid_int(input("Selecciona una opción: "))
    if opt == None:
      print("Opción no válida")
      continue
    
    if opt == main_options.index("Salir") + 1:
      print("Saliendo...")
      break
    
    menu_actions(opt)
  
if __name__ == "__main__":
  start()