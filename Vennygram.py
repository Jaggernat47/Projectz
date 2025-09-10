from matplotlib import pyplot as plt
from matplotlib_venn import venn3

print("WELCOME TO SET THEORY, let's create a diagram")

print("\n[Enter a label for each circle]")
first_ven = input("Circle A: ")
second_ven = input("Circle B: ")
third_ven = input("Circle C: ")

print("\n[Enter number of people in each region of the Venn diagram]")
A = int(input("A: "))
B = int(input("B: "))
A_B = int(input("A and B: "))
C = int(input("C: "))
A_C = int(input("A and C: "))
B_C = int(input("B and C: "))
A_B_C = int(input("A, B and C: "))

subsets = (A, B, A_B, C, A_C, B_C, A_B_C)

venn3(subsets=subsets, set_labels=(first_ven, second_ven, third_ven))

plt.title("Three-set Venn Diagram")
plt.show()

ven_A = A + A_B + A_C + A_B_C
ven_B = B + A_B + B_C + A_B_C
ven_A_B = A + B + A_B + A_C + B_C + A_B_C
ven_C = C + A_C + B_C + A_B_C
ven_A_C = A + C + A_B + A_C + B_C + A_B_C
ven_B_C = B + C + A_B + A_C + B_C + A_B_C
ven_A_B_C = A + B + C + A_B + A_C + B_C + A_B_C

print(f"\n[Find out how many people are involved in ({first_ven}/{second_ven}/{third_ven})] ")

while True:    
    answer = input("\nEnter here: ")

    if first_ven in answer and second_ven not in answer and third_ven not in answer:
        print(f"[{first_ven}], A total of:", ven_A)
    elif second_ven in answer and first_ven not in answer and third_ven not in answer:
        print(f"[{second_ven}] A total of:", ven_B)
    elif second_ven in answer and first_ven in answer and third_ven not in answer:
        print(f"[{first_ven}/{second_ven}] A total of:", ven_A_B)
    elif third_ven in answer and first_ven not in answer and second_ven not in answer:
        print(f"[{third_ven}] A total of:", ven_C)
    elif first_ven in answer and third_ven in answer and second_ven not in answer:
        print(f"[{first_ven}/{third_ven}] A total of:", ven_A_C)
    elif second_ven in answer and third_ven in answer and first_ven not in answer:
        print(f"[{second_ven}/{third_ven}] A total of:", ven_B_C)
    elif first_ven in answer and second_ven in answer and third_ven in answer:
        print(f"[{first_ven}/{second_ven}, {third_ven}] A total of:", ven_A_B_C)
    else:
        print("ERROR")
        break