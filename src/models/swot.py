''' This files will provide the model for a SWOT Analysis object '''

import datetime

class SWOT():
    ''' This is the class '''
    def __init__(self):
        '''{datetime created, category, notes}'''
        self.author = 'trainer'
        self.Strengths = []
        self.Weaknesses = []
        self.Opportunities = []
        self.Threats = []
        self.Notes = ''
        self.date_created = datetime.datetime.now().replace(microsecond=0)

    def to_dict(self):
        ''' Return a dict with a stringified date '''
        return_dict = self.__dict__
        return return_dict

    @classmethod
    def from_dict(cls, input_swot):
        '''Creates a SWOT instance from a dict'''
        swot = SWOT()
        swot.__dict__.update(input_swot)
        return swot
