# file_handling_assignment.py

def write_to_file(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
            print("✅ File written successfully.")
    except Exception as e:
        print(f"❌ An error occurred while writing: {e}")

def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("📄 File content:\n", content)
    except FileNotFoundError:
        print(f"⚠️ The file '{filename}' does not exist.")
    except Exception as e:
        print(f"❌ An error occurred while reading: {e}")

# Example usage
write_to_file("example.txt", "Hello, World from Week 4 Assignment!")
read_from_file("example.txt")
