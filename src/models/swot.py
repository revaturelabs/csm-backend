''' This files will provide the model for a SWOT Analysis object '''

class SWOT():
    ''' This is the class '''
    def __init__(self):
        self.strengths = []
        self.weaknesses = []
        self.opportunities = []
        self.threats = []
        self.notes = None

    def add_swot_item(self, swot_type, content):
        if swot_type in self.__dict__:
            self.__dict__[swot_type].append(content)
            return self.from_dict(self.__dict__)
        else:
            return self

    @classmethod
    def from_dict(cls, input_swot):
        swot = SWOT()
        swot.__dict__.update(input_swot)
        return swot
