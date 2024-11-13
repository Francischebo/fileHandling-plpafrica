# File Read & Write Challenge 🖋️
try:
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        for line in infile:
            modified_line = line.replace('old', 'new')
            outfile.write(modified_line)
except FileNotFoundError:
    print("Error: Input file not found.")
except PermissionError:
    print("Error: Permission denied to read input file.")
except Exception as e:
    print(f"Error: {e}")
else:
    print("File read and modified successfully.")

# Error Handling Lab 🧪
filename = input("Enter filename: ")
try:
    with open(filename, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"Error: {e}")