''' Handles category routes '''

from flask_restplus import Resource, Api

api = Api()

@api.route('/categories')
@api.doc()
class CategoryRoute(Resource):
    '''Class for routing category requests'''
    @api.response(200, 'Success')
    def get(self):
        '''Function for handling GET /categories requests'''
        return ['Category 1', 'Category 2', 'Category 3']
