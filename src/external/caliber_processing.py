'''this module is the driver that calls and processes from caliber'''

from src.external import batches_employees_associates, category_service, evaluation_service, qc_service


def get_qc_data(associate_id):
    '''this function gets qc data from caliber'''
    notes = qc_service.get_note_headers(associate_id)
    process_data = []
    for note in notes:
        content = note['content']
        score = note['technicalStatus']
        week = note['week']
        batchId = note['batchId']
        skill = qc_service.get_qc_category(batchId, week)[]
        process_data.append({})
