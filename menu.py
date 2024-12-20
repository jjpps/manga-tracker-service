from InquirerPy import inquirer
from utils import extract_id_from_url

def abrirMenu():
    while True:
        main_action = inquirer.select(
            message="Main menu:",
            choices=[
                "Add Manga",
                "Update All Mangas",               
                "Exit"
            ],
            vi_mode=True, 
        ).execute()
        if main_action == "Exit":
            print("Exiting...")
            break
        elif main_action == "Add Manga":
            url = inquirer.text(message="Enter the manga URL:").execute()
            manga_id = extract_id_from_url(url)
            if manga_id:
                # buscar manga por ID
                print("buscar manga por ID")
            else:
                print("Invalid URL or ID not found.")