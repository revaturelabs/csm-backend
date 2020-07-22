''' Handles category routes '''

from flask_restplus import Resource, Api

from src.external.category_service import get_category_data

api = Api()

@api.route('/categories')
@api.doc()
class CategoryRoute(Resource):
    '''Class for routing category requests'''
    @api.response(200, 'Success')
    def get(self):
        '''Function for handling GET /categories requests'''
        return get_category_data()
