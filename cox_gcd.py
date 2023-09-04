large_number = int(input("Enter a large number: "))
small_number = int(input("Enter a small number: "))
if large_number or small_number < 0:
    print("You entered a negative number")
if (large_number < small_number)  or (small_number > large_number):
    print("The large number is smaller than the small number")
while (large_number % small_number)  != 0:
    large_number /= small_number
print("The GCD is", large_number)

    
