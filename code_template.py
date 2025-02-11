def get_related_transactions(alert_id):
    # TODO: Implement logic here
    return []


def expand_related_transactions(alert_id):
    # TODO: Implement logic here
    return []


def find_related_alerts(alert_id):
    # TODO: Implement logic here
    return []


# --- Test Cases ---
# These test cases are written to give examples of the correct responses.
# You do not need to match the input or return types as written in these
#   test cases, feel free to rewrite them as you think is appropriate.

def test_get_related_transactions():
    actual = get_related_transactions("1")
    expected = [
        '101,E001,250.00,USD,2024-11-18 08:45:00',
        '103,E001,400.75,USD,2024-11-18 09:00:00',
    ]
    assert actual == expected


def test_expand_related_transactions():
    actual = expand_related_transactions("5")
    expected = [
        '102,E002,300.50,USD,2024-11-18 08:50:00',
        '105,E002,150.25,USD,2024-11-17 14:10:00',
        '110,E002,1000.50,USD,2024-11-15 10:20:00',
    ]
    assert actual == expected

def test_find_related_alerts():
    actual = find_related_alerts("5")
    expected = [
        '2,Malware Detection,2024-11-17 14:30:00,Endpoint infected with malware,"104,105",CLOSED',
        '3,Unauthorized Access,2024-11-16 18:45:00,Multiple failed login attempts,"105,106",OPEN',
    ]
    assert actual == expected

