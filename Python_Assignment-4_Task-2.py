# Task 2: Write and Append Data to a File

# Step 1: Take user input and write to file
data = input("Enter some data to write into output.txt: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

# Step 2: Append additional data
extra_data = input("Enter additional data to append: ")
with open("output.txt", "a") as file:
    file.write(extra_data + "\n")

# Step 3: Read and display the final content
print("\nFinal content of output.txt:\n")
with open("output.txt", "r") as file:
    print(file.read())
