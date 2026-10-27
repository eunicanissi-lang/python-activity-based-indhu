
# Hackathon Team Formation and Ranking System

MIN_TEAM_SIZE = 2
MAX_TEAM_SIZE = 4

# Student scores in each round
students = {
    "S101": {"name": "Arun", "scores": [80, 85, 90]},
    "S102": {"name": "Priya", "scores": [90, 80, 85]},
    "S103": {"name": "Rahul", "scores": [75, 80, 85]},
    "S104": {"name": "Sneha", "scores": [85, 90, 80]},
    "S105": {"name": "Kiran", "scores": [70, 75, 80]},
    "S106": {"name": "Meena", "scores": [80, 85, 85]},
    "S107": {"name": "Vijay", "scores": [90, 90, 90]},
    "S108": {"name": "Anu", "scores": [70, 80, 90]}
}

# Team compositions
teams = {
    "Team Alpha": ["S101", "S102"],
    "Team Beta": ["S103", "S104"],
    "Team Gamma": ["S105", "S106"],
    "Team Delta": ["S107", "S108"],
    "Team Omega": ["S101", "S103", "S105", "S106", "S108"]
}


def validate_team(team_name, members):
    """Validate team size and member IDs."""
    errors = []

    if not MIN_TEAM_SIZE <= len(members) <= MAX_TEAM_SIZE:
        errors.append(
            f"Team size must be between {MIN_TEAM_SIZE} "
            f"and {MAX_TEAM_SIZE}; found {len(members)}."
        )

    if len(members) != len(set(members)):
        errors.append("Duplicate student IDs found.")

    for student_id in members:
        if student_id not in students:
            errors.append(f"Unknown student ID: {student_id}")

    return errors


def calculate_team_scores(members):
    """Calculate round-wise and total team scores."""
    valid_members = [
        student_id for student_id in members
        if student_id in students
    ]

    if not valid_members:
        return [], 0

    rounds = len(students[valid_members[0]]["scores"])

    round_totals = [
        sum(students[sid]["scores"][r] for sid in valid_members)
        for r in range(rounds)
    ]

    total = sum(round_totals)
    return round_totals, total


def rank_teams(teams):
    """
    Rank valid teams by:
    1. Highest total score
    2. Highest final-round score
    3. Highest first-round score
    4. Team name in alphabetical order
    """

    results = []
    assigned_students = set()

    print("=" * 75)
    print("HACKATHON TEAM VALIDATION")
    print("=" * 75)

    for team_name, members in teams.items():
        errors = validate_team(team_name, members)

        # Prevent students from joining multiple teams
        for student_id in members:
            if student_id in students and student_id in assigned_students:
                errors.append(
                    f"{student_id} is already assigned to another team."
                )

        if errors:
            print(f"\n{team_name}: INVALID")
            for error in errors:
                print(f"  - {error}")
            continue

        assigned_students.update(members)

        round_totals, total = calculate_team_scores(members)

        results.append({
            "name": team_name,
            "members": members,
            "round_scores": round_totals,
            "total": total
        })

        print(f"\n{team_name}: VALID")
        print(f"Members: {', '.join(members)}")
        print(f"Round-wise scores: {round_totals}")
        print(f"Total score: {total}")

    # Sort valid teams using the predefined tie-break rules
    results.sort(
        key=lambda team: (
            -team["total"],
            -team["round_scores"][-1],
            -team["round_scores"][0],
            team["name"].lower()
        )
    )

    print("\n" + "=" * 75)
    print("FINAL TEAM RANKINGS")
    print("=" * 75)

    print(f"{'Rank':<8}{'Team':<18}{'Round Scores':<22}{'Total':>10}")
    print("-" * 60)

    for rank, team in enumerate(results, start=1):
        print(
            f"{rank:<8}{team['name']:<18}"
            f"{str(team['round_scores']):<22}{team['total']:>10}"
        )

    if not results:
        print("No valid teams available for ranking.")

    return results


# Execute ranking
ranked_teams = rank_teams(teams)
