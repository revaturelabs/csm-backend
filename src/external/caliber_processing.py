'''this module is the driver that calls and processes from caliber'''

import datetime
import json
from src.external import training_service, category_service, evaluation_service, qc_service
from src.models.associates import Associate
import src.data.associates_db as assoc_db
from src.data.managers_db import assignment_counter, read_all_managers, manager_login
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

def preload_location_weights(batches):
    ''' This function will aggregate the incoming batches and their locations '''
    locations = {}
    current_run = datetime.datetime.today()
    next_run = current_run + datetime.timedelta(days=7)
    
    for batch in batches:
        end_date = datetime.datetime.strptime(batch['endDate'], '%Y-%m-%d')
        if current_run < end_date < next_run:
            if batch['location'] in locations.keys():
                locations[batch['location']] += len(batch['associateAssignments'])
            else:
                locations[batch['location']] = len(batch['associateAssignments'])
    
    return locations

def assignment_weight(locations, this_batch):
    ''' This function will determine which manager to assign batches on depending on the current
    number of already assigned assciates, as well as by location preference '''
    managers = read_all_managers()
    current_assignments = assignment_counter()

    for manager in managers:
        for count in current_assignments:
            if manager['_id'] == count['_id']:
                manager['total'] = count['count']
        if 'total' not in manager.keys():
            manager['total'] = 0
    
    _log.debug('%s', managers)
    _log.debug('%s', this_batch['location'])

    # TODO:
    # Sort the Managers by their total
    # Compare the total of each manager
    # If the disparity is higher than 20% [configurable], then assign to the manager with fewer
    # associates
    # If the disparty is less than 20%, assign based on location - This should be re-compared every
    # time



def get_new_graduates():
    '''associates, end date, batchid'''
    batches = training_service.batch_current()
    current_run = datetime.datetime.today()
    next_run = current_run + datetime.timedelta(days=7)
    assocArr = []
    location_weight = preload_location_weights(batches)
    _log.debug(location_weight)
    for batch in batches:
        end_date = datetime.datetime.strptime(batch['endDate'], '%Y-%m-%d')
        if current_run < end_date < next_run:
            assignment_weight(location_weight, batch)
            batch_id = batch['batchId']
            trainer_list = []
            for trainer in batch['employeeAssignments']:
                temp = trainer['employee']
                name = temp['firstName'] + ' ' + temp['lastName']
                trainer_list.append(name)
            for assoc in batch['associateAssignments']:
                temp = assoc['associate']
                assoc_name = temp['firstName'] + ' ' + temp['lastName']
                assocArr.append(Associate(str(temp['salesforceId']), assoc_name, str(temp['email']),
                                          str(batch_id), trainers=trainer_list, end_date=end_date))
    return assocArr

def get_batch_and_associate_spider_data(associate_email):
    '''gets associate spider data from an associate email'''
    query = {'email': associate_email}
    batch_id = assoc_db.get_associate_batch_id(query)
    batch_spider_data = evaluation_service.get_batch_spider_data(batch_id)
    batch_spider_data = json.loads(batch_spider_data)
    for data_dict in batch_spider_data:
        data_dict.pop('traineeId')
        data_dict.pop('weight')
    associate_spider_data = evaluation_service.get_associate_spider_data(batch_id, associate_email)
    associate_spider_data = json.loads(associate_spider_data)
    for data_dict in associate_spider_data:
        data_dict.pop('traineeId')
        data_dict.pop('weight')
    return batch_spider_data, associate_spider_data

if __name__ == '__main__':
    get_new_graduates()
