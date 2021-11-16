# Copyright @ 2021 Thought Machine Group Limited. All rights reserved.
"""
An example that shows required Calendars being declared in a Smart Contract
"""
display_name = "Contract with Calendar declarations"
api = "3.9.0"
version = "1.0.0"
summary = "Contract with calendars"
parameters = [
    Parameter(
        name="denomination",
        shape=DenominationShape,
        level=Level.TEMPLATE,
        description="Default denomination.",
        display_name="Default denomination for the contract.",
    ),
    Parameter(
        name="interest_rate",
        shape=NumberShape(
            kind=NumberKind.PERCENTAGE, min_value=0, max_value=1, step=0.01
        ),
        level=Level.TEMPLATE,
        description="Gross Interest Reate",
        display_name="Rate paid on positive balances",
    ),
]

pnl_account = "1"


def execution_schedules():
    return [
        ("ACCRUE_INTEREST", {"hour": "00", "minute": "00", "second": "00"}),
    ]


# fmt: off
@requires(
    event_type="ACCRUE_INTEREST",
    parameters=True,
    balances="latest",
    calendar=['CALENDAR_1_REPLACED', 'CALENDAR_2_REPLACED', 'CALENDAR_3_REPLACED'],
)
def scheduled_code(event_type, effective_date):

    vault.get_calendar_events(
        calendar_ids=['CALENDAR_1_REPLACED', 'CALENDAR_2_REPLACED', 'CALENDAR_3_REPLACED']  # noqa: E501
    )

    if event_type == "ACCRUE_INTEREST":
        pass


@requires(parameters=True, balances="latest", calendar=['CALENDAR_1_REPLACED'])
def pre_posting_code():
    vault.get_calendar_events(calendar_ids=['CALENDAR_1_REPLACED'])
# fmt: on
