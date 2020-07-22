''' Handles batch routes '''

from flask_restplus import Resource, Api

import src.external.training_service.get_all_batches
from src.data.managers_db import get_all_info
from src.external.caliber_processing import get_batch_info

api = Api()

@api.route('/batches')
@api.doc()
class BatchRoute(Resource):
    '''Class for routing batch requests'''
    @api.response(200, 'Test success')
    def get(self):
        manager_lst = get_all_info()
        batches = []
        for manager in manager_lst:
            for batch in manager['batches']:
                batch_info = get_batch_info(batch)
                batches.append('batchID': batch, 'manager': manager['username'], 'trainer': batch_info['trainer'],
                                'promotion date': batch_info['promotion date'], 'associates': batch_info['associates'])
        return batches
