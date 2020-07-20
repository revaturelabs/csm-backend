''' This files provides the model for the Batch class '''


class Batch():
    ''' Associate class describing behaviors and attributes of Batches '''
    def __init__(self, _id=-1, batch_id=0, associates=[]):
        self._id = _id
        self.batch_id = batch_id
        self.associates = associates


    def get_batch_id(self, batch_id):
        '''Returns the batch id of the batch'''
        return self.batch_id

    def get_associates(self, associates):
        '''Returns the associate list of the batch'''
        return self.associates


    def set_batch_id(self, new_info):
        '''Sets the batch id of the batch'''
        self.batch_id = new_batch_id

    def set_associates(self, new_info):
        '''Returns the associate list of the batch'''
        self.associates = new_associate_list

    def to_dict(self):
        '''Creates a dict from an instance of an Batch'''
        return self.__dict__

    @classmethod
    def from_dict(cls, input_batch):
        '''Creates an instance of an batch from a dictionary input'''
        batch = Batch()
        batch.__dict__.update(input_batch)
        return batch

class BatchEncoder(json.JSONEncoder):
    ''' Allows us to serialize our objects as JSON '''
    def default(self, o):
        return o.to_dict()