# Bug reports for exercise1.py

Line: 3
Problem: The condition checks if n % 2 == 1, which is true for odd numbers, not even numbers. It should check for equality to 0 to determine if a number is even.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: The function returns the sum of width and height, but the area of a rectangle is the product of width and height, not the sum.
Example: rectangle_area(5, 3) returns 8, expected 15.
Fix: return width * height

Line: 13
Problem: The function adds 2 to n, but "twice the number" means multiplying by 2, not adding 2.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
