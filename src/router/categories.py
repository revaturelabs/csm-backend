''' Handles category routes '''

from flask_restplus import Resource, Api
import src.data as db

api = Api()

@api.route('/categories')
@api.doc()
class CategoryRoute(Resource):
    
    @api.response(200, 'Test success')
    def get(self):
            return 'Category info here'