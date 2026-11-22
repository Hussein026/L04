# Bug reports for exercise4.py

Line: 9
Problem: The function checks if the password is not equal to an empty string and equal to ADMIN_PASSWORD, but it should check if the password is exactly equal to ADMIN_PASSWORD. The condition `ADMIN_PASSWORD != ""` is unnecessary and incorrect because ADMIN_PASSWORD is hardcoded as "admin123", which is not empty. This condition will always be true and does not validate the password correctly.
Example: check_admin("admin123") returns True, expected True (correct), but check_admin("") returns True, expected False.
Fix: return password == ADMIN_PASSWORD

Line: 14
Problem: The function uses string formatting to directly insert the username into a SQL query without escaping, which makes it vulnerable to SQL injection attacks. This is a security bug.
Example: find_user(db, "'; DROP TABLE users; --") returns a row that drops the table, expected None.
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
