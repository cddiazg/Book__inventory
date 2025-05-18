from rich.console import Console
from rich.table import Table

from menus import table as tbl

def show_all_books(books: list):
    if not books or len(books) == 0:
      tbl.show_info("No hay libros para mostrar.")
      return
    
    show_books_in_table(books)

def show_books_in_table(data: list):
    if not data or len(data) == 0:
        tbl.show_error("Error: No hay datos o títulos para mostrar.")
        return
      
    titles = {
      'id': "ID Libro",
      'title': "Título",
      'author': "Autor",
      'pub_year': "Año Pub.",
      'category': "Categoría",
      'status': "Estado",
      'loan': "Préstamo"
    }
  
    console = Console()
    table = Table(
        show_header=True,
        header_style="bold deep_sky_blue3", 
        border_style="dodger_blue3",
        title="Listado general de libros"
    )
    
    for key, value in titles.items():
      if key == 'id':
        table.add_column(value, style="dark_cyan", justify="center", max_width=15)
      else:
        table.add_column(value, justify="center", max_width=20)

    for item in data:
        id_book = item.get('id') 
        if id_book == None:
            tbl.show_error(f"Error: {item} no tiene ID")
            continue
        
        title = item.get('title', '-')
        author = item.get('author', '-')
        pub_year = str(item.get('pub_year', '-'))
        category = item.get('category', '-')
        
        loan_info = item.get('loan', {})
        if loan_info == {}:
            loan_info = "-"
        else:
            name = loan_info.get('name', '-')
            loan_date = loan_info.get('loan_date', '-')
            if name != "-":
                loan_info = f"{name} ({loan_date})"
            else:
                loan_info = "-"

        status = item.get('status')
        if status == "Prestado":
            status = f"[bold red]{status}[/]"
        else:
            status = f"[bold green]{status}[/]"

        table.add_row(id_book, title, author, pub_year, category, status, loan_info)

    console.print(table)