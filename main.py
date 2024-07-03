from components.frames import StoreApp
from schemas.file_manager import FileManager

if __name__ == "__main__":
    file_manager = FileManager()
    
    if not file_manager.file_exists("inventory.pickle"):
        categories = file_manager.read_inventory("inventory.txt")
        file_manager.save_pickle_file(categories, "inventory.pickle")
        print("\n\n[+] Inventory data has been saved as inventory.pickle")

    app = StoreApp()

    app.mainloop()
