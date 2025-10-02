# Password Strength Analyzer

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)

A comprehensive, interactive command-line tool written in Python to analyze the strength of passwords. It provides a detailed report including a strength score, an entropy calculation, identified weaknesses, and actionable recommendations. If a password is found to be weak, the tool can also suggest a randomly generated, secure alternative.

## Features

* **Score-Based Analysis:** Rates passwords on a scale of 0-100 based on various criteria.
* **Qualitative Ratings:** Classifies passwords from "Very Weak" to "Excellent".
* **Entropy Calculation:** Measures the password's randomness in bits using the Shannon entropy formula, providing a quantitative measure of its unpredictability.
* **Detailed Feedback:** Identifies specific issues such as:
    * Insufficient length
    * Lack of character variety (uppercase, lowercase, numbers, symbols)
    * Inclusion of common patterns (e.g., 'password', '1234')
    * Use of dictionary words
    * Presence of personal information (e.g., name, birthdate)
    * Repeated or sequential characters (e.g., 'aaa', 'abc')
* **Secure Password Generation:** Suggests a strong, randomly generated 16-character password if the user's input is not "Excellent".
* **Zero Dependencies:** Runs using only the Python standard library. No `pip install` required!
* **Interactive CLI:** Easy-to-use command-line interface for testing multiple passwords in a single session.

## How It Works

The analyzer evaluates passwords using a multi-faceted approach:

1.  **Scoring System:** A password starts with a base score which is then adjusted.
    * **Positive points** are awarded for length, character variety, and high entropy.
    * **Negative points** are deducted for weaknesses like using common patterns, dictionary words, personal info, repeated characters, or containing spaces.
2.  **Entropy Calculation:** The tool calculates the password's entropy, which measures its unpredictability. The formula used is **Shannon Entropy**:
    $$ H = L \times \log_2(N) $$
    Where:
    -   $H$ is the entropy in bits.
    -   $L$ is the password length.
    -   $N$ is the number of possible characters in the character set used (e.g., 26 for lowercase, 26 for uppercase, 10 for digits, etc.).
    A higher entropy value indicates a more secure and less predictable password.

## Installation

This tool has no external dependencies, making installation incredibly simple.

1.  **Ensure you have Python 3.7+ installed.**

2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Password-Strength-Analyzer.git](https://github.com/your-username/Password-Strength-Analyzer.git)
    cd Password-Strength-Analyzer
    ```
    That's it! You are ready to run the tool.

## Usage

Run the script from your terminal. Let's assume you've named the file `password_analyzer.py`.

```bash
python password_analyzer.py
```

The tool will first ask for optional personal information to check against. You can skip this by pressing Enter. Then, you can enter passwords to analyze in a loop.

### Example Session

```
Enter personal information to avoid in passwords (or press Enter to skip):
Name: John
Birthdate (e.g., 1990): 1995

Enter a password to analyze (or 'quit' to exit): password123

Password Analysis:
Strength: Very Weak (Score: 10/100)
Entropy: 43.19 bits (measures password randomness; higher is better; max for length: 73.1 bits)

Issues:
- Password is too short (11 characters)
- Contains common pattern or word
- Contains sequential characters

Recommendations:
- Use at least 12 characters
- Avoid common words or predictable patterns
- Avoid sequential characters like '123' or 'abc'

Suggested Excellent Password: F!i2<s@oY8p#Hj*V

General Password Security Tips:
- Use at least 12 characters
- Include a mix of uppercase letters, lowercase letters, numbers, and special characters
- Avoid common words, phrases, or patterns (e.g., 'password', '1234')
- ... (and so on)

Enter a password to analyze (or 'quit' to exit): F!i2<s@oY8p#Hj*V

Password Analysis:
Strength: Excellent (Score: 100/100)
Entropy: 101.44 bits (measures password randomness; higher is better; max for length: 101.44 bits)

Issues:
- No major issues detected

Recommendations:
- Maintain good password practices

Enter a password to analyze (or 'quit' to exit): quit
```

## Security and Privacy Disclaimer

This tool performs all analysis **locally on your machine**. No password or personal information is ever sent over the network. However, as a general security practice, avoid entering highly sensitive production passwords into any application you do not fully control and trust.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
