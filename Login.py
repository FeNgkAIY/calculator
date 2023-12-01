from . import Interaction
from . import MyDatabase
class Login:
    def __init__(self, database):
        self.db = MyDatabase()
        self.interaction=None

    def add_user(self, username, password):
        self.db.add_user(username, password)

    def log_in(self, username, password):
        if self.db.verify_user(username, password):
            print(f"Welcome, {username}!")
            self.interaction = Interaction(username,self.db)
            self.interaction.main()
        else:
            print("Invalid credentials")