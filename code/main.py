import csv
from claim import Claim

def load_claims(csv_file_path):
    claims = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            claim = Claim(
                user_id=row['user_id'],
                image_paths=row['image_paths'],
                user_claim=row['user_claim'],
                claim_object=row['claim_object']
            )
            claims.append(claim)
    return claims

if __name__ == "__main__":
    csv_path = 'dataset/sample_claims.csv'
    claims_list = load_claims(csv_path)
    
    for claim in claims_list:
        print(claim)
