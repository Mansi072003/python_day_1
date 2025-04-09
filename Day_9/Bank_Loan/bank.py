def check(age, salary, credit_score):
    if age >= 21:
        if age <= 60:
            if salary >= 25000:
                if credit_score >= 700:
                    return "Eligible for bank loan"
                else:
                    return "Not eligible: Credit score too low"
            else:
                return "Not eligible: Salary too low"
        else:
            return "Not eligible: Age is above the allowed limit"
    else:
        return "Not eligible: Age is below the allowed limit"


def main():
    print("Welcome to the Bank Loan Eligibility Checker")
    try:
        age = int(input("Enter your age: "))
        salary = float(input("Enter your monthly salary: "))
        credit_score = int(input("Enter your credit score: "))
        
        result = check(age, salary, credit_score)
        print("\nResult:", result)
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()
