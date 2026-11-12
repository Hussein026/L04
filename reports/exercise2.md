# Bug reports for exercise2.py

Line: 3
Problem: is_passing says "True if the grade is 5 or more", but the code uses > 5, which excludes 5.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password says "At least 8 characters and at least one digit", but the code uses > 8, which excludes exactly 8 characters.
Example: is_valid_password("abcdefg1") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 13
Problem: clamp says "x, limited to the range from low to high", but the code uses min(x, low) instead of min(x, high), so values above high are not limited.
Example: clamp(15, 0, 10) returns 0, expected 10.
Fix: return max(low, min(x, high))
