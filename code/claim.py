class Claim:
    def __init__(self, user_id, image_paths, user_claim, claim_object):
        self.user_id = user_id
        # Handle image_paths: split by semicolon if it's a string
        self.image_paths = image_paths.split(';') if isinstance(image_paths, str) else image_paths
        self.user_claim = user_claim
        self.claim_object = claim_object

    def __repr__(self):
        return f"<Claim user_id={self.user_id} object={self.claim_object}>"
