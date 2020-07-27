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
        self.date_created = datetime.datetime.now()

    def add_swot_item(self, swot_type, content):
        '''Adding item to swot content'''
        if swot_type in self.__dict__:
            self.__dict__[swot_type].append(content)
            return self.from_dict(self.__dict__)
        else:
            return self

    def to_dict(self):
        ''' Return a dict with a stringified date '''
        return_dict = self.__dict__
        # stringified_date = self.date_created.strftime('%Y-%m-%d')
        # return_dict['date_created'] = stringified_date
        return return_dict

    @classmethod
    def from_dict(cls, input_swot):
        '''Creates a SWOT instance from a dict'''
        swot = SWOT()
        swot.__dict__.update(input_swot)
        return swot
