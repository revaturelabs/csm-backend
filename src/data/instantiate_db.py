''' File to instantiate the database with test data. '''
from src.data.data import DatabaseConnection
from src.data.associates_db import create_associate
from src.data.swot_db import create_swot

from src.models.associates import Associate
from src.models.swot import SWOT

from src.logging.logger import get_logger

DB = DatabaseConnection()
_log = get_logger(__name__)

if __name__ == "__main__":
    DB.get_associates_collection().drop()
    DB.get_swot_collection().drop()

    DB.get_associates_collection().insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})
    DB.get_swot_collection().insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})

    new_associate = Associate(sf_id="SF-8507",
                              email="mock12.associate1b4ee47b-6d18-4c5f-bada-808f1eaf469d@mock.com",
                              batch_id="TR-1649",
                              manager_id="manager",
                              end_date="2020-05-13")
    new_associate.__dict__['_id'] = 'testId'
    Associate.from_dict(new_associate.__dict__)
    create_associate(new_associate)

    # manager_list = []
    # manager_list.append({'username': 'Julie', '_id': 'julie@revature.com'})
    # manager_list.append({'username': 'Emily', '_id': 'emily@revature.com'})
    # _managers.insert_many(manager_list)

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
