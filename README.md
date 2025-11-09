# File Handling and Exception Handling Assignment

A comprehensive Python program demonstrating file reading, writing, modification, and robust error handling.

## 📋 Assignment Requirements

This program fulfills both assignment challenges:

### ✅ Challenge 1: File Read & Write Challenge 🖋️
- Reads content from an input file
- Modifies the content (adds line numbers, converts to uppercase, counts words)
- Writes the modified content to a new output file

### ✅ Challenge 2: Error Handling Lab 🧪
- Asks user for a filename
- Handles errors if file doesn't exist
- Handles permission errors
- Handles I/O errors
- Provides clear error messages

## 🌟 Features

- **📖 File Reading**: Reads any text file specified by the user
- **✏️ Content Modification**: 
  - Adds line numbers to each line
  - Converts text to uppercase
  - Counts words per line
- **💾 File Writing**: Saves modified content to a new file
- **🛡️ Robust Error Handling**: 
  - FileNotFoundError (file doesn't exist)
  - PermissionError (no access rights)
  - IOError (read/write issues)
  - Empty file detection
- **🎨 User-Friendly Interface**: Interactive menu system
- **🧪 Sample File Generator**: Create test files easily
- **👀 Preview Feature**: Shows first 5 lines of modified output

## 🚀 How to Run

1. **Install Python 3.x** (if not already installed)
2. **Clone or download** this repository
3. **Navigate** to the project directory
4. **Run the program**:
   ```bash
   python file_handler.py
   ```

## 📖 Usage Guide

### Main Menu Options

```
1. Read and modify an existing file
2. Create a sample file for testing
3. Exit
```

### Option 1: Read and Modify File

1. Enter the name of the file you want to read
2. Enter a name for the output file (or press Enter for default)
3. The program will:
   - Read the input file
   - Modify the content
   - Save to the output file
   - Display a preview

### Option 2: Create Sample File

1. Enter a name for the sample file (or use default)
2. A test file with sample content will be created

### Option 3: Exit

Exits the program

## 💡 Example Usage

### Example 1: Successful File Processing

**Input file (input.txt):**
```
Hello World
Python is amazing
File handling is fun
```

**Program interaction:**
```
Enter the name of the file to read: input.txt
Enter the name for the output file: output.txt

📂 Reading from: input.txt
📝 Writing to: output.txt

✅ Success! File modified and saved as 'output.txt'
📊 Total lines processed: 3
```

**Output file (output.txt):**
```
Line 1: HELLO WORLD [Words: 2]
Line 2: PYTHON IS AMAZING [Words: 3]
Line 3: FILE HANDLING IS FUN [Words: 4]
```

### Example 2: File Not Found Error

```
Enter the name of the file to read: nonexistent.txt

❌ Error: The file 'nonexistent.txt' does not exist!
Please check the filename and try again.
```

### Example 3: Permission Error

```
Enter the name of the file to read: protected.txt

❌ Error: Permission denied to read 'protected.txt'!
You don't have the necessary permissions to access this file.
```

## 🧪 Test Cases

| Test Case | Input File | Expected Result |
|-----------|------------|-----------------|
| Normal file | `sample.txt` | Successfully modified |
| Non-existent file | `missing.txt` | FileNotFoundError handled |
| Empty file | `empty.txt` | Warning message displayed |
| Protected file | `system.txt` | PermissionError handled |
| Large file | `big.txt` | Successfully processed |

## 🔧 Modifications Applied

The program applies the following modifications to input files:

1. **Line Numbering**: Each line gets a sequential number
2. **Uppercase Conversion**: All text is converted to uppercase
3. **Word Counting**: Displays word count for each line
4. **Formatting**: Structured format: `Line X: CONTENT [Words: Y]`

## 📊 Error Handling

The program handles these exceptions:

| Exception | Cause | Program Response |
|-----------|-------|------------------|
| `FileNotFoundError` | File doesn't exist | Clear error message, suggests checking filename |
| `PermissionError` | No read/write access | Explains permission issue |
| `IOError` | Input/output error | Shows detailed error information |
| `Exception` | Any other error | Catches and displays unexpected errors |

## 🏗️ Code Structure

```
file_handler.py
├── read_and_modify_file()    # Main file processing function
├── create_sample_file()      # Sample file generator
└── main()                    # User interface and program flow
```

## 🎓 Key Concepts Demonstrated

- **File I/O Operations**: `open()`, `read()`, `write()`, `close()`
- **Context Managers**: Using `with` statement for automatic file closing
- **Exception Handling**: `try-except-finally` blocks
- **String Manipulation**: `.upper()`, `.strip()`, `.split()`
- **List Operations**: Working with lists of lines
- **User Input Validation**: Checking for empty inputs
- **Formatted Output**: Using f-strings for clear messages

## 📚 Functions Explained

### `read_and_modify_file(input_filename, output_filename)`
- **Purpose**: Reads a file, modifies its content, and writes to a new file
- **Parameters**: 
  - `input_filename`: File to read
  - `output_filename`: File to write
- **Returns**: `True` if successful, `False` otherwise
- **Error Handling**: Catches and handles all file-related errors

### `create_sample_file(filename)`
- **Purpose**: Creates a sample text file for testing
- **Parameters**: `filename` - Name of file to create
- **Returns**: `True` if successful, `False` otherwise

### `main()`
- **Purpose**: Main program loop and user interface
- **Features**: Menu system, user input handling, program flow control

## 📝 Requirements

- Python 3.x
- No external libraries required (uses only standard library)

## 🎯 Learning Outcomes

After working with this program, you will understand:

✅ How to read files in Python  
✅ How to write to files in Python  
✅ How to modify file content  
✅ How to handle file-related exceptions  
✅ How to create robust, error-proof programs  
✅ How to provide user-friendly error messages  
✅ Best practices for file handling with `with` statement  

## 🔍 Testing the Program

1. **Test with existing file**:
   ```bash
   # Create a test file first
   echo "Hello World" > test.txt
   # Then run the program and select option 1
   ```

2. **Test error handling**:
   - Try opening a non-existent file
   - Try opening a protected system file
   - Try with an empty filename

3. **Test with sample file**:
   - Select option 2 to create `sample.txt`
   - Then select option 1 to process it

## 👤 Author

Akaolisa Obinna

## 📚 Course

Intro to Python - File Handling and Exception Handling Assignment - PLP Assignment

## 📄 License

This project is for educational purposes.

## 🙏 Acknowledgments

This project demonstrates practical file handling and exception handling techniques essential for building robust Python applications.