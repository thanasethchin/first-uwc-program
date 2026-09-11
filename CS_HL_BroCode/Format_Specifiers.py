# Format Specifiers = {value:flags} format a value based on what flags are inserted

price = 27.09

print(f"The price is ${price:.3f}") # .3f means 3 decimal points
print(f"The price is ${price:010}") # 010 means there are 10 spaces in total and 0 is padded
print(f"The price is ${price:<10}") # :< means the spaces are left justified (moves to the left)
print(f"The price is ${price:>10}") # :> means the spaces are right justified (moves to the right)
print(f"The price is ${price:^10}") # :^ means centering the string
print(f"The price is ${price:+}") # :+ means adding a plus infront
print(f"The price is ${price:,}") # :, means separating the thousand comma

print(f"The price is ${price:+,.2f}") # mix and match