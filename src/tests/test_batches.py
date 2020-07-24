''' This module will contain the test suite for the batches routes '''
import unittest
import unittest.mock as mock
import werkzeug
import src.app as app
from src.router.batches import BatchRoute
import src.data.managers_db
import src.external.caliber_processing
from src.logging.logger import get_logger

_log = get_logger(__name__)

class TestRoute(unittest.TestCase):
    ''''''
    def setUp(self):
        ''' Get an instance of the server '''
        TestRoute.server = werkzeug.test.Client(app.app, werkzeug.wrappers.BaseResponse)

    # @mock.patch('src.external.caliber_processing.get_batch_info')
    # @mock.patch('src.data.managers_db.get_all_info')
    def test_batches_route_get(self):
        ''' Tests a GET request to the / batches route '''
        builder = werkzeug.test.EnvironBuilder(path='/batches', method='GET')
        with mock.patch('src.data.managers_db.get_all_info') as mock_managers:
            with mock.patch('src.external.caliber_processing.get_batch_info') as mock_batch_info:
                mock_managers.return_value = ['all managers']
                mock_batch_info.return_value = ['all batch info']

                # resp = TestRoute.server.get('/batches')
                resp = TestRoute.server.open(builder.get_environ())
                _log.debug(resp.data)

                # self.assertEqual(resp.status_code, 200)
                self.assertTrue(mock_managers.called)
                # self.assertTrue(mock_batch_info.called)
