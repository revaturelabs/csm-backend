'''this module is the driver that calls and processes from caliber'''

import datetime
from src.external import batches_employees_associates, category_service, evaluation_service, qc_service
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
    batches = batches_employees_associates.batch_current()
    print(batches)
    # current_time = datetime.today()
    assocArr = []
    for batch in batches:
        # if 
        batch_id = batch['batchId']
        for assoc in batch['associateAssignments']:
            temp = assoc['associate']
            assocArr.append(Associate(str(temp['salesforceId']), str(temp['email']), str(batch_id)))
    # for assoc in assocArr:
    #     print(assoc.get_batch_id(), assoc.get_email(), assoc.get_salesforce_id())
        
        
    # print(batches)
    # print(batches['associateAssignments'])

if __name__ == "__main__":
    get_new_graduates()