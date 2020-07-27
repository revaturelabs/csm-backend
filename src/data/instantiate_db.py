''' File to instantiate the database with test data. '''
from src.data.data import DatabaseConnection
from src.data.associates_db import create_associates_from_scheduler


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
    manager_list.append({"_id": "emily.baillie@revature.com",
                         "username": "Emily",
                         "preferred_locations": ["New York", "Arlington", "West Virginia"],
                         "batches": []
                        })
    manager_list.append({"_id": "julie.seals@revature.com",
                         "username": "Julie",
                         "preferred_locations": ["Reston", "Tampa"],
                         "batches": []
                        })
    DB.get_managers_collection().insert_many(manager_list)

    create_associates_from_scheduler()
