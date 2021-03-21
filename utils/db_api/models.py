class User:
    users = dict()

    def __init__(self, telegram_id):
        self.telegram_id = telegram_id
        self.allowed = True

    @classmethod
    def get(cls, telegram_id):
        return cls.users.get(telegram_id)

    @classmethod
    def create(cls, telegram_id):
        user = User(telegram_id)
        cls.users[telegram_id] = user
        return user

    def block(self):
        self.allowed = False

    def allow(self):
        self.allowed = True
