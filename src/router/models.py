''' This file contains all of the models used for API documentation and validation '''
from flask_restplus import fields, Model, Api

api = Api()

''' SWOT Item model for documentation and validation '''
swot_item = Model('SWOT Item', {
    'category': fields.String,
    'notes': fields.String
})

''' SWOT model for documentation and validation '''
swot_fields = Model('SWOT', {
    'strengths': fields.List(fields.Nested(swot_item)),
    'weaknesses': fields.List(fields.Nested(swot_item)),
    'opportunities': fields.List(fields.Nested(swot_item)),
    'threats': fields.List(fields.Nested(swot_item)),
    'notes': fields.String,
    'creationDate': fields.DateTime
})

''' Associates model for documentation and validation '''
associate_model = Model('Associate', {
    'name': fields.String,
    'salesforce_id': fields.String,
    'email': fields.String,
    'batch_id': fields.String,
    'manager_id': fields.String,
    'trainers': fields.List(fields.String),
    'end_date': fields.String,
    'swot': fields.List(fields.Nested(swot_fields)),
    'status': fields.String
})

''' Short associate model used when getting a Batch '''
associate_model_short = Model('Associate (Short)', {
    'name': fields.String,
    'userID': fields.String
})

''' Trainer Personal Info used in the Trainer model '''
trainer_info_model = Model('Trainer information', {
    'email': fields.String,
    'firstName': fields.String,
    'lastName': fields.String
})

''' Trainer model used for documentation '''
associate_model_trainer = Model('Trainer', {
    "role": fields.String,
    "employee": fields.Nested(trainer_info_model),
    'deletedAt': fields.String
})

''' Category model for documentation and validation '''
category_model = Model('Category', {
    "categoryId": fields.Integer,
    "skillCategory": fields.String,
    "active": fields.Boolean
})

''' Batch model for documentation and validation '''
batch_model = Model('Batch', {
    "batchID": fields.String,
    "batchName": fields.String,
    "skill": fields.String,
    "manager": fields.String,
    "trainer": fields.List(fields.Nested(associate_model_trainer)),
    "promotionDate": fields.String,
    "associates": fields.List(fields.Nested(associate_model_short))
})

''' Associate Manager View model for documenting the associates/manager/manager_id route '''
associate_model_manager_view = Model('Associate Model (Manager View)', {
    "name": fields.String,
    "SWOT": fields.List(fields.Nested(swot_fields)),
    "ID": fields.String,
    "status": fields.String
})

''' Spider Data Model for documentation purposes '''
spider_data_model = Model('Spider Data Entry', {
    "assessmentType": fields.String,
    "score": fields.Float,
    "week": fields.Integer
})

''' QC Notes Model for documentation purposes '''
qc_note_model = Model('QC Note Model', {
    'skill': fields.String,
    'score': fields.String,
    'content': fields.String
})

''' Assocuate Evaluation model for documentation and validation purposes '''
associate_evaluation_model = Model('Associate Evaluation Model', {
    'batch_spider': fields.List(fields.Nested(spider_data_model)),
    'associate_spider': fields.List(fields.Nested(spider_data_model)),
    'qc': fields.List(fields.Nested(qc_note_model))
})

''' Manager model for documentation and validation purposes '''
manager_model = Model('Manager Model', {
    "_id": fields.String,
    "username": fields.String,
    "preferred_locations": fields.List(fields.String),
    "batches": fields.List(fields.String)
})
