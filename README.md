# Hash Tools

This versatile Python script, powered by the Tkinter library, provides a simple graphical interface to both verify whether a provided hash (MD5, SHA-1, SHA-256, SHA-384, SHA-512, BLAKE2b, or BLAKE2s) matches the content of a selected file and generate hashes for any file. This project was created with the purpose of learning Python.

## Requirements

- Python 3.x installed on your system.
- [pyperclip v1.8.2](https://pypi.org/project/pyperclip/)

## Usage

### Use the Executable

1. **Download and Run the Executable:**

   - Obtain the executable file (`hashTools.exe`) from your desired location and double-click to launch the application.

2. **Interact with the Graphical Interface:**

   - The graphical interface is divided into two tabs: "Check Hash" and "Generate Hash."

     - **Check Hash Tab:**

       - Use the dropdown menu to choose the hash function.
       - Enter the hash to check in the provided field.
       - Click the "Select file to check hash" button to choose the file.
       - Click the "Check Hash" button to perform the verification.

     - **Generate Hash Tab:**
       - Select this tab if you want to generate a hash for any file.
       - Use the dropdown menu to choose the hash function.
       - Click the "Select file to generate hash" button to choose the file.
       - The generated hash will be displayed, and you can copy it to the clipboard using the "Copy Hash" button.

### Use the Script

1. **Clone the repository to your local machine:**

```bash
git clone https://github.com/Cayetano97/hashTools.git
```

2. **Navigate to the project directory:**

```bash
cd hashTools
```

3. **Install the required dependencies using `pip` and the `requirements.txt` file:**

```bash
pip install -r requirements.txt
```

4. **Run the script:**

```bash
python hashTools.py
```

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
  a95bc0005b1c39a5dcd3dd728867b8f3
  ```

- SHA-1

  ```
  cff8c3994ab3d7ecdc7805630af36770b95ec43b
  ```

- SHA-256

  ```
  896a54e6f0667a5e1bfd2ff21170e8a354d4c4c92f846ea9748793d4d7f38a73
  ```

- SHA-384

  ```
  aba7c74e97d12c8d56fd25250abb2ef0a57e43a0298f008b30fd51a6c514337fb17308e2f20f133ed992be935a14bc43
  ```

- SHA-512

  ```
  02fb4b8873a0cf5cbc70df5ab5c6e0c904878baff09f264d97d40d633c542857aac21087ad3a824e67a8761fec7ac14a26012e9e51be22ec8d1e027edb7b1693
  ```

- BLAKE2b

  ```
  c938df16c6468047bad38f3b1410a2b5c164434621f7a5f5040450898ddfb13f04d81ad7c1371d4fda0536903d5dda2713e90aa59ec85368bf0b6855bea73441
  ```

- BLAKE2s

  ```
  16d2435f58d056766628296916e7de8ed7ae0a2e3343dfb0a01935d2851d07e9
  ```
