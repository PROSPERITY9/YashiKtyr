# ABOUT

This is the submission for One Banc's Assignment on MPIN strength validation. 
# PIN-Validator-Yashi

**PIN-Validator-Yashi** is a Python tool that validates the strength of Mobile PINs (MPINs) by detecting commonly used patterns and vulnerabilities linked to demographic information (e.g date of birth, wedding anniversaries). The tool helps identify weak MPINs to improve security in mobile banking apps.

## Key Features
1. **Common MPIN Detection**: Detects weak MPINs like `1234`, `1122`, and other common patterns.
2. **Demographic Weakness Detection**: Identifies MPINs based on personal data, such as birthdates or anniversaries.
3. **Modular Design**: Easily scalable to handle 6-digit MPINs and future enhancements.
4. **Testable**: Includes test cases to validate functionality.

## How It Works
- **MPIN Validation**: `validate_mpin()` checks for commonly used MPINs.
- **Demographic Check**: `handle_demographics()` detects weaknesses based on user’s personal information.
- **Result**: Returns **STRONG** or **WEAK**, with reasons if weak.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/prosperitea/PIN-Validator-Yashi.git
