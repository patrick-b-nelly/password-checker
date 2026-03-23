from analyzer import password strength checker
password = input("Enter password: ")
strength, feedback = password strength checker(password)
print("\n=== Password Strength Analysis ==")
print(f"Strength Level: {strength}")
if feedback:
print("\nRecommendations to improve your password:")
for tip in feedback:
 print(f"- {tip}")
else:
print("\nYour password meets strong security standards.")
