import secrets
import string 

def generate_Password(password_len):
    if password_len<8:
        print("Password length should be 8")
        return 0
    else:
        password_letter=string.ascii_letters+ string.digits + string.punctuation
        password=''.join(secrets.choice(password_letter) for _ in range(password_len))
        return password

if __name__ == "__main__":
    
    password_len=int(input("Enter the password leangth : "))
    try:
        if password_len>0:
            password=generate_Password(password_len)
            print(password)
        else:
            print("Enter a positive number of length for password generator")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")