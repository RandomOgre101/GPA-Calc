from art import logo

grades = {
    "s": 10, 
    "a": 9,
    "b": 8,
    "c": 7,
    "d": 6,
    "e": 5,
    "f": 1,
    "n": 1
}

print(logo)

subjects = int(input("\nHow many subjects?: "))
total_credits = 0
gpa = 0


for i in range(0,subjects):
    credits = int(input("\nHow many credits?: "))
    total_credits += credits
    grade = input("What is your grade?: ").lower()
    gpa += grades[grade]*credits

final_gpa = gpa/total_credits

print(f"\nYour gpa is: {final_gpa}\n")
