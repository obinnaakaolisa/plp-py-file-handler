# File Handling and Exception Handling Assignment
# Combining File Read & Write Challenge with Error Handling Lab

def read_and_modify_file(input_filename, output_filename):
    """
    Read a file and write a modified version to a new file.
    Modifications:
    - Add line numbers
    - Convert text to uppercase
    - Add word count for each line
    
    Parameters:
    input_filename (str): Name of the file to read
    output_filename (str): Name of the file to write modified content
    
    Returns:
    bool: True if successful, False otherwise
    """
    try:
        # Open and read the input file
        with open(input_filename, 'r') as input_file:
            lines = input_file.readlines()
        
        # Check if file is empty
        if not lines:
            print(f"Warning: '{input_filename}' is empty!")
            return False
        
        # Modify the content
        modified_lines = []
        for index, line in enumerate(lines, start=1):
            # Remove trailing whitespace
            line = line.rstrip()
            # Convert to uppercase
            uppercase_line = line.upper()
            # Count words in the line
            word_count = len(line.split())
            # Format: Line number | Content | Word count
            modified_line = f"Line {index}: {uppercase_line} [Words: {word_count}]\n"
            modified_lines.append(modified_line)
        
        # Write modified content to output file
        with open(output_filename, 'w') as output_file:
            output_file.writelines(modified_lines)
        
        print(f"✅ Success! File modified and saved as '{output_filename}'")
        print(f"📊 Total lines processed: {len(lines)}")
        return True
        
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist!")
        print("Please check the filename and try again.")
        return False
    
    except PermissionError:
        print(f"❌ Error: Permission denied to read '{input_filename}'!")
        print("You don't have the necessary permissions to access this file.")
        return False
    
    except IOError as e:
        print(f"❌ Error: Cannot read file '{input_filename}'!")
        print(f"Details: {e}")
        return False
    
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")
        return False


def create_sample_file(filename):
    """Create a sample file for testing."""
    try:
        with open(filename, 'w') as file:
            file.write("Hello World\n")
            file.write("Python is amazing\n")
            file.write("File handling is fun\n")
            file.write("Exception handling is important\n")
        print(f"✅ Sample file '{filename}' created successfully!")
        return True
    except Exception as e:
        print(f"❌ Error creating sample file: {e}")
        return False


def main():
    """Main function to run the file handling program."""
    
    print("=" * 60)
    print("FILE HANDLING & EXCEPTION HANDLING PROGRAM")
    print("=" * 60)
    print()
    
    while True:
        print("\nOptions:")
        print("1. Read and modify an existing file")
        print("2. Create a sample file for testing")
        print("3. Exit")
        print()
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            # File Read & Write Challenge with Error Handling
            print("\n" + "-" * 60)
            print("FILE READ & WRITE CHALLENGE")
            print("-" * 60)
            
            input_filename = input("\nEnter the name of the file to read: ").strip()
            
            if not input_filename:
                print("❌ Error: Filename cannot be empty!")
                continue
            
            # Suggest output filename
            output_filename = input("Enter the name for the output file (or press Enter for default): ").strip()
            
            if not output_filename:
                # Create default output filename
                if '.' in input_filename:
                    name, ext = input_filename.rsplit('.', 1)
                    output_filename = f"{name}_modified.{ext}"
                else:
                    output_filename = f"{input_filename}_modified.txt"
            
            print(f"\n📂 Reading from: {input_filename}")
            print(f"📝 Writing to: {output_filename}")
            print()
            
            # Attempt to read and modify the file
            success = read_and_modify_file(input_filename, output_filename)
            
            if success:
                # Show preview of output
                try:
                    with open(output_filename, 'r') as file:
                        print("\n" + "=" * 60)
                        print("PREVIEW OF MODIFIED FILE:")
                        print("=" * 60)
                        preview_lines = file.readlines()[:5]  # Show first 5 lines
                        for line in preview_lines:
                            print(line.rstrip())
                        if len(preview_lines) >= 5:
                            print("... (showing first 5 lines)")
                        print("=" * 60)
                except:
                    pass
        
        elif choice == "2":
            # Create sample file for testing
            print("\n" + "-" * 60)
            print("CREATE SAMPLE FILE")
            print("-" * 60)
            
            sample_filename = input("\nEnter name for sample file (or press Enter for 'sample.txt'): ").strip()
            
            if not sample_filename:
                sample_filename = "sample.txt"
            
            create_sample_file(sample_filename)
        
        elif choice == "3":
            print("\n👋 Thank you for using the File Handling Program!")
            print("=" * 60)
            break
        
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()