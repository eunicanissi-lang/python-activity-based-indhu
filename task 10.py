
import re

# Validation rules
EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
REGISTRATION_PATTERN = r"^UNI-\d{4}-[A-Z]{3}$"

# Sample student records
students = [
    {
        "name": "Arun",
        "email": "arun.kumar@example.com",
        "registration_id": "UNI-2025-CSE"
    },
    {
        "name": "Priya",
        "email": "priya@@example.com",
        "registration_id": "UNI-25-CSE"
    },
    {
        "name": "Rahul",
        "email": "rahul.example.com",
        "registration_id": "UNI-2025-123"
    },
    {
        "name": "Sneha",
        "email": "sneha@college",
        "registration_id": "UNI/2025/ECE"
    },
    {
        "name": "Kiran",
        "email": "kiran kumar@example.com",
        "registration_id": "UNI-2025-CSE"
    }
]


def validate_email(email):
    """Validate email and identify common formatting errors."""
    errors = []

    if not email:
        return ["Email is missing."]

    if email.count("@") == 0:
        errors.append("Missing '@' separator.")
    elif email.count("@") > 1:
        errors.append("Multiple '@' separators found.")

    if "@" in email:
        local, domain = email.rsplit("@", 1)

        if not local:
            errors.append("Email username is missing.")

        if not domain:
            errors.append("Email domain is missing.")
        elif "." not in domain:
            errors.append("Domain extension is missing.")

    if email.startswith(".") or email.endswith("."):
        errors.append("Email cannot start or end with a dot.")

    if ".." in email:
        errors.append("Consecutive dots are not allowed.")

    if re.search(r"\s", email):
        errors.append("Whitespace is not allowed.")

    if not re.fullmatch(EMAIL_PATTERN, email):
        if not errors:
            errors.append("Email contains invalid characters or format.")

    return errors


def validate_registration_id(reg_id):
    """Validate registration ID using UNI-YYYY-XXX format."""
    errors = []

    if not reg_id:
        return ["Registration ID is missing."]

    parts = reg_id.split("-")

    if len(parts) != 3:
        errors.append("Expected exactly 3 components separated by hyphens.")
    else:
        prefix, year, department = parts

        if prefix != "UNI":
            errors.append("Prefix must be 'UNI'.")

        if not re.fullmatch(r"\d{4}", year):
            errors.append("Year must contain exactly 4 digits.")

        if not re.fullmatch(r"[A-Z]{3}", department):
            errors.append(
                "Department must contain exactly 3 uppercase letters."
            )

    if not re.fullmatch(REGISTRATION_PATTERN, reg_id):
        if not errors:
            errors.append("Registration ID has an invalid format.")

    return errors


def validate_student(student):
    """Validate all identifiers for one student."""
    email_errors = validate_email(student.get("email", ""))
    id_errors = validate_registration_id(
        student.get("registration_id", "")
    )

    valid = not email_errors and not id_errors

    print("\n" + "-" * 60)
    print(f"Student Name     : {student['name']}")
    print(f"Email             : {student.get('email', '')}")
    print(f"Registration ID   : {student.get('registration_id', '')}")

    if email_errors:
        print("Email Status      : INVALID")
        for error in email_errors:
            print(f"  - {error}")
    else:
        print("Email Status      : VALID")

    if id_errors:
        print("Registration Status: INVALID")
        for error in id_errors:
            print(f"  - {error}")
    else:
        print("Registration Status: VALID")

    print("Overall Status    :", "VALID" if valid else "INVALID")

    return valid


def generate_report(students):
    """Generate summary of valid and invalid records."""
    valid_count = 0
    invalid_count = 0

    print("=" * 60)
    print("STUDENT EMAIL AND IDENTIFIER VALIDATION REPORT")
    print("=" * 60)

    for student in students:
        if validate_student(student):
            valid_count += 1
        else:
            invalid_count += 1

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total students : {len(students)}")
    print(f"Valid records  : {valid_count}")
    print(f"Invalid records: {invalid_count}")


# Run validation
generate_report(students)
