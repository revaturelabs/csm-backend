''' This files will provide the model for a Manager object '''

class Manager():
    ''' This is the class '''
    def __init__(self, username='', email=''):
        self.username = username
        self.email = email
    def set_username(self, username):
        ''' Setter for the username field'''
        self.username = username
    def get_username(self):
        ''' Getter for the username field'''
        return self.username
    def set_email(self, email):
        ''' Setter for the email field'''
        self.email = email
    def get_email(self):
        ''' Getter for the email field'''
        return self.email
    def to_dict(self):
        ''' Returns a dictionary representation of itself'''
        dict_rep = self.__dict__
        return dict_rep
    @classmethod
    def from_dict(cls, input_dict):
        ''' Creates an instance of the set given a dictionary representation of the set'''
        new_manager = cls()
        new_manager.__dict__.update(input_dict)
        return new_manager