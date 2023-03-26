class User:
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def is_authenticated(self):
        return True

    @staticmethod
    def is_active(self):
        return True
    
    @staticmethod
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.name