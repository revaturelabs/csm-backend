''' File to instantiate the database with test data. '''
<<<<<<< HEAD:src/data/instation_db.py
import datetime

from src.data.data import _db
from src.data.associates_db import _associates, create_associate
from src.data.swot_db import _swot, create_swot
=======
from src.data.data import DatabaseConnection
from src.data.associates_db import create_associate
from src.data.swot_db import create_swot
>>>>>>> 1dacb4003024fc52d1539a1405c83bd10a327e20:src/data/instantiate_db.py

from src.models.associates import Associate
from src.models.swot import SWOT

from src.logging.logger import get_logger

DB = DatabaseConnection()
_log = get_logger(__name__)

if __name__ == "__main__":
    DB.get_associates_collection().drop()
    DB.get_swot_collection().drop()

<<<<<<< HEAD:src/data/instation_db.py

    _associates.create_index('salesforce_id', unique=True)
    _associates.create_index('email', unique=True)

    _swot.insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})
    _associates.insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})
=======
    DB.get_associates_collection().insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})
    DB.get_swot_collection().insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})
>>>>>>> 1dacb4003024fc52d1539a1405c83bd10a327e20:src/data/instantiate_db.py


    new_associate = Associate(sf_id="SF-8507",
                              name="Mock 111 Tester 111",
                              email="mock12.associate1b4ee47b-6d18-4c5f-bada-808f1eaf469d@mock.com",
<<<<<<< HEAD:src/data/instation_db.py
                              batch_id="TT 1111",
=======
                              batch_id="TR-1649",
>>>>>>> 1dacb4003024fc52d1539a1405c83bd10a327e20:src/data/instantiate_db.py
                              manager_id="manager",
                              trainers=['Trainer Names Here'],
                              end_date=datetime.datetime.today())
    new_associate.__dict__['_id'] = 0
    Associate.from_dict(new_associate.__dict__)
    create_associate(new_associate)
    new_swot = SWOT()
    _log.debug(new_swot)
    new_swot.add_swot_item('strengths', 'strengths test')
    new_swot.add_swot_item('strengths', 'strengths test 2')
    new_swot.add_swot_item('weaknesses', 'weaknesses test')
    new_swot.add_swot_item('weaknesses', 'weaknesses test 2')
    new_swot.add_swot_item('opportunities', 'opportunities test')
    new_swot.add_swot_item('opportunities', 'opportunities test 2')
    new_swot.add_swot_item('threats', 'threats test')
    new_swot.add_swot_item('threats', 'threats test 2')
    create_swot('salesforce_id', 'SF-8507', new_swot.__dict__)
