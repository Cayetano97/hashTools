# Hash Checker

This compact Python script, powered by the Tkinter library, provides a simple graphical interface to verify whether a provided hash (MD5, SHA-1, SHA-256, SHA-384, or SHA-512) matches the content of a selected file.

## Requirements

- Python 3.x installed on your system.

## Usage

1. **Download and Run the Executable:**

   - Obtain the executable file (`hashChecker.exe`) from your desired location and double-click to launch the application.

2. **Interact with the Graphical Interface:**

   - The graphical interface opens with a dropdown menu allowing you to select the hash function. Enter the hash and select the file.

   - Alternatively, you can run the `hashChecker.py` script

## Warning

Exercise caution when handling files and providing hashes. Ensure a full understanding of the script's purpose and implications before use.

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

## Verifying the executable

- MD5

  ```
  59427373bbbe49004a9c7aedd9885e1c
  ```

- SHA-1

  ```
  27f37952e8d23368b014a2b643a3fd8bc5a4b14d
  ```

- SHA-256

  ```
  5e4a86b7f601996475c6ec8c66a175cf68e86563f02ac0efae5f86ff80a72e9e
  ```

- SHA-384

  ```
  8de94bef838ba2bd8794c6fe7af6cb8f0598ca70673ba16cca4695ddd6b5806a18fd0e55f9aa6635f48752bbeb107bae
  ```

- SHA-512

  ```
  3bf7d54e791aabea9226ec13edcadff783a7f61d7cfdde5acfae133f0718c037564b058d0f450b3d9a1eb0b489ee7f06a2dd6aa8b809f3a941ceb942f9b3a1c5
  ```
