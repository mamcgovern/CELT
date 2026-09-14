from datetime import datetime, timedelta


# Schedule milestones
MILESTONES = [
    ("Send initial email", 0),
    ("Reminder email", 3),
    ("Due date", 4),
    ("Make trainings", 5),
    ("Send email", 6),
    ("Due date for schedule", 7),
]


def get_due_date():
    """Ask the user for the Week 7 due date."""
    while True:
        date_input = input(
            "Enter the due date for the schedule (MM/DD/YYYY): "
        )

        try:
            return datetime.strptime(date_input, "%m/%d/%Y")
        except ValueError:
            print("Invalid date. Please use MM/DD/YYYY.")


def generate_schedule(schedule_due_date):
    """Generate all milestone dates based on the Week 7 due date."""
    schedule = []

    for task, week in MILESTONES:
        weeks_from_start = week
        weeks_before_due = 7 - weeks_from_start

        date = schedule_due_date - timedelta(weeks=weeks_before_due)

        schedule.append({
            "task": task,
            "week": week,
            "date": date
        })

    return schedule


def display_schedule(schedule):
    """Display the generated schedule."""
    print("\nSchedule")
    print("-" * 60)

    for item in schedule:
        formatted_date = item["date"].strftime("%A, %B %d, %Y")

        # Remove the leading zero from the day
        formatted_date = formatted_date.replace(" 0", " ")

        print(f"Week {item['week']}: {item['task']}")
        print(f"        {formatted_date}")
        print()


def main():
    schedule_due_date = get_due_date()
    schedule = generate_schedule(schedule_due_date)

    display_schedule(schedule)


if __name__ == "__main__":
    main()