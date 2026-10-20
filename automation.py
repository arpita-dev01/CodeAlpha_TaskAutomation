"""
CodeAlpha Internship - Task 3
Task Automation with Python Scripts (beginner level)

Two real-life automations in one menu-driven script:
  1. Move all .jpg images from a folder into a new folder.
  2. Extract all email addresses from a .txt file and save them to another file.

Concepts used: os, shutil, re, file handling, functions, loops, if-else.
Only Python standard library modules are used - nothing to install.
"""

import os
import shutil
import re


# ---------------------------------------------------------------
# AUTOMATION 1: MOVE ALL .JPG FILES INTO A NEW FOLDER
# ---------------------------------------------------------------

def move_jpg_files():
    """Move every .jpg / .jpeg file from a source folder to a destination folder."""
    print("\n--- Move JPG Images ---")

    source_folder = input("Enter the SOURCE folder path: ").strip()

    # os.path.isdir() checks that the path exists AND is a folder.
    if not os.path.isdir(source_folder):
        print("Error: '" + source_folder + "' is not a valid folder. Returning to menu.")
        return

    destination_folder = input("Enter the DESTINATION folder path: ").strip()

    if destination_folder == "":
        print("Error: destination cannot be empty. Returning to menu.")
        return

    # Create the destination folder if it does not exist yet.
    # exist_ok=True stops Python raising an error if it is already there.
    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0

    # os.listdir() returns a list of every file/folder name inside the folder.
    for filename in os.listdir(source_folder):
        # .lower() makes the check work for .JPG as well as .jpg
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            old_path = os.path.join(source_folder, filename)
            new_path = os.path.join(destination_folder, filename)

            # Skip folders that happen to end in .jpg (rare, but safe to check)
            if not os.path.isfile(old_path):
                continue

            shutil.move(old_path, new_path)
            print("  Moved: " + filename)
            moved_count = moved_count + 1

    if moved_count == 0:
        print("No .jpg or .jpeg files were found in that folder.")
    else:
        print("Done! Moved " + str(moved_count) + " image(s) to '" + destination_folder + "'.")


# ---------------------------------------------------------------
# AUTOMATION 2: EXTRACT EMAIL ADDRESSES FROM A TEXT FILE
# ---------------------------------------------------------------

# A regular expression (regex) pattern that matches an email address.
#   [a-zA-Z0-9._%+-]+   one or more characters allowed before the @
#   @                   the literal @ symbol
#   [a-zA-Z0-9.-]+      the domain name, e.g. gmail
#   \.                  a literal dot
#   [a-zA-Z]{2,}        the extension, e.g. com / org / in (2+ letters)
EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails():
    """Read a .txt file, find all email addresses, save them to a new file."""
    print("\n--- Extract Email Addresses ---")

    input_file = input("Enter the path of the .txt file to read: ").strip()

    if not os.path.isfile(input_file):
        print("Error: '" + input_file + "' was not found. Returning to menu.")
        return

    # 'r' means read mode. We read the whole file into one big string.
    file = open(input_file, "r")
    text = file.read()
    file.close()

    # re.findall() returns a LIST of every match it can find.
    found_emails = re.findall(EMAIL_PATTERN, text)

    if len(found_emails) == 0:
        print("No email addresses were found in that file.")
        return

    # Remove duplicates while keeping the original order.
    unique_emails = []
    for email in found_emails:
        if email not in unique_emails:
            unique_emails.append(email)

    output_file = input("Enter the name of the output file (e.g. emails.txt): ").strip()
    if output_file == "":
        output_file = "emails.txt"
        print("No name given - using 'emails.txt'.")

    file = open(output_file, "w")
    for email in unique_emails:
        file.write(email + "\n")
    file.close()

    print("\nFound " + str(len(found_emails)) + " email(s), "
          + str(len(unique_emails)) + " of them unique:")
    for email in unique_emails:
        print("  " + email)
    print("Saved to '" + output_file + "'.")


# ---------------------------------------------------------------
# MENU
# ---------------------------------------------------------------

def show_menu():
    print("\n" + "=" * 45)
    print("        PYTHON TASK AUTOMATION TOOL")
    print("=" * 45)
    print("1. Move all .jpg images to a new folder")
    print("2. Extract email addresses from a .txt file")
    print("3. Exit")
    print("=" * 45)


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please type 1, 2 or 3.")


if __name__ == "__main__":
    main()
