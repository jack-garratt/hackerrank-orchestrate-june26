import os

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
        self.verify_image_paths()

    def verify_image_paths(self):
        """Verifies that all images in image_paths exist on disk."""
        paths = self.image_paths
        
        all_exist = True
        if not paths or (len(paths) == 1 and paths[0] == ''):
            all_exist = False
            print(f"User: {self.user_id} failed in check 1")
        else:
            for path in paths:
                if not os.path.exists(f"dataset/{path}"):
                    all_exist = False
                    print(f"User: {self.user_id} failed in check 2 with path {path}")
                    break

        
        if not all_exist:
            self.evidence_standard_met = False
            self.evidence_standard_met_reason = "No image provided so unable to verifiy damage."
            self.risk_flags = []
            self.issue_type = "unknown"
            self.object_part = "unknown"
            self.claim_status = "not_enough_information"
            self.claim_status_justification = "No image provided so unable to verifiy damage."
            self.supporting_image_ids = None
            self.valid_image = False
            self.severity = "unknown"

    def __repr__(self):
        return f"<Claim user_id={self.user_id} object={self.claim_object}>"
