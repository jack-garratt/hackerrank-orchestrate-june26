import csv
import os

def process_all_claims(csv_path="dataset/sample_claims.csv"):
    """Reads all records from the CSV and processes each one."""
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        return

    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            user_id = row['user_id']
            image_paths = row['image_paths'].split(';')
            user_claim = row['user_claim']
            claim_object = row["claim_object"]

            
            print(f"--- Processing User: {user_id} ---")
            print(f"Image Paths: {image_paths}")
            print(f"Claim: {user_claim}")
            print(f"Claim Object: {claim_object}") 
            # You can add further processing logic here

if __name__ == "__main__":
    process_all_claims()
