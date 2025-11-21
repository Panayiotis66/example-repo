import statistics


float_numbers=[]
entries=0

while entries != 10:
    float_numbers.append(float(input("Please enter a float number: ")))
    entries += 1

print(float_numbers)

print("The sum of the number is:" + str(sum(float_numbers)))

print("The maximum number is: "+ str(max(float_numbers)))

print("The minimum number is: "+ str(min(float_numbers)))

print("The mean value is:" + str(round(statistics.mean(float_numbers),2)))

print ("The average of the values is:"+ str(statistics.median(float_numbers)))