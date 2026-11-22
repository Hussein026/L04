# Bug reports for exercise3.py

Line: 3
Problem: The function averages a list but crashes on an empty list because len(numbers) would be 0, causing division by zero. The docstring states that an empty list has average 0, so it should handle this case.
Example: average([]) returns ZeroDivisionError, expected 0.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: The function splits the text and returns the first word, but if the text is empty or contains only whitespace, split() returns an empty list, and accessing [0] raises an IndexError. The docstring says to return "" if the text is empty.
Example: first_word("  ") returns IndexError, expected "".
Fix: return text.split()[0] if text.strip() else ""

Line: 13
Problem: The function returns part / total * 100, but if total is 0, this causes division by zero. The docstring specifies that if total is 0, the result is 0.
Example: percent(5, 0) returns ZeroDivisionError, expected 0.
Fix: return part / total * 100 if total != 0 else 0
