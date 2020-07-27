''' Handles batch routes '''

from flask_restplus import Resource, Api
from src.data.managers_db import get_all_info, get_managers_by_batch
from src.external.caliber_processing import get_batch_info
from src.logging.logger import get_logger

from src.router.models import batch_model, associate_model_trainer, associate_model_short, \
                              trainer_info_model

_log = get_logger(__name__)

api = Api()

@api.route('/batches')
class BatchRoute(Resource):
    '''Class for routing batch requests'''
    @api.response(200, 'Success', batch_model)
    def get(self):
        ''' Function for handling GET /batches requests '''
        manager_lst = get_all_info()
        batches = []
        for manager in manager_lst:
            for batch in manager['batches']:
                batch_info = get_batch_info(batch)
                batches.append({'batchID': batch, 'batchName': batch_info['name'],
                                'skill': batch_info['skill'], 'manager': manager['username'],
                                'trainer': batch_info['trainer'],
                                'promotionDate': batch_info['promotion date'],
                                'associates': batch_info['associates']})
        return batches

@api.route('/batches/<str:batch_id>')
class BatchIndividualRoute(Resource):
    '''Class for routing batch requests'''
    @api.response(200, 'Success', batch_model)
    def get(self, batch_id):
        ''' Function for handling GET /batches/batch_id requests '''
        batch_info = get_batch_info(batch_id)
        manager = get_managers_by_batch(batch_id)
        batch = ({'batchID': batch_id, 'batchName': batch_info['name'],
                  'skill': batch_info['skill'], 'manager': manager['username'],
                  'trainer': batch_info['trainer'], 'promotionDate': batch_info['promotion date'],
                  'associates': batch_info['associates']})
        return batch
