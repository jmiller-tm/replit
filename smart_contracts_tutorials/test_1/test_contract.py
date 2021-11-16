"""
Smart Contract advanced test scenario

Add a denomination parameter to the contract at the instance level
"""
display_name = 'Scenario 1'
api = '3.0.0'
version = '0.0.1'
tside = Tside.LIABILITY

# Add Parameter

@requires(parameters=True)
def pre_posting_code(postings, effective_date):
    # Access parameter timeseries
    denomination = 
    if any(post.denomination != denomination for post in postings):
        raise Rejected(
            'Cannot make transactions in given denomination; '
            'transactions must be in {}'.format(denomination),
            reason_code=RejectedReason.WRONG_DENOMINATION,
        )