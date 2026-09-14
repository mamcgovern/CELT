# Canvas Presence Reports

## Description
This project is a Python-based reporting tool that automates the creation of Canvas Presence reports from institutional course data. It processes a CSV export, organizes and sorts course information, and generates structured Excel workbooks for each college.

The tool is designed to reduce manual data cleanup and improve visibility into missing LMS (Canvas) course sections across departments.

### Key Features
* Imports raw CSV course data
* Automatically maps academic departments to colleges
* Sorts data hierarchically: Department → Course Subject → Course Number → Instructor → Section
* Generates a “Canvas Presence” flag based on LMS section availability
* Splits output into separate Excel files by college
* Creates a formatted Instructions sheet in every file
* Applies Excel formatting:
    * Conditional formatting (missing Canvas sections highlighted)
    * Structured Excel tables
    * Auto-wrapped text and dynamic row sizing
* Includes a simple GUI for:
    * Semester selection
    * Report type selection (Start of Term / Interim / End of Term)
    * File selection

## Understanding the Report

### What This Report Shows
Canvas Presence Reports provide information about which Iowa State University course sections are linked to an active Canvas course shell for the designated semester. Each report is organized by college and sorted by department, course, and then instructor. Sections of the same course are grouped together.

### How To Read the Canvas Presence Column
'Yes' in the Canvas Presence column means the section is enrolled in an active Canvas shell.  
'No' does not automatically mean that the section has not been enrolled in an active Canvas course. Before drawing any conclusions, check other columns, since a 'No' may simply reflect an exemption.

### Understanding Exemptions
Exemptions are determined by the department when course section records are entered in Workday, and may include:

#### 1. Non-Grade Control Sections (e.g., Labs and Recitations)
"Some sections, such as labs and recitations, are designated as non-grade control, meaning they cannot submit grades. These sections are paired with a grade control section, which is used for grade submission.  
Non-grade control sections showing 'No' for Canvas presence may be enrolled a Canvas course shell that was created for their associated grade-control section. To check if this is the case:  
     a) Find all sections of the same course (they are grouped together). Check the section_type column for each section.  
     b) Locate the section marked as grade control and check whether it shows 'Yes' for Canvas presence.  
     c) Compare the student_count for the grade control section against the combined enrollment in the non-grade control sections. If the numbers match, then students from non-grade control sections are enrolled in a Canvas course shell via the paired grade-control section."  

#### 2. Low-Enrollment Courses
Instructors of courses with very few students, such as dissertation research credits for doctoral candidates, independent studies, etc., may choose not to create a Canvas course shell.
If a section shows 'No' in the Canvas Presence column and the student_count is very low (e.g., 1–3 students), this is likely the reason.

#### 3. Half-Semester Courses That Haven't Started Yet
If this report was generated before the second half of the semester begins, Canvas shells for half-semester courses may not yet been created. If a section shows 'No' in the Canvas Presence column, check the start_date column. If the course starts later in the semester, the Canvas shell may be created closer to that date.

### Data Analysis is Key
Each college should review the report to identify which courses have an active Canvas presence. Pay close attention to the start_date, student_count, grade_control, and section_type columns, as they are essential to interpreting Canvas presence correctly.

### Importance of Canvas Presence
The Learning Management System helps students keep track of their grades and easily and conveniently access course materials. To promote faculty use of this best practice, the Office of the Senior Vice President and Provost requires all courses to maintain an active presence in Canvas. For assistance with Canvas troubleshooting, ISU Admin Tools, course design, or other pedagogical questions, contact celt-help@iastate.edu.

### Need help?
If you have questions about the report or how to interpret it, please reach out to celt-help@iastate.edu. In your message, include a description of the issue, and we will be able to double-check your interpretation.
## Resources
* Canvas Presence Reports KBA https://iastate.service-now.com/kb_view.do?sysparm_article=KB0024222
* Canvas Presence Report Automation KBA https://iastate.service-now.com/kb_view.do?sysparm_article=KB0025152