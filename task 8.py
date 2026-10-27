
# Integrated University Fee and Eligibility Audit

# University eligibility rules
MIN_ATTENDANCE = 75
MIN_INTERNAL_MARKS = 40

# Student records
students = {
    "S101": {
        "name": "Arun",
        "total_fee": 50000,
        "fee_paid": 50000,
        "attendance": 85,
        "internal_marks": 75,
        "exam_registered": True
    },
    "S102": {
        "name": "Priya",
        "total_fee": 50000,
        "fee_paid": 35000,
        "attendance": 90,
        "internal_marks": 80,
        "exam_registered": True
    },
    "S103": {
        "name": "Rahul",
        "total_fee": 50000,
        "fee_paid": 50000,
        "attendance": 65,
        "internal_marks": 35,
        "exam_registered": True
    },
    "S104": {
        "name": "Sneha",
        "total_fee": 50000,
        "fee_paid": 50000,
        "attendance": 80,
        "internal_marks": 60,
        "exam_registered": False
    },
    "S105": {
        "name": "Kiran",
        "total_fee": 50000,
        "fee_paid": 30000,
        "attendance": 70,
        "internal_marks": 30,
        "exam_registered": False
    }
}


def audit_student(student_id, record):
    """Check fee, attendance, marks, and exam registration."""

    outstanding = []

    # 1. Fee payment verification
    balance = record["total_fee"] - record["fee_paid"]

    if balance > 0:
        outstanding.append(
            f"Fee pending: Rs. {balance:.2f}"
        )

    # 2. Attendance verification
    if record["attendance"] < MIN_ATTENDANCE:
        outstanding.append(
            f"Low attendance: {record['attendance']}% "
            f"(minimum {MIN_ATTENDANCE}%)"
        )

    # 3. Internal marks verification
    if record["internal_marks"] < MIN_INTERNAL_MARKS:
        outstanding.append(
            f"Insufficient internal marks: "
            f"{record['internal_marks']} "
            f"(minimum {MIN_INTERNAL_MARKS})"
        )

    # 4. Examination registration verification
    if not record["exam_registered"]:
        outstanding.append("Examination registration incomplete")

    # Determine overall eligibility
    eligible = len(outstanding) == 0

    return {
        "student_id": student_id,
        "name": record["name"],
        "fee_balance": balance,
        "attendance": record["attendance"],
        "internal_marks": record["internal_marks"],
        "eligible": eligible,
        "outstanding": outstanding
    }


def generate_report(students):
    """Generate summary and reason-wise audit reports."""

    results = []

    print("=" * 95)
    print("          INTEGRATED UNIVERSITY FEE AND ELIGIBILITY AUDIT")
    print("=" * 95)

    print(
        f"{'ID':<8}{'Name':<12}{'Fee Balance':>14}"
        f"{'Attendance':>13}{'Internal':>11}{'Status':>15}"
    )
    print("-" * 95)

    # Audit each student
    for student_id, record in students.items():
        result = audit_student(student_id, record)
        results.append(result)

        status = "ELIGIBLE" if result["eligible"] else "NOT ELIGIBLE"

        print(
            f"{student_id:<8}{record['name']:<12}"
            f"{result['fee_balance']:>14.2f}"
            f"{result['attendance']:>12}%"
            f"{result['internal_marks']:>11}"
            f"{status:>15}"
        )

    # Reason-wise report
    print("\n" + "=" * 95)
    print("REASON-WISE OUTSTANDING CONDITIONS")
    print("=" * 95)

    reason_counts = {
        "Fee pending": 0,
        "Low attendance": 0,
        "Insufficient internal marks": 0,
        "Examination registration incomplete": 0
    }

    for result in results:
        if result["outstanding"]:
            print(
                f"\n{result['student_id']} - {result['name']}"
            )

            for reason in result["outstanding"]:
                print(f"  - {reason}")

                if reason.startswith("Fee pending"):
                    reason_counts["Fee pending"] += 1
                elif reason.startswith("Low attendance"):
                    reason_counts["Low attendance"] += 1
                elif reason.startswith("Insufficient internal marks"):
                    reason_counts["Insufficient internal marks"] += 1
                elif reason.startswith("Examination registration"):
                    reason_counts[
                        "Examination registration incomplete"
                    ] += 1

    # Overall summary
    eligible_count = sum(
        result["eligible"] for result in results
    )
    ineligible_count = len(results) - eligible_count
    total_balance = sum(
        result["fee_balance"] for result in results
    )

    print("\n" + "=" * 95)
    print("AUDIT SUMMARY")
    print("=" * 95)

    print(f"Total students       : {len(results)}")
    print(f"Eligible students    : {eligible_count}")
    print(f"Not eligible         : {ineligible_count}")
    print(f"Total pending fees   : Rs. {total_balance:.2f}")

    print("\nOutstanding Conditions by Category:")

    for reason, count in reason_counts.items():
        print(f"{reason:<40}: {count} student(s)")

    print("=" * 95)


# Run the integrated audit
generate_report(students)
