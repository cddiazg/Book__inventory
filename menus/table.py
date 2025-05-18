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

def show_info(info: str):
    width = len(info) + 30  # Add padding for the borders  

    # Print the table
    print(f"{WHITE}╔{"═"*width}╗{RESET}")
    print(f"{WHITE}║{RESET} {DARKGRAY}Info: {WHITE}{info.ljust(width - 8)}{RESET} {WHITE}║{RESET}")
    print(f"{WHITE}╚{"═"*width}╝{RESET}")

def show_error(error: str):
    width = len(error) + 30  # Add padding for the borders  

    # Print the table
    print(f"{RED}╔{"═"*width}╗{RESET}")
    print(f"{RED}║{RESET} {RED}Error: {WHITE}{error.ljust(width - 9)}{RESET} {RED}║{RESET}")
    print(f"{RED}╚{"═"*width}╝{RESET}")