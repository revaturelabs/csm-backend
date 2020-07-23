''' File to instantiate the database with test data. '''
import datetime

from src.data.data import DatabaseConnection
from src.data.associates_db import create_associate, create_associates_from_scheduler
from src.data.swot_db import create_swot

from src.models.associates import Associate
from src.models.swot import SWOT

from src.logging.logger import get_logger

DB = DatabaseConnection()
_log = get_logger(__name__)

if __name__ == "__main__":
    DB.get_associates_collection().drop()
    DB.get_swot_collection().drop()
    DB.get_managers_collection().drop()

    DB.get_associates_collection().insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})
    DB.get_swot_collection().insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})

    manager_list = []
    manager_list.append({
                            "_id": "emily.baillie@revature.com",
                            "username": "Emily",
                            "preferred_locations": ["New York", "Arlington", "West Virginia"],
                            "batches": ["TR-1653"]
                        })
    manager_list.append({
                            "_id": "julie.seals@revature.com",
                            "username": "Julie",
                            "preferred_locations": ["Reston", "Tampa"],
                            "batches": ["TR-1651"]
                        })
    DB.get_managers_collection().insert_many(manager_list)

    create_associates_from_scheduler()

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
