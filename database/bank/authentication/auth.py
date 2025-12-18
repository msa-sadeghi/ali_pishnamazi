from models.users import Users

class AuthManager:
    def __init__(self):
        self.user_model = Users()
        self.current_user = None

    def login(self, username, password):
        user = self.user_model.search(username)
        print("result",user)

    def log_out(self):
        self.current_user = None


