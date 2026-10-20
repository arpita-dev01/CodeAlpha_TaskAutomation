# CodeAlpha Python Programming Internship — Task 3: Task Automation with Python Scripts

A menu-driven Python script that automates two repetitive tasks using only Python standard library modules. No additional packages or internet connection are required.

## Task Requirements

| Automation | Status |
|---|---|
| Move `.jpg` and `.jpeg` files from one folder to another | Done |
| Extract email addresses from a `.txt` file and save them | Done |
| Key concepts: `os`, `shutil`, `re`, file handling | Covered |

Web scraping was skipped because it requires additional setup and an internet connection.

## How to Run

```bash
python automation.py
```

On macOS/Linux, use:

```bash
python3 automation.py
```

Then choose option 1, 2, or 3 from the menu.

## Automation 1 — Move JPG Images

Enter a source folder and a destination folder. The script moves `.jpg` and `.jpeg` files and creates the destination folder if it does not exist.

**Warning:** This operation moves files rather than copying them. Test with sample images first.

## Automation 2 — Extract Email Addresses

Enter the path of a `.txt` file. The script uses a regular expression to find email addresses, removes duplicates, displays the results, and writes the unique addresses to an output file, one per line.

A sample file, `sample_emails.txt`, is included.

Example:

```text
Enter the path of the .txt file to read: sample_emails.txt
Enter the name of the output file (e.g. emails.txt): emails.txt
```

## The Regex Explained

```python
r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
```

| Part | Meaning |
|---|---|
| `[a-zA-Z0-9._%+-]+` | Characters allowed before `@` |
| `@` | The literal `@` symbol |
| `[a-zA-Z0-9.-]+` | Domain name |
| `\.` | A literal dot |
| `[a-zA-Z]{2,}` | Domain extension of two or more letters |

## Project Structure

```text
CodeAlpha_TaskAutomation/
├── automation.py
├── sample_emails.txt
├── README.md
└── .gitignore
```

## Author

Submitted as part of the CodeAlpha Python Programming Internship.
