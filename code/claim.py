class Claim:
    def __init__(self, user_id, image_paths, user_claim, claim_object, previous_claims_context=None):
        self.user_id = user_id
        self.image_paths = image_paths
        self.user_claim = user_claim
        self.claim_object = claim_object
        self.previous_claims_context = previous_claims_context
        self.evidence_standard_met = None
        self.evidence_standard_met_reason = None                           
        self.risk_flags = None                            
        self.issue_type = None                           
        self.object_part = None                         
        self.claim_status = None                        
        self.claim_status_justification = None            
        self.supporting_image_ids = None       
        self.valid_image = None  
        self.severity = None

    def __repr__(self):
        return f"<Claim user_id={self.user_id} object={self.claim_object}>"
