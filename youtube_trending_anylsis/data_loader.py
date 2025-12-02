#data loader.py
import csv
from typing import List, Dict
#tiny helper function
def _to_int(value: str):
    try:
        return int(value)
    except Exception:
        return 0
# main function
def load_data(filepath: str) -> List[Dict[str, str]]:
    """
    Load CSV and return a list of rows as dictionaries.
    Numeric fields are converted to ints where possible.
    If file missing or unreadable, returns empty list.
    """
    rows: List[Dict[str, str]] = []
    try:
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                # Normalize keys and convert common numeric fields
                row = {k.strip(): v.strip() for k, v in r.items()}
                if 'views' in row:
                    row['views'] = _to_int(row['views'])
                if 'likes' in row:
                    row['likes'] = _to_int(row['likes'])
                if 'dislikes' in row:
                    row['dislikes'] = _to_int(row['dislikes'])
                rows.append(row)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error loading data: {e}")
    return rows


