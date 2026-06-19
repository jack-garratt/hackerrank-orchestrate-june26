class UserHistory:
    def __init__(self, user_id, past_claim_count, accept_claim, manual_review_claim, 
                 rejected_claim, last_90_days_claim_count, history_flags, history_summary):
        self.user_id = user_id
        self.past_claim_count = int(past_claim_count)
        self.accept_claim = int(accept_claim)
        self.manual_review_claim = int(manual_review_claim)
        self.rejected_claim = int(rejected_claim)
        self.last_90_days_claim_count = int(last_90_days_claim_count)
        self.history_flags = history_flags
        self.history_summary = history_summary
