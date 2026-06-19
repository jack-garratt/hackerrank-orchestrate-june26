class Claim:
    def __init__(self, user_id, image_paths, user_claim, claim_object, previous_claims_context=None):
        self.user_id = user_id
        self.image_paths = image_paths
        self.user_claim = user_claim
        self.claim_object = claim_object
        self.previous_claims_context = previous_claims_context

    def __repr__(self):
        return f"<Claim user_id={self.user_id} object={self.claim_object}>"
