import csv
import os

def process_first_claim(csv_path="dataset/sample_claims.csv"):
    """Reads the first record from the CSV and parses its data."""
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        return

    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        row = next(reader, None)
        
        if row:
            user_id = row['user_id']
            # Split image_paths by semicolon into a list
            image_paths = row['image_paths'].split(';')
            user_claim = row['user_claim']
            claim_object = row['claim_object']
            evidence_standard_met = row['evidence_standard_met']
            evidence_standard_met_reason = row['evidence_standard_met_reason']
            risk_flags = row['risk_flags']
            issue_type = row['issue_type']
            object_part = row['object_part']
            claim_status = row['claim_status']
            claim_status_justification = row['claim_status_justification']
            supporting_image_ids = row['supporting_image_ids']
            valid_image = row['valid_image']
            severity = row['severity']
            
            print(f"User ID: {user_id}")
            print(f"Image Paths: {image_paths}")
            print(f"Claim: {user_claim}")
            # You can access other variables here as needed
        else:
            print("No records found in CSV.")

if __name__ == "__main__":
    process_first_claim()
