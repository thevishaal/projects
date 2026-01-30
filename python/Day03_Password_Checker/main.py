def validate_password(username, password):
    errors = []

    # Length check 
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    
    # Number check
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one number.")
    
    # Lowecase letter check
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")

    # Uppercase letter check
    if not password[0].isupper():
        errors.append("Password must start with a capital letter.")
    
    # username check (case-insensitive)
    if username.lower() in password.lower():
        errors.append("Password should not contain your username.")

    # special character check
    SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;:',.<>/?"
    if not any(char in SPECIAL_CHARS for char in password):
        errors.append("Password must contain at least one special letter.")

    return errors


username = input("Username: ").strip()
password = input("Create Password: ")

result = validate_password(username, password)

if not result:
    print("✅ Password is STRONG & VALID.")
else:
    print("❌ Password is WEAK.")
    for error in result:
        print("-", error)