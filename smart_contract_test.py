import os
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from decimal import Decimal
from json import dumps as json_dumps
from collections import defaultdict
from unittest.mock import call, Mock

from common.test_utils.contracts.unit import run
from common.test_utils.contracts.unit.common import (
    ContractTest,
    balance_dimensions,
    mock_client_transaction,
)
from common.test_utils.contracts.unit.types_extension import (
    DEFAULT_ADDRESS,
    DEFAULT_ASSET,
    Phase,
    Balance,
    Rejected,
    Tside,
    RejectedReason,
    UnionItemValue,
    NumberShape,
    Parameter,
    InvalidContractParameter,
    OptionalValue,
    OptionalShape,
)

CONTRACT_FILE = os.environ['contract_file']
UTILS_MODULE_FILE = 'utils.py'
INTEREST_MODULE_FILE = 'interest.py'

DEFAULT_DENOMINATION = "GBP"
DEFAULT_DATE = datetime(2019, 1, 1)
ADDITIONAL_DENOMINATIONS = json_dumps(["USD", "EUR"])
ACCRUED_INCOMING = "ACCRUED_INCOMING"
ACCRUED_OUTGOING = "ACCRUED_OUTGOING"

def balances_for_sc(
    dt=DEFAULT_DATE,
    default_balance=Decimal("0"),
    accrued_deposit_payable=Decimal("0"),
    accrued_deposit_receivable=Decimal("0"),
    accrued_overdraft_fee_receivable=Decimal("0"),
    accrued_incoming=Decimal("0"),
    accrued_outgoing=Decimal("0"),
):

    balance_dict = defaultdict(lambda: Balance(net=Decimal("0")))
    balance_dict[balance_dimensions(denomination=DEFAULT_DENOMINATION)] = Balance(
        net=default_balance
    )
    balance_dict[
        balance_dimensions(denomination=DEFAULT_DENOMINATION, address=ACCRUED_OUTGOING)
    ] = Balance(net=accrued_outgoing)
    balance_dict[
        balance_dimensions(denomination=DEFAULT_DENOMINATION, address=ACCRUED_INCOMING)
    ] = Balance(net=accrued_incoming)
    balance_dict[
        balance_dimensions(denomination=DEFAULT_DENOMINATION, phase=Phase.COMMITTED)
    ] = Balance(net=default_balance)
    balance_dict[
        balance_dimensions(denomination=DEFAULT_DENOMINATION, address=DEFAULT_ADDRESS)
    ] = Balance(net=default_balance)
    return [(dt, balance_dict)]

class SCTest(ContractTest):
    contract_file = CONTRACT_FILE
    side = Tside.LIABILITY
    linked_contract_modules = {
        "utils": {
            "path": UTILS_MODULE_FILE,
        },
        "interest": {"path": INTEREST_MODULE_FILE},
    }

    def create_mock(
        self,
        balance_ts=None,
        postings=None,
        creation_date=DEFAULT_DATE,
        client_transaction=None,
        denomination=DEFAULT_DENOMINATION,
        additional_denominations=ADDITIONAL_DENOMINATIONS,
        flags=None,):

        params = {
            key: {"value": value}
            for key, value in locals().items()
            if key not in self.locals_to_ignore
        }
        parameter_ts = self.param_map_to_timeseries(params, creation_date)

        balance_ts = balance_ts or []
        postings = postings or []
        creation_date = DEFAULT_DATE
        client_transaction = client_transaction or {}
        flags = flags or []

        return super().create_mock(
            balance_ts=balance_ts,
            parameter_ts=parameter_ts,
            postings=postings,
            creation_date=creation_date,
            client_transaction=client_transaction,
            flags=flags,
        )

    def test_pre_posting_code_rejects_postings_in_wrong_denomination(self):
        effective_time = datetime(2019, 1, 1)
        default_balance = Decimal("2000")
        test_postings = self.mock_posting_instruction_batch(
            denomination="HKD",
            posting_instructions=[self.mock_posting_instruction(denomination="HKD")],
        )
        balance_ts = balances_for_sc(effective_time, default_balance=default_balance)

        mock_vault = self.create_mock(
            balance_ts=balance_ts,
            denomination="GBP",
            additional_denominations=ADDITIONAL_DENOMINATIONS,
        )

        with self.assertRaises(Rejected) as e:
            self.run_function(
                "pre_posting_code", mock_vault, test_postings, effective_time
            )

        self.assertEqual(e.exception.reason_code, RejectedReason.WRONG_DENOMINATION)