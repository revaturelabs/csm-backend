''' Handles manager routes. Only login for now '''

from flask_restplus import Resource, Api
import src.data.managers_db as manage_db

api = Api()

@api.route('/managers/<str:manager_id>')
@api.doc()
class ManagerRoute(Resource):
    '''Class for routing manager requests'''
    @api.response(200, 'Test success')
    def get(self, manager_id):
        '''Function for handling GET /manager requests'''
        return manage_db.manager_login(manager_id)
        
