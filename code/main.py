import csv
import os
from claim import Claim
from user_history import UserHistory

def load_user_history(history_path="dataset/user_history.csv"):
    history_map = {}
    with open(history_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            history_map[row['user_id']] = UserHistory(**row)
    return history_map

def process_all_claims(csv_path="dataset/sample_claims.csv"):
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        return []

    # Load history first
    history_map = load_user_history()
    
    claims = []
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Get history for this user
            user_history = history_map.get(row['user_id'])
            
            # Create a Claim instance
            claim = Claim(
                user_id=row['user_id'],
                image_paths=row['image_paths'].split(";"),
                user_claim=row['user_claim'],
                claim_object=row['claim_object'],
                previous_claims_context=user_history
            )
            claims.append(claim)
            print(f"Created: {claim}")
            
    return claims

if __name__ == "__main__":
    process_all_claims()
