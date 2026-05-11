# Python_day_03
Today I learn and understand the "Conditional Expression" and "Loops" (For loop and while loop).


# ATM Withdrawal Program in Python

A simple Python program that simulates an ATM withdrawal using `if-else` conditional statements.

## Code

```python
balance = 10000
withdraw = 2500

if withdraw <= balance:
    balance -= withdraw
    print("Transaction successful!")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")

Output:
Transaction successful!
Remaining balance: 7500

# Python Loops

Loops are used to execute a block of code repeatedly.

## Types of Loops in Python

1. `for` loop
2. `while` loop

---

## `for` Loop

Used when the number of iterations is known.

```python
for i in range(5):
    print(i)
