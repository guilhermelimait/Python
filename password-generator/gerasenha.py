import secrets
import string
import sys

def generate_password(length=16, use_punctuation=True):
    """
    Generate a cryptographically secure password
    
    Args:
        length: Length of password (default: 16)
        use_punctuation: Include special characters (default: True)
    
    Returns:
        str: Generated password
    """
    # Build character set
    chars = string.ascii_letters + string.digits
    if use_punctuation:
        chars += string.punctuation
    
    # Ensure password has at least one of each type
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
    ]
    
    if use_punctuation:
        password.append(secrets.choice(string.punctuation))
    
    # Fill remaining length with random characters
    password += [secrets.choice(chars) for _ in range(length - len(password))]
    
    # Shuffle to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)


if __name__ == "__main__":
    print("Secure Password Generator\n")
    
    # Get length from user or command line
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
        except ValueError:
            print("Invalid length. Using default (16).")
            length = 16
    else:
        try:
            length = int(input("Enter password length (press Enter for 16): ") or "16")
        except ValueError:
            print("Invalid input. Using default (16).")
            length = 16
    
    # Validate length
    if length < 4:
        print("Password too short. Minimum length is 4. Using 16.")
        length = 16
    
    # Generate multiple passwords
    print(f"\nGenerated passwords ({length} characters):\n")
    for i in range(5):
        password = generate_password(length)
        print(f"{i+1}. {password}")
    
    print("\nTip: Use a password manager to store these securely!")