import redef check_password(password):
score = 0
feedback = []
if len(password) >= 8:
score += 1
else:
feedback.append("Password should be at least 8 characters")
if re.search(r"[A-Z]", password):
score += 1
else:
feedback.append("Add uppercase letters")
if re.search(r"[a-z]", password):
score += 1
else:
feedback.append("Add lowercase letters")
if re.search(r"[0-9]", password):
score += 1
else:
feedback.append("Add numbers")
if re.search(r"[@$!%*?&]", password):
score += 1
else:
feedback.append("Add special characters")
if score <= 2:
strength = "Weak"
elif score <= 4:
strength = "Moderate"
else:
strength = "Strong"
return strength, feedback
password = input("Enter password: ")
strength, feedback = check_password(password)
print("\nPassword Strength:", strength)
print("Suggestions:")
for tip in feedback:
    print("-", tip)
