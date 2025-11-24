README - Password Manager Project
=================================

Project Overview
----------------
This Password Manager is a simple command‑line application written in Python that allows users to securely store, retrieve, search, delete, import, and export password entries.  
It uses a JSON file for data storage and provides an easy-to-use menu interface.

Features
--------
- Add new password entries  
- Retrieve a password by service name  
- List all entries or only names  
- Search entries by name or username  
- Delete existing entries  
- Export data to a readable text file  
- Import data from a JSON file  
- Automatically saves all changes

How to Run
----------
1. Ensure you have Python 3 installed.  
2. Place `passwords.py` in your working directory.  
3. Run the program using:

    python passwords.py

4. Follow the on-screen menu to use the password manager.

---------------------------------------------

PROJECT REPORT
==============

1. Introduction
---------------
Password management is essential for digital safety. This project implements a lightweight password manager using Python, aimed at beginners learning file handling and object‑oriented programming.

2. Objective
------------
- To create a functional and user-friendly password management system.  
- To practice Python concepts such as classes, file handling, JSON operations, and CLI design.

3. System Architecture
----------------------
The project uses a single class: **PasswordManager**, responsible for:
- Loading and saving JSON data  
- CRUD operations (Create, Read, Update, Delete)  
- Searching and exporting entries  
- Providing utility functions such as listing and quick access

The `main()` function provides an interactive menu-driven interface.

4. Modules Used
----------------
- `json`: for storing structured data  
- `os`: for file existence checks  
- `getpass` (included but unused in current implementation)  

5. Flow of Execution
--------------------
- On launch, the program loads existing JSON data if available.  
- User interacts through the menu:  
  - Choosing options triggers corresponding methods inside `PasswordManager`.  
  - Any modifications are saved immediately.  
- The user can exit the program safely using option 9.

6. Limitations
--------------
- Passwords are stored in **plain text**, which is not secure.  
- No encryption implemented.  
- No password masking during entry.  
- No multi-user support.

---------------------------------------------

PROJECT STATEMENT
=================

This project aims to develop a simple yet functional password manager in Python that allows users to store and retrieve login credentials efficiently.  
The program demonstrates key programming concepts such as object‑oriented design, persistent data handling using JSON, and building an interactive command-line interface.  
Its purpose is educational, helping students understand how data can be structured, stored, retrieved, and managed in real applications.

---------------------------------------------
