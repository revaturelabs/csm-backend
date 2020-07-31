''' Handles manager routes. Only login for now '''

from flask_restplus import Resource, Api
import src.data.managers_db as manage_db
from src.logging.logger import get_logger

_log = get_logger(__name__)

api = Api()

@api.route('/managers/<str:manager_id>')
class ManagerRoute(Resource):
    '''Class for routing manager requests'''
    @api.response(200, 'Success')
    @api.response(401, 'Unauthorized')
    # making it a post so in the future, it will accept a password in the body
    # @api.expect(password)
    def post(self, manager_id):
        ''' Login request route for manager id '''
        login_manager = manage_db.manager_login(manager_id)
        if login_manager:
            return login_manager, 200
        else:
            return {}, 401
