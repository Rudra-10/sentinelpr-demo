#flawed code for demo PRs later
import sqlite3

def get_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # BUG: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    return cursor.fetchone()

def process_items(items):
    result = []
    for i in range(len(items)):         # BUG: O(n²) — should use enumerate
        for j in range(len(items)):
            if items[i] == items[j] and i != j:
                result.append(items[i])
    return result

SECRET_KEY = "hardcoded-secretAc123"  # BUG: hardcoded secret
