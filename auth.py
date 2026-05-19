import hashlib

class AccountLockedError(Exception):
    pass

class UserAuth:
    def __init__(self):
        self.users = {}

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username: str, password: str):
        if len(password) < 8 or not any(char.isdigit() for char in password):
            raise ValueError("Password must be at least 8 characters and contain at least one digit")
        if username in self.users:
            raise ValueError("Username already exists")
        
        self.users[username] = {
            'password_hash': self._hash_password(password),
            'attempts': 0,
            'locked': False
        }

    def login(self, username: str, password: str) -> bool:
        if username not in self.users:
            return False
            
        user_data = self.users[username]
        
        if user_data['locked']:
            raise AccountLockedError("Account is locked")
            
        if user_data['password_hash'] == self._hash_password(password):
            user_data['attempts'] = 0
            return True
        else:
            user_data['attempts'] += 1
            if user_data['attempts'] >= 4:
                user_data['locked'] = True
                raise AccountLockedError("Account is locked")
            return False

    def is_locked(self, username: str) -> bool:
        if username not in self.users:
            return False
        return self.users[username]['locked']

    def reset_attempts(self, username: str):
        if username in self.users:
            self.users[username]['attempts'] = 0
            self.users[username]['locked'] = False
