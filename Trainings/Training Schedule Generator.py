import os
import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox

from tkcalendar import DateEntry


MILESTONES = [
    {
        "task": "Send Initial Email",
        "week": 0,
        "description": "Send the initial email to CELT-CDQ asking them to fill out the training schedule for the upcoming semester"
    },
    {
        "task": "Reminder Email",
        "week": 3,
        "description": "Send a reminder to CELT-CDQ members who have not yet completed the required information."
    },
    {
        "task": "Due Date",
        "week": 4,
        "description": "Deadline for CELT-CDQ members to submit their training information."
    },
    {
        "task": "Make Trainings",
        "week": 5,
        "description": "Create the teams meetings for the trainings based on the information submitted by CELT-CDQ members."
    },
    {
        "task": "Send Email",
        "week": 6,
        "description": "Send CELT central (Linds, Lisa, Krista) an email with their completed training information and any next steps."
    },
    {
        "task": "Due Date for Schedule",
        "week": 7,
        "description": "Final deadline for the training schedule to be completed and ready for the upcoming term."
    },
]


def format_date(date):
    """Format a date without a leading zero on the day."""
    return date.strftime("%A, %B %d, %Y").replace(" 0", " ")


def generate_schedule(schedule_due_date):
    """Generate all milestone dates based on the Week 7 due date."""
    schedule = []

    for task, week in MILESTONES:
        weeks_before_due = 7 - week
        date = schedule_due_date - timedelta(weeks=weeks_before_due)

        schedule.append({
            "task": task,
            "week": week,
            "date": date
        })

    return schedule


def create_schedule_file(semester, schedule):
    """Create the semester folder and formatted schedule.txt file."""

    script_folder = os.path.dirname(os.path.abspath(__file__))
    folder_name = semester.strip()
    folder_path = os.path.join(script_folder, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, "schedule.txt")

    first_date = schedule[0]["date"]
    final_date = schedule[-1]["date"]

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("=" * 45 + "\n")
        file.write("           TRAINING SCHEDULE\n")
        file.write(f"           {semester.upper()}\n")
        file.write("=" * 45 + "\n")
        file.write("\n")

        file.write(
            f"Schedule Due Date: {format_date(final_date)}\n"
        )
        file.write("\n")

        file.write("-" * 45 + "\n")
        file.write("AT-A-GLANCE TIMELINE\n")
        file.write("-" * 45 + "\n")
        file.write("\n")

        file.write(
            f"{'Week':<7}"
            f"{'Date':<27}"
            f"Task\n"
        )

        file.write(
            f"{'-' * 5:<7}"
            f"{'-' * 24:<27}"
            f"{'-' * 30}\n"
        )

        for item in schedule:
            date_text = item["date"].strftime("%A, %B %d")
            date_text = date_text.replace(" 0", " ")

            file.write(
                f"{item['week']:<7}"
                f"{date_text:<27}"
                f"{item['task']}\n"
            )

        file.write("\n")

        file.write("-" * 45 + "\n")
        file.write("DETAILED TIMELINE\n")
        file.write("-" * 45 + "\n")
        file.write("\n")

        for item in schedule:
            file.write(f"Week {item['week']}\n")
            file.write(f"{item['task']}\n")
            file.write(f"{format_date(item['date'])}\n")
            file.write("\n")

        file.write("-" * 45 + "\n")
        file.write("SUMMARY\n")
        file.write("-" * 45 + "\n")
        file.write("\n")

        file.write("First Action:\n")
        file.write(f"{format_date(first_date)}\n")
        file.write("\n")

        file.write("Final Due Date:\n")
        file.write(f"{format_date(final_date)}\n")
        file.write("\n")

        file.write("Timeline:\n")
        file.write("7 weeks\n")

    return file_path


def generate_button_clicked():
    """Generate the schedule when the button is clicked."""

    semester = semester_entry.get().strip()

    if not semester:
        messagebox.showerror(
            "Missing Semester",
            "Please enter a semester, such as Fall 2026."
        )
        return

    schedule_due_date = due_date_picker.get_date()

    schedule_due_datetime = datetime.combine(
        schedule_due_date,
        datetime.min.time()
    )

    schedule = generate_schedule(schedule_due_datetime)

    file_path = create_schedule_file(
        semester,
        schedule
    )

    messagebox.showinfo(
        "Schedule Created",
        f"Your schedule has been created successfully.\n\n"
        f"Folder: {semester}\n"
        f"File: schedule.txt\n\n"
        f"Location:\n{file_path}"
    )


# --------------------------------------------------
# Main Window
# --------------------------------------------------

root = tk.Tk()
root.title("Training Schedule Generator")
root.geometry("500x350")
root.resizable(False, False)


# --------------------------------------------------
# Title
# --------------------------------------------------

title_label = tk.Label(
    root,
    text="Training Schedule Generator",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=(30, 10))


# --------------------------------------------------
# Description
# --------------------------------------------------

description_label = tk.Label(
    root,
    text="Enter the semester and schedule due date.",
    font=("Arial", 11)
)
description_label.pack(pady=(0, 25))


# --------------------------------------------------
# Semester
# --------------------------------------------------

semester_frame = tk.Frame(root)
semester_frame.pack(pady=10)

semester_label = tk.Label(
    semester_frame,
    text="Semester:",
    font=("Arial", 11)
)
semester_label.grid(
    row=0,
    column=0,
    padx=(0, 10)
)

semester_entry = tk.Entry(
    semester_frame,
    width=25,
    font=("Arial", 11)
)
semester_entry.grid(
    row=0,
    column=1
)

semester_entry.insert(
    0,
    "Fall 2026"
)


# --------------------------------------------------
# Due Date
# --------------------------------------------------

due_date_frame = tk.Frame(root)
due_date_frame.pack(pady=10)

due_date_label = tk.Label(
    due_date_frame,
    text="Due Date for Schedule:",
    font=("Arial", 11)
)
due_date_label.grid(
    row=0,
    column=0,
    padx=(0, 10)
)

due_date_picker = DateEntry(
    due_date_frame,
    width=18,
    font=("Arial", 11),
    date_pattern="mm/dd/yyyy",
    borderwidth=1,
)

due_date_picker.grid(
    row=0,
    column=1
)

# Configure the calendar popup after it is created.
calendar = due_date_picker._calendar

calendar.configure(
    foreground="#ffffff",
    background="#2b2b2b",
    headersforeground="#ffffff",
    headersbackground="#3a3a3a",
    selectforeground="#ffffff",
    selectbackground="#0078d7",
    normalforeground="#ffffff",
    normalbackground="#2b2b2b",
    weekendforeground="#ffffff",
    weekendbackground="#2b2b2b",
    othermonthforeground="#aaaaaa",
    othermonthbackground="#2b2b2b",
    othermonthweforeground="#aaaaaa",
    othermonthwebackground="#2b2b2b",
)


# --------------------------------------------------
# Generate Button
# --------------------------------------------------

generate_button = tk.Button(
    root,
    text="Generate Schedule",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    command=generate_button_clicked
)

generate_button.pack(
    pady=35
)


# --------------------------------------------------
# Start Application
# --------------------------------------------------

root.mainloop()