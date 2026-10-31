# NIST Password Checker

A Python GUI application that checks password strength based on modern cybersecurity guidelines.

## Features
* **Length Check:** Ensures passwords are at least 15 characters long.
* **Blocklist:** Rejects commonly used and breached passwords.
* **Repeated Characters:** Rejects passwords where a single character makes up more than half the length.

## NIST Guidelines Followed
NIST 2025 guidance prioritizes length because password strength grows exponentially with each added character, making brute-force attacks far harder than any short but complex string. Forcing special characters and numbers often backfires, as users resort to predictable patterns like "Password123!" or write passwords down, whereas long passphrases are both stronger and easier to remember.

## Testing Scenarios

**1. Length Check Failure:**
![Short Password](<Screenshot 2026-10-31 111744.png>)

**2. Repeated Character Failure:**
![Repeated Characters](<Screenshot 2026-10-31 111827.png>)

**3. Blocklist Failure:**
![Common Password](<Screenshot 2026-10-31 111841.png>)

**4. Password Accepted:**
![Accepted Password](<Screenshot 2026-10-31 111905.png>)

## How to Run
1. Make sure Python is installed.
2. Run `python password_checker_gui.py` in the terminal.
3. Enter a password in the window and click "Check Password".