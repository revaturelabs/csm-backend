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
    
    _log.debug('Mangers: %s', managers)
    _log.debug('%s', this_batch['location'])

    _log.debug(type(managers))
    julie = managers[0]
    julie['total'] =20
    # TODO:
    # Sort the Managers by their total
    managers = sorted(managers, key = lambda i: i['total'])
    print(managers)
    if len(managers) > 1:
        if mangers[0]['totals']:
            disparity = (managers[1]['totals'] - managers[0]['totals'])/managers[0]['totals']
            if disparity >= 0.2:
                #assign the batch to the manager with fewer (managers[0])
            else:
                #assign the batch to the manager based on location
    # Compare the total of each manager
    # If the disparity is higher than 20% [configurable], then assign to the manager with fewer
    # associates
    # If the disparty is less than 20%, assign based on location - This should be re-compared every
    # time
    # return manager, batchid



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
