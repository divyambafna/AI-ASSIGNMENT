import random
import string

def generate_captcha(length=6):
    """
    Generates a random alphanumeric captcha string.
    Minor changes: Added punctuation-avoidance for clarity and a verification loop.
    """
    # Using the letters and digits only in order to avoid confusing symbols we might get
    characters = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choice(characters) for _ in range(length))
    return captcha_text

def run_verification():
    secret = generate_captcha()
    print(f"CAPTCHA: {secret}")
    
    user_input = input("Please enter the CAPTCHA above: ")
    
    if user_input == secret:
        print("Verification Successful!")
    else:
        print("Verification Failed. Access Denied.")

if __name__ == "__main__":
    run_verification()
