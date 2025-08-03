list = ["Apple","Mongo", "Delhi","GKP",100,12]
# All elements
print("list :", list)

# Print the first 3 elements of your list
print("First 3 ele: ", list[0:3])

# Print the last item using negative indexing
print("last ele: ", list[-1])

# List Methods (append/remove/pop/sort/reverse)
# list.append(80)
# list.remove("Mongo")

elem = "Mongo"
if elem in list:
    list.remove(elem)
else :
    print("not found")

print("append: ", list )

numbers = [100, 80, 12, 45]
# Sort
numbers.sort()
print("Sort numbers:", numbers)

# Reverse the numbers
numbers.reverse()
print("Reverse numbers:", numbers)

# Loop and print index with item
# for item in list:
#     print("All item: ", list)

for item in range(len(list)):
    print("All item: " ,list[item])

# Create a list of squares
squares = [x*x for x in range(1, 6)]
print(squares)

# Create list of even numbers using list comprehension
evenNum = [x for x in range(1,25) if(x%2==0)]
print(evenNum)

# TODO List App
# 1. View a todo list
# 2. Add item to the list
# 3. Remove item from the list
# 4. Exit the program

# TODO List App - Clean Simple Version

# todo_list = []

# while True:
#     print("\n==== TODO MENU ====")
#     print("1. View Tasks")
#     print("2. Add Task")
#     print("3. Remove Task")
#     print("4. Exit")
    
#     choice = input("Enter your choice (1-4): ").strip()

#     if choice == "1":
#         if not todo_list:
#             print("📝 No tasks yet.")
#         else:
#             print("\nYour Tasks:")
#             for i, task in enumerate(todo_list, start=1):
#                 print(f"{i}. {task}")

#     elif choice == "2":
#         task = input("Enter task to add: ").strip()
#         if task:
#             todo_list.append(task)
#             print(f"✅ '{task}' added.")
#         else:
#             print("⚠️ Task cannot be empty!")

#     elif choice == "3":
#         task = input("Enter exact task to remove: ").strip()
#         if task in todo_list:
#             todo_list.remove(task)
#             print(f"❌ '{task}' removed.")
#         else:
#             print("⚠️ Task not found.")

#     elif choice == "4":
#         print("👋 Goodbye!")
#         break

#     else:
#         print("❌ Invalid choice. Please enter 1–4.")




# for i in range(1,50) :
#     if(i%2==0):
#         print(i)
        
#     else :
#         print("odd")

# for i in range(1,11):
#     print("2" + "*" + "i",2*i)



# Declare a list of your 5 items
# Print the total number of items in the list
# Use a for loop to print each item

# items = ["Coffee","Chocalate","Milk","Sugar","Ice creame"]
# print(len(items))

# for i in range(len(items)):
#     print("each item is : ", items[i])

# ➡️ Ask user for hours_worked and rate_per_hour
# ➡️ Print the total salary

def calculate_salary(hours_worked, rate_per_hour):
    return hours_worked * rate_per_hour

hours_worked = float(input("enter the hours worked: "))
rate_per_hour = float(input("enter the rate per hour: "))

sal = calculate_salary(hours_worked, rate_per_hour)
print("your salary is: ", sal)