''' Handles category routes '''

from flask_restplus import Resource, Api
from src.logging.logger import get_logger

from src.router.models import category_model

_log = get_logger(__name__)

from src.external.category_service import get_category_data

api = Api()

@api.route('/categories')
@api.doc()
class CategoryRoute(Resource):
    '''Class for routing category requests'''
    @api.response(200, 'Success', category_model)
    def get(self):
        '''Function for handling GET /categories requests'''
        return get_category_data()
