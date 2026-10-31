import tkinter as tk

def check_length(password):
    if len(password) >= 15:
        return True
    else:
        return False
common_passwords = {"123456","admin","12345678","123456789","12345","password","Aa123456","1234567890","Pass@123","admin123","1234567","123123","111111","12345678910","P@ssw0rd","Password","Aa@123456","admintelecom","Admin@123","112233","qwerty","1234","abc123","password1","11111111","secret","monkey","dragon","welcome","iloveyou","letmein","000000"}
def check_blocklist(password):
    if password in common_passwords:
        return True
    else:
        return False
def check_repeated_chars(password):
    max_count = 0
    for char in set(password):
        char_count = password.count(char)
        if char_count > max_count:
            max_count = char_count
    if max_count > len(password) / 2:
        return False
    return True
def check_password(password):
    if check_blocklist(password):
       return "Rejected: this password is too common. please try again"
    elif check_length(password) == False:
        return "Rejected: password must be at least 15 characters. please try again"
    elif check_repeated_chars(password) == False:
        return "Rejected: password contains too many repeated characters. please try again"
    else:
        return "Accepted: password meets length and blocklist requirements."

def on_check_button_click():
    typed_password = password_entry.get()
    final_message = check_password(typed_password)
    result_label.config(text=final_message)

window = tk.Tk()
window.title("NIST Password Checker")
window.geometry("800x500")


instruction_label = tk.Label(window, text="Enter a password to check:")
instruction_label.pack(pady=10)  # pack() puts it in the window, pady adds vertical padding

# Password Text Box
password_entry = tk.Entry(window, width=30)
password_entry.pack(pady=5)

# Check Button
check_button = tk.Button(window, text="Check Password", command=on_check_button_click)
check_button.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="")
result_label.pack(pady=20)

window.mainloop()