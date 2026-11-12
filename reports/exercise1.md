# Bug reports for exercise1.py

Line: 3
Problem: is_even returns True for odd numbers, but the docstring says "true for even numbers". The condition n % 2 == 1 checks for odd numbers.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: rectangle_area returns the sum of width and height, but the docstring says "area of a rectangle". Area should be width times height.
Example: rectangle_area(3, 4) returns 7, expected 12.
Fix: return width * height

Line: 12
Problem: double returns n + 2, but the docstring says "twice the number n". It should return n * 2.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
