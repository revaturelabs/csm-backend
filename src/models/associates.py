''' This files provides the model for the Associate class '''

import datetime

class Associate():
    ''' Associate class describing behaviors and attributes of Associates '''
<<<<<<< HEAD
    def __init__(self, sf_id='', email='', manager_id='', batch_id='', end_date=datetime.datetime.now()):
=======
    def __init__(self, sf_id='', email='', manager_id='', end_date=datetime.datetime.now()):
>>>>>>> b4e9fdab3c6b4db6e84d0778b8ce1ccc57cf1885
        self.salesforce_id = sf_id
        self.email = email
        self.manager_id = manager_id
        self.batch_id = batch_id
        self.end_date = end_date
        self.swot = None
        #Active > Benched > Deactivated
        self.status = 'Active'

    def get_salesforce_id(self):
        '''Returns the salesforce id of the associate'''
        return self.salesforce_id
<<<<<<< HEAD
        
=======

>>>>>>> b4e9fdab3c6b4db6e84d0778b8ce1ccc57cf1885
    def get_email(self):
        '''Returns the email of the associate'''
        return self.email

    def get_manager_id(self):
        '''Returns the manager_id of the associate'''
        return self.manager_id

<<<<<<< HEAD
    def get_batch_id(self):
        '''Returns the batch id of the associate'''
        return self.batch_id

=======
>>>>>>> b4e9fdab3c6b4db6e84d0778b8ce1ccc57cf1885
    def get_end_date(self):
        '''Returns the end date of the associate'''
        return self.end_date

    def get_swot(self):
        '''Returns the swot associated with the associate'''
        return self.swot

    def get_status(self):
        '''Returns the status of the associate'''
        return self.status



    def set_salesforce_id(self, new_sfid):
        '''Sets the salesforce id of the associate'''
        self.salesforce_id = new_sfid

    def set_email(self, new_email):
        '''Sets the email of the associate'''
        self.email = new_email

    def set_manager_id(self, new_mid):
        '''Sets the manager_id of the associate'''
        self.manager_id = new_mid

    def set_batch_id(self, new_batch_id):
        '''Sets the batch id of the associate'''
        self.batch_id = new_batch_id

    def set_end_date(self, new_end):
        '''Sets the end date of the associate'''
        self.end_date = new_end

    def set_swot(self, new_swot):
        '''Sets the swot associated with the associate'''
        self.swot = new_swot

    def set_status(self, new_status):
        '''Sets the status of the associate'''
        self.status = new_status



    def to_dict(self):
        '''Creates a dict from an instance of an Associate'''
        return self.__dict__

    @classmethod
    def from_dict(cls, input_associate):
        '''Creates an instance of an associate from a dictionary input'''
        associate = Associate()
        associate.__dict__.update(input_associate)
        return associate
