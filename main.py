from components.frames import StoreApp
from db.db_init import db_main
from utils.os_utils import file_exists

if __name__ == "__main__":
    if not file_exists("inventory.pickle"):
        db_main()

    app = StoreApp()

    app.mainloop()
