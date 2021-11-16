import vault_caller
from datetime import datetime, timezone
from decimal import Decimal
import os
import unittest
core_api_url = 'https://core-api-demo.zootopia.tmachine.io'
auth_token = 'A0006289297864182782927!1ruBonOcUfg5o+8gLqEdl6uwEOEXP7QAo3qffzNnibMR470w76WOg5ek9/T1y6AwH+9M0tyxaq7QGSssY4VyBF/mQ8w='
CONTRACT_FILE = './test_contract.py'

class TutorialTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        contract = os.path.join(os.path.dirname(__file__), CONTRACT_FILE)
        if not core_api_url or not auth_token:
            raise ValueError("Please provide values for core_api_url and auth_token, these should "
                             "be provided by your system administrator.")
        with open(contract) as smart_contract_file:
            self.smart_contract_contents = smart_contract_file.read()
        self.client = vault_caller.Client(
            core_api_url=core_api_url,
            auth_token=auth_token
        )
        
    def test_instance_parameter(self):
        start = datetime(year=2019, month=1, day=1, tzinfo=timezone.utc)
        end = datetime(year=2019, month=1, day=2, tzinfo=timezone.utc)
        template_params = {'denomination': 'GBP'}
        instance_params = {}
        deposit_event = {
            "posting_instruction_batch": {
                "client_id": "Visa",
                "client_batch_id": "123",
                "posting_instructions": [{
                    "inbound_hard_settlement": {"amount": "1000", "denomination": "GBP",
                                                "target_account_id": "Main account"},
                    "client_transaction_id": "123456",
                    "pics": ["FEES"],
                    "instruction_details": {"description": "test2"},
                }],
                "batch_details": {"description": "test"},
                "value_timestamp": "2019-01-01T01:00:00+00:00"
            }
        }
        events = [vault_caller.SimulationEvent(start, deposit_event)]
        res = self.client.simulate_smart_contract(contract_code=self.smart_contract_contents,
                                                  start_timestamp=start, end_timestamp=end,
                                                  template_parameters=template_params,
                                                  instance_parameters=instance_params,
                                                  return_event_log=True,
                                                  events=events)
        self.assertEqual(len(res.get('postings_batches')), 1)

if __name__ == '__main__':
    unittest.main()

# flake8: noqa