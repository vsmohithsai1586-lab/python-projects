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
while True:
    user_password = input("Enter a password to check (or type 'quit' to exit): ")
    if user_password == "quit":
        break
    result = check_password(user_password)
    print(result)