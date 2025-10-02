import re
import math
import random
import string
from typing import Dict, List, Tuple

class PasswordAnalyzer:
    def __init__(self):
        self.min_length = 12
        self.common_patterns = [
            r'password', r'admin', r'user', r'login', r'1234', r'qwerty',
            r'abc', r'letmein', r'welcome', r'monkey', r'secret', r'love',
            r'god', r'jesus', r'admin123', r'pass', r'12345', r'666',
            r'777', r'ilove'
        ]
        self.dictionary_words = [
            'apple', 'house', 'book', 'tree', 'sun', 'moon', 'star', 'home',
            'work', 'play', 'dog', 'cat', 'bird', 'fish', 'game', 'life'
        ]
        self.max_charset_size = 26 + 26 + 10 + 15  # lowercase + uppercase + digits + special chars (no spaces)

    def analyze_password(self, password: str, personal_info: List[str] = None) -> Dict[str, any]:
        """
        Analyzes password strength and returns detailed feedback
        Personal_info: List of strings like name, birthdate to check against
        """
        if not password:
            return {
                "score": 0,
                "strength": "Invalid",
                "issues": ["Password cannot be empty"],
                "recommendations": ["Enter a non-empty password"],
                "generated_password": None,
                "entropy": 0,
                "max_entropy": 0
            }

        score = 0
        issues = []
        recommendations = []
        personal_info = personal_info or []
        has_spaces = False

        # Check for spaces
        if ' ' in password:
            has_spaces = True
            issues.append("Password contains spaces")
            recommendations.append("Avoid using spaces in passwords")
            score -= 15

        # Check length
        length_score = min(len(password) * 5, 40)
        score += length_score
        if len(password) < self.min_length:
            issues.append(f"Password is too short ({len(password)} characters)")
            recommendations.append(f"Use at least {self.min_length} characters")

        # Check character variety
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        
        char_types = sum([has_lower, has_upper, has_digit, has_special])
        char_score = char_types * 15
        score += char_score
        
        if char_types < 3:
            issues.append("Limited character variety")
            recommendations.append("Include a mix of uppercase, lowercase, numbers, and special characters")

        # Check for common patterns
        for pattern in self.common_patterns:
            if re.search(pattern, password.lower()):
                issues.append("Contains common pattern or word")
                recommendations.append("Avoid common words or predictable patterns")
                score -= 20
                break

        # Check for dictionary words
        for word in self.dictionary_words:
            if re.search(r'\b' + word + r'\b', password.lower()):
                issues.append("Contains dictionary word")
                recommendations.append("Avoid using common dictionary words")
                score -= 15
                break

        # Check for personal information
        for info in personal_info:
            if info and info.lower() in password.lower():
                issues.append("Contains personal information")
                recommendations.append("Avoid using personal details like name or birthdate")
                score -= 20
                break

        # Check for repeated characters
        if re.search(r'(.)\1{2,}', password):
            issues.append("Contains repeated characters")
            recommendations.append("Avoid repeating the same character multiple times")
            score -= 10

        # Check for sequential characters
        if re.search(r'123|abc|xyz', password.lower()):
            issues.append("Contains sequential characters")
            recommendations.append("Avoid sequential characters like '123' or 'abc'")
            score -= 10

        # Calculate entropy
        charset_size = (26 if has_lower else 0) + (26 if has_upper else 0) + \
                      (10 if has_digit else 0) + (15 if has_special else 0)
        if charset_size > 0:
            entropy = math.log2(charset_size ** len(password))
            entropy_score = min(int(entropy / 2), 30)
            score += entropy_score
        else:
            entropy = 0
            entropy_score = 0

        # Calculate maximum possible entropy
        max_entropy = math.log2(self.max_charset_size ** len(password))

        # Normalize score
        score = max(0, min(score, 100))

        # Determine strength
        if score >= 90:
            strength = "Excellent"
            generated_password = None
        elif score >= 70:
            strength = "Strong"
            generated_password = self.generate_excellent_password()
        elif score >= 50:
            strength = "Moderate"
            generated_password = self.generate_excellent_password()
        elif score >= 30:
            strength = "Weak"
            generated_password = self.generate_excellent_password()
        else:
            strength = "Very Weak"
            generated_password = self.generate_excellent_password()

        return {
            "score": score,
            "strength": strength,
            "issues": issues if issues else ["No major issues detected"],
            "recommendations": recommendations if recommendations else ["Maintain good password practices"],
            "entropy": round(entropy, 2),
            "max_entropy": round(max_entropy, 2),
            "generated_password": generated_password,
            "has_spaces": has_spaces
        }

    def generate_excellent_password(self, length: int = 16) -> str:
        """
        Generates a random password with an Excellent rating, no spaces
        """
        chars = (
            string.ascii_lowercase +
            string.ascii_uppercase +
            string.digits +
            string.punctuation.replace(' ', '')
        )
        
        # Ensure at least one of each required character type
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation.replace(' ', ''))
        ]
        
        # Fill the rest of the password length
        for _ in range(length - 4):
            password.append(random.choice(chars))
        
        # Shuffle the password
        random.shuffle(password)
        return ''.join(password)

    def generate_recommendations(self) -> List[str]:
        """
        Returns general password security recommendations
        """
        return [
            "Use at least 12 characters",
            "Include a mix of uppercase letters, lowercase letters, numbers, and special characters",
            "Avoid common words, phrases, or patterns (e.g., 'password', '1234')",
            "Avoid dictionary words (e.g., 'apple', 'house')",
            "Avoid personal information (e.g., name, birthdate)",
            "Use unique passwords for each account",
            "Consider using a password manager for secure storage",
            "Update passwords regularly but not too frequently",
            "Enable two-factor authentication where possible",
            "Avoid spaces in passwords"
        ]

def main():
    analyzer = PasswordAnalyzer()
    
    # Collect personal information (optional)
    print("Enter personal information to avoid in passwords (or press Enter to skip):")
    name = input("Name: ").strip()
    birthdate = input("Birthdate (e.g., 1990): ").strip()
    personal_info = [info for info in [name, birthdate] if info]
    
    while True:
        password = input("\nEnter a password to analyze (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break
            
        result = analyzer.analyze_password(password, personal_info)
        
        print("\nPassword Analysis:")
        print(f"Strength: {result['strength']} (Score: {result['score']}/100)")
        print(f"Entropy: {result['entropy']} bits (measures password randomness; higher is better; max for length: {result['max_entropy']} bits)")
        if result['has_spaces']:
            print("WARNING: Many systems do not allow spaces in passwords.")
        print("\nIssues:")
        for issue in result['issues']:
            print(f"- {issue}")
        print("\nRecommendations:")
        for rec in result['recommendations']:
            print(f"- {rec}")
        if result['generated_password']:
            print(f"\nSuggested Excellent Password: {result['generated_password']}")
        
        if result['strength'] != "Excellent":
            print("\nGeneral Password Security Tips:")
            for tip in analyzer.generate_recommendations():
                print(f"- {tip}")
        print()

if __name__ == "__main__":
    main()