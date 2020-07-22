'''this module is the driver that calls and processes from caliber'''

import datetime
import json
from src.external import training_service, category_service, evaluation_service, qc_service
from src.models.associates import Associate
import src.data.associates_db as assoc_db
from src.logging.logger import get_logger
_log = get_logger(__name__)


def get_qc_data(associate_id):
    '''this function gets qc data from caliber from a salesforce id'''
    notes = qc_service.get_note_headers(associate_id)
    _log.debug(qc_service.get_note_headers)
    _log.debug(notes)
    process_data = []
    for note in notes:
        content = note['content']
        score = note['technicalStatus']
        week = note['week']
        batchId = note['batchId']
        skill = qc_service.get_qc_category(batchId, week)
        process_data.append({})

def get_new_graduates():
    '''associates, end date, batchid'''
    batches = training_service.batch_current()
    b = batches[0]
    current_run = datetime.datetime.today()
    next_run = current_run + datetime.timedelta(days=7)
    assocArr = []
    for batch in batches:
        #get manager_id from weight function here, so that it is re-evaluated each batch
        end_date = datetime.datetime.strptime(batch['endDate'], '%Y-%m-%d')
        if current_run < end_date < next_run:
            batch_id = batch['batchId']
            trainer_list = []
            for trainer in b['employeeAssignments']:
                temp = trainer['employee']
                name = temp['firstName'] + ' ' + temp['lastName']
                trainer_list.append(name)
            for assoc in batch['associateAssignments']:
                temp = assoc['associate']
                assoc_name = temp['firstName'] + ' ' + temp['lastName']
                #include str(manager_id) in this append
                assocArr.append(Associate(str(temp['salesforceId']), assoc_name, str(temp['email']),
                                          str(batch_id), trainers=trainer_list, end_date=end_date))
    return assocArr


def get_spider_data(associate_email):
    '''gets associate spider data from an associate email'''
    query = {'email': associate_email}
    batch_id = assoc_db.get_associate_batch_id(query)
    spider_data = evaluation_service.get_associate_spider_data(batch_id, associate_email)
    spider_data = json.loads(spider_data)
    for data_dict in spider_data:
            data_dict.pop('traineeId')
            data_dict.pop('weight')
    _log.debug(type(spider_data))
    return spider_data
