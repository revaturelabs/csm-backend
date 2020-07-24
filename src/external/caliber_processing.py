'''this module is the driver that calls and processes from caliber'''

import datetime
import json
from src.external import training_service, category_service, evaluation_service, qc_service
from src.models.associates import Associate
import src.data.associates_db as assoc_db
import src.data.managers_db as manager_db
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

def assignment_weight(this_batch):
    ''' This function will determine which manager to assign batches on depending on the current
    number of already assigned assciates, as well as by location preference '''
    managers = manager_db.read_all_managers()
    current_assignments = manager_db.assignment_counter()

    _log.debug(current_assignments)

    for manager in managers:
        for count in current_assignments:
            if manager['_id'] == count['_id']:
                manager['total'] = count['count']
        if 'total' not in manager.keys():
            manager['total'] = 0
    
    _log.debug('Mangers: %s', managers)
    _log.debug('%s', this_batch['location'])

    _log.debug(type(managers))
    managers = sorted(managers, key = lambda i: i['total'])
    if len(managers) > 1:
        if managers[0]['total'] > 0:
            disparity = (managers[1]['total'] - managers[0]['total'])/managers[0]['total']
            if disparity >= 0.2:
                _log.debug('Assigned by disparity')
                return managers[0]['_id']
            else:
                for manager in managers:
                    if this_batch['location'] in manager['preferred_locations']:
                        _log.debug('Assigned by location')
                        _log.debug('Batch location: %s', this_batch['location'])
                        _log.debug('Manager: %s', manager['_id'])
                        return manager['_id']
        return managers[0]['_id']               

def get_batches():
    '''this function will return a list of current batches'''
    batches = training_service.batch_current()
    return batches

def get_new_graduates(batch):
    '''associates, end date, batchid'''
    current_run = datetime.datetime.today()
    next_run = current_run + datetime.timedelta(days=7)
    assocArr = []
    manager_id = assignment_weight(batch)
    end_date = datetime.datetime.strptime(batch['endDate'], '%Y-%m-%d')
    if current_run < end_date < next_run:
        batch_id = batch['batchId']
        trainer_list = []
        for trainer in batch['employeeAssignments']:
            temp = trainer['employee']
            name = temp['firstName'] + ' ' + temp['lastName']
            trainer_list.append(name)
        for assoc in batch['associateAssignments']:
            temp = assoc['associate']
            assoc_name = temp['firstName'] + ' ' + temp['lastName']
            manager_db.update_batches(manager_id, batch_id)
            assocArr.append(Associate(str(temp['salesforceId']), assoc_name, str(temp['email']),
                                        str(batch_id), str(manager_id), trainers=trainer_list, end_date=end_date))
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

def get_batch_and_associate_spider_data(associate_email, batch_id):
    '''gets associate spider data from an associate email'''
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

def get_batch_info(batch_id):
    ''' gets high level batch info from caliber'''
    batch = training_service.get_batch_by_id(batch_id)
    _log.debug(batch)
    associates = []
    for i in batch['associateAssignments']:
        temp = i['associate']
        associate = {'name': temp['firstName'] + ' ' + temp['lastName'], 'userID': temp['email']}
        associates.append(associate)
    to_return = {'trainer': batch['employeeAssignments'], 'promotion date': batch['endDate'],'name': batch['name'],'skill': batch['skill'],
                 'associates': associates}
    return to_return

if __name__ == '__main__':
    get_new_graduates()
        if note['content']:
            content = note['content']
            score = note['technicalStatus']
            week = note['week']
            batchId = note['batchId']
            skill = qc_service.get_qc_category(batchId, str(week))
            process_data.append({'skill': skill, 'score': score, 'content': content})
    return process_data
