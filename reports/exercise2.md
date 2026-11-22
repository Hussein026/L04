# Bug reports for exercise2.py

Line: 3
Problem: The condition checks if the grade is "5 or more" but uses > 5, which excludes 5. It should use >= 5 to include 5.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: The condition checks for "at least 8 characters" using > 8, which excludes 8 characters. It should use >= 8 to include 8 characters.
Example: is_valid_password("abcdefgh") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 13
Problem: The function clamps x between low and high, but uses min(x, low) which incorrectly uses low twice. It should use min(x, high) to cap at high.
Example: clamp(10, 1, 5) returns 1, expected 5.
Fix: return max(low, min(x, high))
