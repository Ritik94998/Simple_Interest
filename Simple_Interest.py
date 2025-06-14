# Simple Interest Calculator
# Input principal, rate and time
principal = float(input("Enter the amount: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time(annually): "))

# Calculate simple interest
simple_interest = (principal * rate * time ) / 100

## Display the result
print(f"Simple Interest is: {SI:.2f}USD")
