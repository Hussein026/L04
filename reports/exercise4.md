# Bug reports for exercise4.py

Line: 9
Problem: The condition checks if ADMIN_PASSWORD is not empty and compares the password to ADMIN_PASSWORD, but it should check if the password matches exactly the admin password. The condition "ADMIN_PASSWORD != "" and password == ADMIN_PASSWORD" is logically flawed because even if the password is empty, it will return True if ADMIN_PASSWORD is not empty, which contradicts the docstring. The docstring says "true if the password is the admin password", meaning only when the password exactly matches the admin password.
Example: check_admin("") returns True, expected False.
Fix: return password == ADMIN_PASSWORD

Line: 14
Problem: The function uses string formatting to directly insert the username into a SQL query without escaping, making it vulnerable to SQL injection. This means an attacker could pass a malicious input like "'; DROP TABLE users; --" to execute arbitrary SQL commands.
Example: find_user("x' OR '1'='1", "alice") returns the row of alice, expected None.
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
