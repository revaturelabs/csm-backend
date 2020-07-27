''' Handles category routes '''

from flask_restplus import Resource, Api
from src.logging.logger import get_logger
from src.external.category_service import get_category_data

from src.router.models import category_model

_log = get_logger(__name__)

api = Api()

@api.route('/categories')
class CategoryRoute(Resource):
    '''Class for routing category requests'''
    @api.response(200, 'Success', category_model)
    def get(self):
        '''Retrieves a list of categories from Caliber api'''
        return get_category_data()
