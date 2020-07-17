''' Handles batch routes '''

from flask_restplus import Resource, Api
import src.data as db

api = Api()

@api.route('/batches')
@api.doc()
class BatchRoute(Resource):

    @api.response(200, 'Test success')
    def get(self):
        '''Returns all the batches from mongodb'''
        batches = db.get_batches()
        value = bytes(json.dumps(batches, cls=BatchEncoder), 'utf-8')
        return value

    def put(self):
        '''Updates batches in mongodb'''


