# CodeAlpha_TaskAutomation

**CodeAlpha Python Programming Internship — Task 3: Task Automation with Python Scripts**

A menu-driven script that automates two small, real-life repetitive tasks.
Only Python standard library modules are used — nothing to install, and no
internet connection is needed.

---

## Task Requirements (from CodeAlpha)

The task asks you to pick one automation idea. This project implements **two**
of the listed ideas:

| Automation | Status |
|---|---|
| Move all .jpg files from a folder to a new folder | Done |
| Extract all email addresses from a .txt file and save them | Done |
| Key concepts: `os`, `shutil`, `re`, file handling | Done |

The third idea (web scraping) was skipped deliberately, since it needs the
`requests` library and an internet connection.

---

## How to Run

```bash
python automation.py
```

On macOS/Linux use `python3 automation.py`. Then choose option 1, 2 or 3 from
the menu.

---

## Automation 1 — Move JPG Images

Enter a source folder and a destination folder. Every `.jpg` and `.jpeg` file
is moved across, and the destination folder is created automatically if it
doesn't exist. Invalid folder paths are rejected instead of crashing.

**Warning:** this *moves* files, it does not copy them. Test it on a folder of
sample images first, not on your only copy of something important.

## Automation 2 — Extract Email Addresses

Enter the path of a `.txt` file. The script uses a regular expression to find
every email address inside it, removes duplicates, prints them, and writes
them to an output file (one per line).

A ready-made test file, `sample_emails.txt`, is included. Try:

```
Enter the path of the .txt file to read: sample_emails.txt
Enter the name of the output file (e.g. emails.txt): emails.txt
```

It contains 7 email addresses, one of which is a duplicate — so the script
reports 7 found and 6 unique. It also contains near-misses like `www.codealpha.tech`
and `user at domain dot com` that are correctly ignored.

---

## The Regex Explained

```python
r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
```

| Part | Meaning |
|---|---|
| `[a-zA-Z0-9._%+-]+` | one or more valid characters before the `@` |
| `@` | the literal `@` symbol |
| `[a-zA-Z0-9.-]+` | the domain name, e.g. `gmail` |
| `\.` | a literal dot |
| `[a-zA-Z]{2,}` | the extension (2 or more letters), e.g. `com`, `in` |

---

## Project Structure

```
CodeAlpha_TaskAutomation/
├── automation.py
├── sample_emails.txt    # test data for automation 2
├── README.md
└── .gitignore
```

---

## Author

Submitted as part of the CodeAlpha Python Programming Internship.
