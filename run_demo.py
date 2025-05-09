from main.mpin_validator import MPINValidator
from main.demographics_handler import DemographicsHandler

def main():
    print("🔐 Welcome to MPIN Strength Checker Demo\n")

    # Sample demographic data
    dob = "1998-02-01"
    spouse_dob = "1998-03-05"
    anniversary = "2022-06-15"

    # Initialize demographics handler
    demographics = DemographicsHandler(dob, spouse_dob, anniversary)

    # User input with validation for 4 or 6 digit MPIN
    while True:
        mpin = input("Enter your 4 or 6 digit MPIN: ")
        if mpin.isdigit() and len(mpin) in [4, 6]:
            break  # Exit the loop if the input is valid
        else:
            print("❌ Invalid MPIN. Please enter a 4 or 6 digit number.")

    # Validate MPIN
    validator = MPINValidator(mpin, demographics)
    result = validator.validate_mpin()

    # Output the result
    print("\n✅ Validation Result:")
    print(f"Strength: {result['strength']}")
    if result['reasons']:
        print("Reasons for weakness:")
        for reason in result['reasons']:
            print(f" - {reason}")
    else:
        print("This is a strong MPIN. Good job! 🎉")

if __name__ == "__main__":
    main()
