''' Handles batch routes '''

from flask_restplus import Resource, Api
from src.logging.logger import get_logger

_log = get_logger(__name__)

from src.data.managers_db import get_all_info, get_managers_by_batch
from src.external.caliber_processing import get_batch_info
from src.logging.logger import get_logger

_log = get_logger(__name__)

api = Api()

@api.route('/batches')
@api.doc()
class BatchRoute(Resource):
    '''Class for routing batch requests'''
    @api.response(200, 'Test success')
    def get(self):
<<<<<<< HEAD
        '''Function for handling GET /batches requests'''
        return {'status': "yippee"}
    ''' would like to potentially return an array
    each batch have their id
    have an array of associates:
    
// [batches//     {batch1
//         batchID,
//         manager,
//         trainer name,
//         promotion date,
//         associates [
//             {associate1
//                 name,
//                 # of swots,
//                 email,
//                 userID (if different than email. Whatever we use to look up evaluations)
//             }
//         ]
//     }
//     ...
// ]'''
=======
        ''' Function for handling GET /batches requests '''
        manager_lst = get_all_info()
        batches = []
        for manager in manager_lst:
            for batch in manager['batches']:
                batch_info = get_batch_info(batch)
                _log.debug(batch_info)
                batches.append({'batchID': batch, 'batchName': batch_info['name'],'skill': batch_info['skill'],
                                'manager': manager['username'], 'trainer': batch_info['trainer'],
                                'promotionDate': batch_info['promotion date'], 'associates': batch_info['associates']})
        return batches

@api.route('/batches/<str:batch_id>')
@api.doc()
class BatchIndividualRoute(Resource):
    '''Class for routing batch requests'''
    @api.response(200, 'Test success')
    def get(self, batch_id):
        batch_info = get_batch_info(batch_id)
        manager = get_managers_by_batch(batch_id)
        batch = ({'batchID': batch_id, 'batchName': batch_info['name'],'skill': batch_info['skill'],
                  'manager': manager['username'], 'trainer': batch_info['trainer'],
                  'promotionDate': batch_info['promotion date'], 'associates': batch_info['associates']})
        return batch
>>>>>>> fa8d6c02c938522d25d09ac11d2429d8da4a79ed
