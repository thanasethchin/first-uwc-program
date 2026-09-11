# String Indexing = accessing elements of a sequence using [] (indexing operator)
#                   [start : end : step]

credit_number = "1234-6345-9889"

print(credit_number[0]) # 1st position
print(credit_number[:4]) # 1st position to 4th (excluding 4th)
print(credit_number[5:10]) # 5th position to 10th (excluding 10th)
print(credit_number[5:]) # 5th position to end
print(credit_number[:-1]) # Starts from end
print(credit_number[::3]) # Counts every 3rd number, start to end
print(credit_number[::-1]) # Reverse the entire string