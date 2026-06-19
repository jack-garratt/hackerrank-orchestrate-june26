import os
import csv
from claim import Claim

def load_evidence_requirements(csv_path="dataset/evidence_requirements.csv"):
    """Loads evidence requirements from CSV, grouping by claim_object."""
    # Initialize dictionary with empty lists for each type
    requirements = {"car": [], "laptop": [], "package": []}
    
    if os.path.exists(csv_path):
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                obj = row['claim_object']
                if obj in requirements:
                    requirements[obj].append(row['minimum_image_evidence'])
    return requirements

def process_all_claims():
    """Placeholder for processing logic."""
    return []

if __name__ == "__main__":
    # Load requirements
    reqs = load_evidence_requirements()
    
    # Split into 3 variables
    car_reqs = reqs['car']
    laptop_reqs = reqs['laptop']
    package_reqs = reqs['package']
    
    # Process claims
    claims = process_all_claims()
    
    # Now you have the requirements ready for the AI agent integration
    print(f"Loaded {len(car_reqs)} requirements for Car.")
    print(f"Loaded {len(laptop_reqs)} requirements for Laptop.")
    print(f"Loaded {len(package_reqs)} requirements for Package.")
