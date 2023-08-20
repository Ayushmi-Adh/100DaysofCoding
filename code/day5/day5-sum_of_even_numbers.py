#SUM OF EVEN NUMBERS USING FOR LOOP IN RANGE
total_sum=0
for even in range(2,101,2):
    total_sum += even
print(f"The total sum is:{total_sum}")