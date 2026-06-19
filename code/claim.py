class Claim:
    def __init__(
        self,
        user_id,
        image_paths,
        user_claim,
        claim_object,
        evidence_standard_met,
        evidence_standard_met_reason,
        risk_flags,
        issue_type,
        object_part,
        claim_status,
        claim_status_justification,
        supporting_image_ids,
        valid_image,
        severity,
        previous_claims_context=None
    ):
        self.user_id = user_id
        self.image_paths = image_paths if isinstance(image_paths, list) else image_paths.split(';')
        self.user_claim = user_claim
        self.claim_object = claim_object
        self.evidence_standard_met = evidence_standard_met
        self.evidence_standard_met_reason = evidence_standard_met_reason
        self.risk_flags = risk_flags
        self.issue_type = issue_type
        self.object_part = object_part
        self.claim_status = claim_status
        self.claim_status_justification = claim_status_justification
        self.supporting_image_ids = supporting_image_ids
        self.valid_image = valid_image
        self.severity = severity
        self.previous_claims_context = previous_claims_context

    def __repr__(self):
        return f"<Claim user_id={self.user_id} status={self.claim_status}>"
