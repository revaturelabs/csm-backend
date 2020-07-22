''' Handles batch routes '''

from flask_restplus import Resource, Api
from src.logging.logger import get_logger

_log = get_logger(__name__)

api = Api()

@api.route('/batches')
@api.doc()
class BatchRoute(Resource):
    '''Class for routing batch requests'''
    @api.response(200, 'Test success')
    def get(self):
        '''Function for handling GET /batches requests'''
        return {'status': "yippee"}
    ''' would like to potentially return an array
    each batch have their id
    have an array of associates: '''