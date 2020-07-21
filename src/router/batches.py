''' Handles batch routes '''

from flask_restplus import Resource, Api

api = Api()

@api.route('/batches')
@api.doc()
class BatchRoute(Resource):
    '''Class for routing batch requests'''
    @api.response(200, 'Test success')
    def get(self):
        '''Function for handling GET /batches requests'''
        return {'status': "yippee"}
