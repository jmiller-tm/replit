import vault_caller
from datetime import datetime, timezone
from decimal import Decimal
import os
import unittest
core_api_url = 'https://core-api-demo.atlantics.tmachine.io'
auth_token = 'A0008077239444320292579!JFu/xVxOgiGfwOkYX4Bbk3Z789qDTbwgYCQYFEz37R8Rt4DF0AIrqB/batilz1UOB+MF3SktonV+yvVx3xDpZ4FtBos='
CONTRACT_FILE = './tutorial_contract.py'
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
    def test_unchallenged_deposit(self):
        start = datetime(year=2019, month=1, day=1, tzinfo=timezone.utc)
        end = datetime(year=2019, month=1, day=2, tzinfo=timezone.utc)
        template_params = {}
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
    def test_wrong_denomination_deposit(self):
        start = datetime(year=2019, month=1, day=1, tzinfo=timezone.utc)
        end = datetime(year=2019, month=1, day=2, tzinfo=timezone.utc)
        template_params = {}
        instance_params = {}
        deposit_event = {
            "posting_instruction_batch": {
                "client_id": "Visa",
                "client_batch_id": "123",
                "posting_instructions": [{
                    "inbound_hard_settlement": {"amount": "1000", "denomination": "EUR",
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
        # No valid postings were made
        self.assertEqual(len(res.get('postings_batches')), 0)
        # The event log contains the error we expect to be raised by an invalid currency
        self.assertIn('Cannot make transactions in given denomination; transactions must be in GBP',
                      res['event_log_json'])
    def test_wrong_denomination_with_parameter_deposit(self):
        start = datetime(year=2019, month=1, day=1, tzinfo=timezone.utc)
        end = datetime(year=2019, month=1, day=2, tzinfo=timezone.utc)
        template_params = {'denomination': 'GBP'}
        instance_params = {}
        deposit_event = {
            "posting_instruction_batch": {
                "client_id": "Visa",
                "client_batch_id": "123",
                "posting_instructions": [{
                    "inbound_hard_settlement": {"amount": "1000", "denomination": "EUR",
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
        # No valid postings were made
        self.assertEqual(len(res.get('postings_batches')), 0)
        # The event log contains the error we expect to be raised by an invalid currency
        self.assertIn('Cannot make transactions in given denomination; transactions must be in GBP',
                      res['event_log_json'])
    def test_fee_applied_after_withdrawal(self):
        start = datetime(year=2019, month=1, day=1, tzinfo=timezone.utc)
        end = datetime(year=2019, month=1, day=2, tzinfo=timezone.utc)
        template_params = {
            'denomination': 'GBP',
            'overdraft_limit': '100',
            'overdraft_fee': '20'
        }
        instance_params = {}
        withdrawal_event = {
            "posting_instruction_batch": {
                "client_id": "Visa",
                "client_batch_id": "123",
                "posting_instructions": [{
                    "outbound_hard_settlement": {"amount": "110", "denomination": "GBP",
                                                "target_account_id": "Main account"},
                    "client_transaction_id": "123456",
                    "pics": [],
                    "instruction_details": {"description": "test2"},
                }],
                "batch_details": {"description": "test"},
                "value_timestamp": "2019-01-01T01:00:00+00:00"
            }
        }
        events = [vault_caller.SimulationEvent(start, withdrawal_event)]
        res = self.client.simulate_smart_contract(contract_code=self.smart_contract_contents,
                                                  start_timestamp=start, end_timestamp=end,
                                                  template_parameters=template_params,
                                                  instance_parameters=instance_params,
                                                  return_event_log=True,
                                                  events=events)
        self.assertEqual(res['v3_balance_timeseries'][0]['amount'], '-110.0')
        self.assertEqual(res['v3_balance_timeseries'][1]['amount'], '-130.0')
    def test_execution_schedule(self):
        start = datetime(year=2019, month=1, day=1, tzinfo=timezone.utc)
        end = datetime(year=2019, month=1, day=2, tzinfo=timezone.utc)
        template_params = {
            'denomination': 'GBP',
            'overdraft_limit': '100',
            'overdraft_fee': '20',
            'gross_interest_rate': '0.08'
        }
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
        # There will be two balances because we now have an interest accrual
        self.assertEqual(len(res.get('v3_balance_timeseries')), 2)
        self.assertEqual(res['v3_balance_timeseries'][-1]['account_address'], 'ACCRUED_INCOMING')
        self.assertEqual(
            Decimal(res['v3_balance_timeseries'][-1]['amount']).quantize(Decimal('.00001')),
            Decimal('0.21918')
        )
    def test_improved_execution_schedule(self):
        start = datetime(year=2019, month=1, day=1, tzinfo=timezone.utc)
        end = datetime(year=2019, month=1, day=5, hour=1, tzinfo=timezone.utc)
        template_params = {
            'denomination': 'GBP',
            'overdraft_limit': '100',
            'overdraft_fee': '20',
            'gross_interest_rate': '0.08',
        }
        instance_params = {'interest_payment_day': '5'}
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
        # There will be two balances because we now have an interest accrual
        self.assertEqual(
            res['postings_batches'][-1]['posting_instructions'][0]['custom_instruction']['postings'][0]['amount'],
            '0.88')
        self.assertEqual(res['postings_batches'][-1]['posting_instructions'][0]['instruction_details']['event'],
                         'APPLY_ACCRUED_INTEREST')
if __name__ == '__main__':
    unittest.main()

# flake8: noqa