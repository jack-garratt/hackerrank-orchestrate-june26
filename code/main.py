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
            
            print(f"User ID: {user_id}")
            print(f"Image Paths: {image_paths}")
            print(f"Claim: {user_claim}")
            print(f"Claim Object: {claim_object}")
            # You can access other variables here as needed
        else:
            print("No records found in CSV.")

if __name__ == "__main__":
    process_first_claim()
