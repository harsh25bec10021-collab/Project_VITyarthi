README - Password Manager
==========================

Setup Instructions
------------------
1. Ensure Python 3 is installed on your system.
2. Place `passwords.py` in your working directory.
3. Run the program using:

       python passwords.py

4. A `passwords.json` file will be created automatically to store your data.

Code Details
------------
- The project uses a `PasswordManager` class that handles:
  - Loading and saving data from `passwords.json`
  - Adding, retrieving, searching, deleting password records
  - Listing entries (full details or just names)
  - Importing/exporting data

- The program uses a menu-driven interface inside the `main()` function, allowing:
  - Add password  
  - Retrieve password  
  - View all passwords  
  - Search passwords  
  - Delete entries  
  - Export to text  
  - Import from JSON  

- All data is stored in a simple JSON structure with fields:
  - name  
  - username  
  - password  

Note: Passwords are stored in plain text (no encryption).
