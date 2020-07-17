''' Handles category routes '''

from flask_restplus import Resource, Api
import src.data as db

api = Api()

@api.route('/categories')
@api.doc()
class CategoryRoute(Resource):
    
    @api.response(200, 'Success')
    def get(self):
            return ['Category 1', 'Category 2', 'Category 3']