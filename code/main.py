import csv

def count_claims(csv_path="dataset/sample_claims.csv"):
    """Counts the number of claims in the sample_claims.csv file."""
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            return sum(1 for row in reader)
    except FileNotFoundError:
        return 0

if __name__ == "__main__":
    print(f"Number of claims: {count_claims()}")
