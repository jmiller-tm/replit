"""
Smart Contract advanced test scenario
"""
display_name = 'Scenario 1'
api = '3.0.0'
version = '0.0.1'
tside = Tside.LIABILITY

parameters = [
    Parameter(
        name='denomination',
        shape=DenominationShape,
        level=Level.TEMPLATE,
        description='Default denomination.',
        display_name='Default denomination for the contract.',
    )
]

@requires(parameters=True)
def pre_posting_code(postings, effective_date):
    wrong = vault.get_parameter_timeseries(name='denomination').latest()
    if any(post.denomination != denomination for post in postings):
        raise Rejected(
            'Cannot make transactions in given denomination; '
            'transactions must be in {}'.format(denomination),
            reason_code=RejectedReason.WRONG_DENOMINATION,
        )