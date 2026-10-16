
history = []
current_page = None

allowed_pages = [
    "uam.edu.ni",
    "python.org",
    "github.com",
    "josedata.com",
    "daviddata.com"
]

def visit_page(url):
    global current_page #Esta almacena la página que estamos visitando actualmente y la actualiza en todo el codigo no solo en visit

    url = url.strip().lower() #para q no lo escrriban mal

    if url not in allowed_pages:
        print("Pestaña equivocada") 
        return

    if current_page is not None: #none sirve para ayudar con los errores el usa l codigo
        history.append(current_page)

    current_page = url
    print("Current page:", current_page)

def go_back():
    global current_page

    if len(history) == 0:
        print("No existen páginas anteriores")
    else:
        current_page = history.pop()
        print("Current page:", current_page)

def show_current_page():
    if current_page is None:
        print("No page is open")
    else:
        print("Current page:", current_page)

def show_history():
    if len(history) == 0:
        print("No existen páginas anteriores")
    else:
        print("History pending to go back:")

        for page in reversed(history):
            print(page)

def show_stack():
    if len(history) == 0:
        print("Stack is empty")
    else:
        print("\n--- Navigation Stack ---")
        print("Top of stack")

        for page in reversed(history):
            print("|" + page + "|")

        print("Bottom of stack")
        print("Total elements:", len(history))

# Main menu
while True:
    print("\n--- Web Browser ---")
    print("1. Visit a new page")
    print("2. Go back")
    print("3. Show current page")
    print("4. Show navigation history")
    print("5. Show stack visualization")
    print("6. Exit")

    option = input("Select an option: ")

    if option == "1":
        print("Allowed pages:")

        for page in allowed_pages:
            print(page)

        url = input("Enter the page address: ")
        visit_page(url)

    elif option == "2":
        go_back()

    elif option == "3":
        show_current_page()

    elif option == "4":
        show_history()

    elif option == "5":
        show_stack()

    elif option == "6":
        print("Closing browser...")
        break

    else:
        print("Invalid option. Try again.")
