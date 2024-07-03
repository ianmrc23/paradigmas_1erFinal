from components.frames import StoreApp
from utils.utils import db_main, file_exists

if __name__ == "__main__":
    if not file_exists("inventory.pickle"):
        db_main()

    app = StoreApp()

    app.mainloop()
