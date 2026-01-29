# ===== EXERCISE 1: Multi-line For Loop (Sum Even Numbers) =====
print("Exercise 1: Sum of even numbers 1-20")
total = 0
for i in range(1, 21):
    if i % 2 == 0:
        total += i
        print(f"Added {i}, running total: {total}")
print(f"Final sum: {total}\n")

# ===== EXERCISE 2: Nested Loops (Multiplication Table) =====
print("Exercise 2: 5x5 Multiplication Table")
for i in range(1, 6):          
    row = ""
    for j in range(1, 6):       
        row += f"{i*j:2d} "    
    print(row)
print()

# ===== EXERCISE 3: While Loop with Break =====
print("Exercise 3: Countdown with Break")
count = 10
while count > 0:
    print(count, end=" ")
    if count == 5:
        print("\n→ BREAK at 5!")
        break
    count -= 1
print("→ Loop ended\n")

# ===== EXERCISE 4: Continue (Skip Multiples of 3) =====
print("Exercise 4: Numbers 1-15, skipping multiples of 3")
for num in range(1, 16):
    if num % 3 == 0:
        print(f"Skip {num}")
        continue
    print(num, end=" ")
print("\n")

# ===== EXERCISE 5: Nested with Continue/Break Combo =====
print("Exercise 5: Nested pattern (break on diagonal)")
for row in range(1, 4):
    print(f"Row {row}:", end=" ")
    for col in range(1, 4):
        if row == col:
            print(f"STOP", end=" ")
            break
        print(f"{row*col:2d}", end=" ")
    print()
