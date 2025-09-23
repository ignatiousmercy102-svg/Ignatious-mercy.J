import re

def check_password(pwd):
    score = 0
    feedback = []

    # Length
    if len(pwd) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # Character types
    if re.search(r'[a-z]', pwd):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
    if re.search(r'[A-Z]', pwd):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
    if re.search(r'\d', pwd):
        score += 1
    else:
        feedback.append("Add numbers.")
    if re.search(r'[^A-Za-z0-9]', pwd):
        score += 1
    else:
        feedback.append("Add special characters (!,@,#,$, etc.).")

    # Strength labels
    labels = ["Very Weak", "Weak", "Okay", "Good", "Strong", "Excellent"]
    label = labels[score]

    return score, label, feedback

if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    pwd = input("Enter a password: ")
    score, label, feedback = check_password(pwd)

    print(f"\nStrength: {label} (Score: {score}/5)")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(" -", f)
    else:
        print("✅ Your password looks strong!")
