
# University Academic Progression Audit

PASS_MARK = 40
MIN_ATTENDANCE = 75
REQUIRED_SUBJECTS = 4

# Student academic records
students = {
    "S101": {
        "name": "Arun",
        "semester_marks": {
            "Python": 75,
            "Mathematics": 65,
            "Physics": 32,
            "English": 80
        },
        "attendance": {
            "Python": 90,
            "Mathematics": 80,
            "Physics": 70,
            "English": 85
        },
        "prerequisites": {
            "Python": True,
            "Mathematics": True,
            "Physics": True,
            "English": True
        }
    },

    "S102": {
        "name": "Priya",
        "semester_marks": {
            "Python": 85,
            "Mathematics": 78,
            "Physics": 72,
            "English": 88
        },
        "attendance": {
            "Python": 95,
            "Mathematics": 90,
            "Physics": 85,
            "English": 92
        },
        "prerequisites": {
            "Python": True,
            "Mathematics": True,
            "Physics": True,
            "English": True
        }
    },

    "S103": {
        "name": "Rahul",
        "semester_marks": {
            "Python": 55,
            "Mathematics": 35,
            "Physics": 45,
            "English": 60
        },
        "attendance": {
            "Python": 80,
            "Mathematics": 78,
            "Physics": 82,
            "English": 65
        },
        "prerequisites": {
            "Python": True,
            "Mathematics": False,
            "Physics": True,
            "English": True
        }
    }
}


def audit_student(student_id, record):
    """Audit marks, attendance, and prerequisites."""

    outstanding = []
    passed_subjects = 0
    total_subjects = len(record["semester_marks"])

    print("\n" + "=" * 55)
    print(f"Student ID   : {student_id}")
    print(f"Student Name : {record['name']}")
    print("=" * 55)

    print(
        f"{'Subject':<16}{'Marks':>8}"
        f"{'Attendance':>13}{'Result':>12}"
    )
    print("-" * 55)

    for subject, marks in record["semester_marks"].items():
        attendance = record["attendance"].get(subject)
        prerequisite_done = record["prerequisites"].get(subject)

        issues = []

        # Validate marks
        if marks < PASS_MARK:
            issues.append("Failed marks")
            outstanding.append(f"{subject}: Minimum {PASS_MARK} marks required")

        # Validate attendance
        if attendance is None:
            issues.append("Attendance missing")
            outstanding.append(f"{subject}: Attendance record missing")
        elif attendance < MIN_ATTENDANCE:
            issues.append("Low attendance")
            outstanding.append(
                f"{subject}: Attendance must be at least "
                f"{MIN_ATTENDANCE}%"
            )

        # Validate prerequisite completion
        if prerequisite_done is not True:
            issues.append("Prerequisite incomplete")
            outstanding.append(
                f"{subject}: Prerequisite completion required"
            )

        # A subject passes only if every condition is met
        if not issues:
            result = "PASS"
            passed_subjects += 1
        else:
            result = " / ".join(issues)

        attendance_text = (
            f"{attendance}%" if attendance is not None else "Missing"
        )

        print(
            f"{subject:<16}{marks:>8}"
            f"{attendance_text:>13}{result:>12}"
        )

    # Determine progression eligibility
    print("-" * 55)
    print(f"Subjects cleared: {passed_subjects}/{total_subjects}")

    if passed_subjects == total_subjects and not outstanding:
        print("Progression Status: ELIGIBLE")
    else:
        print("Progression Status: NOT ELIGIBLE")
        print("\nOutstanding Requirements:")

        for requirement in outstanding:
            print(f"- {requirement}")


def run_progression_audit(students):
    """Audit all student academic records."""

    print("UNIVERSITY ACADEMIC PROGRESSION AUDIT")

    for student_id, record in students.items():
        audit_student(student_id, record)


# Execute the audit
run_progression_audit(students)
