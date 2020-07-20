''' File to instantiate the database with test data. '''
from src.data.associates_db import _associates, create_associate
from src.data.swot_db import create_swot
from src.data.data import _db

from src.models.associates import Associate
from src.models.swot import SWOT

from src.logging.logger import get_logger

_log = get_logger(__name__)

_managers = _db['managers']

if __name__ == "__main__":
    _associates.drop()
    new_associate = Associate(sf_id="SF-8507",
                              email="mock12.associate1b4ee47b-6d18-4c5f-bada-808f1eaf469d@mock.com",
                              manager_id="manager",
                              end_date="2020-05-13")
    new_associate.__dict__['_id'] = 'testId'
    Associate.from_dict(new_associate.__dict__)
    create_associate(new_associate)

    _managers.drop()
    manager_list = []
    manager_list.append({'username': 'Julie', 'email': 'julie@revature.com'})
    manager_list.append({'username': 'Emily', 'email': 'emily@revature.com'})
    _db.managers.insert_many(manager_list)

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
