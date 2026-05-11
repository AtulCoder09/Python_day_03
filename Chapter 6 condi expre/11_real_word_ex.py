balance = 10000
withdraw = int(input("Enter withdrawal amount :"))

if withdraw <= balance:
    balance -= withdraw
    print("Transaction sucessful!")
    print("Remaining balance :", balance)

else:
    print("Insuffecent balance")