import csv
from typing import List, Dict

def load_csv(filename: str) -> List[Dict]:
    with open(filename, 'r') as f:
        return list(csv.DictReader(f))

alerts = load_csv('alerts.csv')
transactions = load_csv('transactions.csv')


def get_related_transactions(alert_id):
    # TODO: Implement logic here
    alert = next((a for a in alerts if a['alert_id'] == alert_id), None)
    if not alert:
        return []
    
    transaction_ids = set(alert['primary_transaction_ids'].split(','))
    return [t for t in transactions if t['transaction_id'] in transaction_ids]


def expand_related_transactions(alert_id):
    # TODO: Implement logic here
    related_transactions = get_related_transactions(alert_id)
    entity_ids = set(t['entity_id'] for t in related_transactions)
    return [t for t in transactions if t['entity_id'] in entity_ids]


def find_related_alerts(alert_id):
    # TODO: Implement logic here
    expanded_transactions = expand_related_transactions(alert_id)
    transaction_ids = set(t['transaction_id'] for t in expanded_transactions)
    
    related_alerts = []
    for alert in alerts:
        if alert['alert_id'] == alert_id:
            continue
        alert_transaction_ids = set(alert['primary_transaction_ids'].split(','))
        if alert_transaction_ids.intersection(transaction_ids):
            related_alerts.append(alert)
    
    return related_alerts


# --- Test Cases ---
# These test cases are written to give examples of the correct responses.
# You do not need to match the input or return types as written in these
#   test cases, feel free to rewrite them as you think is appropriate.

def test_get_related_transactions():
    actual = get_related_transactions("1")
    expected = [
        {'transaction_id': '101', 'entity_id': 'E001', 'amount': '250.00', 'currency': 'USD', 'timestamp': '2024-11-18 08:45:00'},
        {'transaction_id': '103', 'entity_id': 'E001', 'amount': '400.75', 'currency': 'USD', 'timestamp': '2024-11-18 09:00:00'}
    ]
    assert actual == expected, f"Expected {expected}, but got {actual}"


def test_expand_related_transactions():
    actual = expand_related_transactions("5")
    expected = [
        {'transaction_id': '102', 'entity_id': 'E002', 'amount': '300.50', 'currency': 'USD', 'timestamp': '2024-11-18 08:50:00'},
        {'transaction_id': '105', 'entity_id': 'E002', 'amount': '150.25', 'currency': 'USD', 'timestamp': '2024-11-17 14:10:00'},
        {'transaction_id': '110', 'entity_id': 'E002', 'amount': '1000.50', 'currency': 'USD', 'timestamp': '2024-11-15 10:20:00'}
    ]
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_find_related_alerts():
    actual = find_related_alerts("5")
    expected = [
        {'alert_id': '2', 'alert_type': 'Malware Detection', 'created_at': '2024-11-17 14:30:00', 'description': 'Endpoint infected with malware', 'primary_transaction_ids': '104,105', 'status': 'CLOSED'},
        {'alert_id': '3', 'alert_type': 'Unauthorized Access', 'created_at': '2024-11-16 18:45:00', 'description': 'Multiple failed login attempts', 'primary_transaction_ids': '105,106', 'status': 'OPEN'}
    ]
    assert actual == expected, f"Expected {expected}, but got {actual}"

if __name__ == "__main__":
    test_get_related_transactions()
    test_expand_related_transactions()
    test_find_related_alerts()
    print("All tests passed!")

