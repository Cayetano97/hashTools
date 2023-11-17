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
  eb5edbb0517e2378334bdaf1a7fb9365
  ```

- SHA-1

  ```
  d51007a9800bfbbb0feaed7eb95de5ab16cfd720
  ```

- SHA-256

  ```
  6ea8260e58a2d155a24df6a1703685bf66661068a7cdbcd0a97981a3735c1b4b
  ```

- SHA-384

  ```
  63ac162d28b880127e9a9695fb2fcf73b02f31b6ce923f3bef5cd1ec28aa4723f480b1e97458b66924826330fdbbd4f2
  ```

- SHA-512

  ```
  e31f8156856a2d5439dd4db5127b1ab1fa4619e457422ce35101754290cb9467c10dcbd5335b7ff2e59cbb10ae353b3dfd22766ee30a39cd15af26f2810d7ff3
  ```
