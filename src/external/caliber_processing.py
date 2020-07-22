'''this module is the driver that calls and processes from caliber'''

import datetime
from src.external import training_service, category_service, evaluation_service, qc_service
from src.models.associates import Associate


def get_qc_data(associate_id):
    '''this function gets qc data from caliber'''
    notes = qc_service.get_note_headers(associate_id)
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
                assocArr.append(Associate(str(temp['salesforceId']), assoc_name, str(temp['email']),
                                          str(batch_id), trainers=trainer_list, end_date=end_date))
    return assocArr


if __name__ == '__main__':
    assoc = get_new_graduates()
    print(assoc[0].to_dict())