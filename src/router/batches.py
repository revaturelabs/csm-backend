''' Handles batch routes '''

from flask_restplus import Resource, Api

import src.external.training_service.get_all_batches

api = Api()

@api.route('/batches')
@api.doc()
class BatchRoute(Resource):
    '''Class for routing batch requests'''
    @api.response(200, 'Test success')
    def get(self):
        batches = 
        return {'status': "yippee"}
