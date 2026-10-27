
from datetime import datetime

# Course schedules represented as strings
courses = {
    "Python": "Monday 09:00 10:00 R101",
    "Maths": "Monday 09:30 10:30 R102",
    "Physics": "Tuesday 10:00 11:00 R103"
}

# Unavailable rooms
unavailable_rooms = ["R103", "R105"]


def parse_schedule(schedule):
    """Convert a schedule string into a tuple."""
    day, start, end, room = schedule.split()
    return (day, start, end, room)


def time_to_minutes(time_str):
    """Convert HH:MM into minutes."""
    time_obj = datetime.strptime(time_str, "%H:%M")
    return time_obj.hour * 60 + time_obj.minute


def has_time_overlap(course1, course2):
    """Check whether two courses overlap in time."""
    day1, start1, end1, room1 = course1
    day2, start2, end2, room2 = course2

    if day1 != day2:
        return False

    start1 = time_to_minutes(start1)
    end1 = time_to_minutes(end1)
    start2 = time_to_minutes(start2)
    end2 = time_to_minutes(end2)

    return start1 < end2 and start2 < end1


def detect_conflicts(courses):
    """Detect overlapping courses and unavailable rooms."""
    schedules = {
        name: parse_schedule(schedule)
        for name, schedule in courses.items()
    }

    names = list(schedules.keys())

    print("=== TIMETABLE CONFLICT REPORT ===")

    # Check overlapping course periods
    overlap_found = False

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            course1 = schedules[names[i]]
            course2 = schedules[names[j]]

            if has_time_overlap(course1, course2):
                print(
                    f"Time Conflict: {names[i]} and "
                    f"{names[j]} have overlapping periods."
                )
                overlap_found = True

    if not overlap_found:
        print("No overlapping course periods.")

    # Check unavailable rooms
    room_conflict_found = False

    for name, schedule in schedules.items():
        if schedule[3] in unavailable_rooms:
            print(
                f"Room Conflict: {name} is assigned to "
                f"unavailable room {schedule[3]}."
            )
            room_conflict_found = True

    if not room_conflict_found:
        print("No unavailable room assignments.")

    return not overlap_found and not room_conflict_found


def validate_timetable(proposed_courses):
    """Validate the proposed timetable."""
    print("\n=== TIMETABLE VALIDATION ===")

    if detect_conflicts(proposed_courses):
        print("Result: Timetable is VALID.")
        return True
    else:
        print("Result: Timetable is INVALID.")
        return False


# Example proposed timetable
proposed_timetable = {
    "Python": "Monday 09:00 10:00 R101",
    "Maths": "Monday 09:30 10:30 R102",
    "Physics": "Tuesday 10:00 11:00 R103"
}

validate_timetable(proposed_timetable)
