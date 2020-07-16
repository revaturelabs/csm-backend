''' This files will provide the model for a SWOT Analysis object '''

class SWOT():
    ''' This is the class '''
    def __init__(self):
        self.strengths = None
        self.weaknesses = None
        self.opportunities = None
        self.threats = None
        self.notes = None

    def add_swot_item(self, swot_type, content):
        if swot_type in self.__dict__:
            self.__dict__[swot_type].append(content)
