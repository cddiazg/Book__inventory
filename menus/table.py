from rich.console import Console
from rich.table import Table

# Ansi colors for terminal output
WHITE = "\033[97m"
DARKCYAN = "\033[36m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
DARKGRAY = "\033[90m"
RED = "\033[91m"
RESET = "\033[0m"

# Function to display a table with a title and options
def show_menu(options: list, title: str):
    # Get the maximum width of the options
    all_options = options + [title]
    # Calculate the total width of the table
    max_width = max([len(opt) for opt in all_options])
    width = max_width + 4  # Add padding for the borders

    # Print the table
    print(f"{BLUE}╔{"═"*width}╗{RESET}")
    print(f"{BLUE}║{RESET} {DARKCYAN}{title.center(width - 2)}{RESET} {BLUE}║{RESET}")
    print(f"{BLUE}╠{"═"*width}╣{RESET}")
    for i, option in enumerate(options):
        print(f"{BLUE}║{RESET} {DARKCYAN}[{str(i + 1)}]{RESET} {WHITE}{option.ljust(width - 6)}{RESET} {BLUE}║{RESET}")
    print(f"{BLUE}╚{"═"*width}╝{RESET}")

# Function to display a table with book information
def show_books_in_table(books: list, table_title: str):
    if not books or len(books) == 0:
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
        title=table_title
    )
    
    for key, value in titles.items():
      if key == 'id':
        table.add_column(value, style="dark_cyan", justify="center", max_width=15)
      else:
        table.add_column(value, justify="center", max_width=20)

    for book in books:
        id_book = book.get('id') 
        if id_book == None:
            tbl.show_error(f"Error: {book} no tiene ID")
            continue
        
        title = book.get('title', '-')
        author = book.get('author', '-')
        pub_year = str(book.get('pub_year', '-'))
        category = book.get('category', '-')
        
        loan_info = book.get('loan', {})
        if loan_info == {}:
            loan_info = "-"
        else:
            name = loan_info.get('name', '-')
            loan_date = loan_info.get('loan_date', '-')
            if name != "-":
                loan_info = f"{name} ({loan_date})"
            else:
                loan_info = "-"

        status = book.get('status')
        if status == "Prestado":
            status = f"[bold red]{status}[/]"
        else:
            status = f"[bold green]{status}[/]"

        table.add_row(id_book, title, author, pub_year, category, status, loan_info)

    console.print(table)

# Function to display an information message in a table format
def show_info(info: str):
    width = len(info) + 30  # Add padding for the borders  

    # Print the table
    print(f"{WHITE}╔{"═"*width}╗{RESET}")
    print(f"{WHITE}║{RESET} {DARKGRAY}Info: {WHITE}{info.ljust(width - 8)}{RESET} {WHITE}║{RESET}")
    print(f"{WHITE}╚{"═"*width}╝{RESET}")

# Function to display an information message in a table format
def show_sucess(msg: str):
    width = len(msg) + 30  # Add padding for the borders  

    # Print the table
    print(f"{GREEN}╔{"═"*width}╗{RESET}")
    print(f"{GREEN}║{RESET} {GREEN}Info: {WHITE}{msg.ljust(width - 8)}{RESET} {GREEN}║{RESET}")
    print(f"{GREEN}╚{"═"*width}╝{RESET}")

# Function to display an error message in a table format
def show_error(error: str):
    message_error = f"{RED}Error: {WHITE}{error}{RESET}"
    width = len(message_error) # Add padding for the borders  
    # Print the table
    print(f"{RED}╔{"═"*width}╗{RESET}")
    print(f"{RED}║{RESET} {message_error.ljust(width + 12)} {RED}║{RESET}")
    print(f"{RED}╚{"═"*width}╝{RESET}")