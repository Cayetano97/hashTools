# Hash Checker

This small Python script utilizes the Tkinter library to create a simple graphical interface that allows you to check whether a provided SHA-256 hash matches the content of a selected file.

## Requirements

- Installed Python 3.x

## Usage

1. **Download the Executable:**

   - Download the executable file (`hash_checker.exe`) from the desired location.

2. **Run the Executable:**

   - Double-click the executable file to launch the application.

3. **Interact with the Graphical Interface:**

   - The graphical interface should appear, allowing you to enter the hash and select the file just like in the script version.

or

1. Run the `hash_checker.py` script.
2. Enter the hash you want to check in the input field.
3. Click the "Select File to check hash" button to choose the file you want to verify.
4. The script will calculate the SHA-256 hash of the selected file and compare it with the provided hash.
5. A message will be displayed indicating whether the hashes match or not.

## Warning

Be cautious when handling files and providing hashes. Make sure to fully understand the purpose and implications before using this script.

## Verifying Hash using PowerShell (Windows)

To verify the hash of a file using PowerShell:

1. Open PowerShell.
2. Navigate to the directory where your file is located using the `cd` command.
3. Use the `Get-FileHash` cmdlet to calculate the hash of the file:

   ```powershell
   Get-FileHash -Algorithm SHA256 .\your_file.txt
   ```

   Replace your_file.txt with the actual name of your file.

Compare the displayed hash with the hash you want to verify. If they match, the file content is unchanged.
