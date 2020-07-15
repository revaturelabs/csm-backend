''' Handles batch routes '''

from flask_restplus import Resource, Api
import src.data as db

api = Api()

@api.route('/batches')
@api.doc()
class BatchRoute(Resource):

    @api.response(200, 'Test success')
    def get(self):
        return {'status': "yippee"}
