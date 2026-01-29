from models.users import Users
import bcrypt
class AuthManager:
    def __init__(self):
        self.user_model = Users()
        self.current_user = None
    def login(self, username, password):
        user = self.user_model.search(username)
        if user:
            return self.verify_password(password, user[0][2])
        return False
    def hash_password(self, password):
        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed.decode()
    def verify_password(self, password, password_hashed):
        return bcrypt.checkpw(password.encode("utf-8"), password_hashed.encode("utf-8"))
    def log_out(self):
        self.current_user = None


