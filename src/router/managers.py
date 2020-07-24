''' Handles manager routes. Only login for now '''
import json
from flask_restplus import Resource, Api, Model
import src.data.managers_db as manage_db
from src.logging.logger import get_logger

_log = get_logger(__name__)

api = Api()

@api.route('/managers/<str:manager_id>')
@api.doc()
class ManagerRoute(Resource):
    '''Class for routing manager requests'''
    @api.response(200, 'Test success')
    # making it a post so in the future, it will accept a password in the body
    # @api.expect(password)
    def post(self, manager_id):
        '''Function for handling POST /manager requests'''
        return json.loads(json.dumps(manage_db.manager_login(manager_id)))
