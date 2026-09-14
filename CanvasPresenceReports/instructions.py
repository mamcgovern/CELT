def get_instructions(college, semester, selected_option):
    return [
        ("TITLE", "Canvas Presence Report", 30),
        ("SUBTITLE", f"{college} - {semester} - {selected_option}", 16),
        
        ("TEXT", "", 16), #blank line
        ("H1", "What This Report Shows", 16),
        ("TEXT", "Canvas Presence Reports provide information about which Iowa State University course sections are linked to an active Canvas course shell for the designated semester. Each report is organized by college and sorted by department, course, and then instructor. Sections of the same course are grouped together.", 35),
        
        ("TEXT", "", 16), #blank line
        ("H1", "How To Read the Canvas Presence Column", 16),
        ("TEXT", "'Yes' in the Canvas Presence column means the section is enrolled in an active Canvas shell.\n'No' does not automatically mean that the section has not been enrolled in an active Canvas course. Before drawing any conclusions, check other columns, since a 'No' may simply reflect an exemption.", 35),
        
        ("TEXT", "", 16), #blank line
        ("H1", "Understanding Exemptions", 16),
        ("TEXT", "Exemptions are determined by the department when course section records are entered in Workday, and may include:", 16),
        
        ("TEXT", "", 16), #blank line
        ("H2", "  1. Non-Grade Control Sections (e.g., Labs and Recitations)", 16),
        ("TEXT", "Some sections, such as labs and recitations, are designated as non-grade control, meaning they cannot submit grades. These sections are paired with a grade control section, which is used for grade submission.\nNon-grade control sections showing 'No' for Canvas presence may be enrolled a Canvas course shell that was created for their associated grade-control section. To check if this is the case:\n     a) Find all sections of the same course (they are grouped together). Check the section_type column for each section.\n     b) Locate the section marked as grade control and check whether it shows 'Yes' for Canvas presence.\n     c) Compare the student_count for the grade control section against the combined enrollment in the non-grade control sections. If the numbers match, then students from non-grade control sections are enrolled in a Canvas course shell via the paired grade-control section.", 96),
        
        ("TEXT", "", 16), #blank line
        ("H2", "  2. Low-Enrollment Courses", 16),
        ("TEXT", "Instructors of courses with very few students, such as dissertation research credits for doctoral candidates, independent studies, etc., may choose not to create a Canvas course shell. If a section shows 'No' in the Canvas Presence column and the student_count is very low (e.g., 1–3 students), this is likely the reason.", 35),
        
        ("TEXT", "", 16), #blank line
        ("H2", "  3. Half-Semester Courses That Haven't Started Yet", 16),
        ("TEXT", "If this report was generated before the second half of the semester begins, Canvas shells for half-semester courses may not yet been created. If a section shows 'No' in the Canvas Presence column, check the start_date column. If the course starts later in the semester, the Canvas shell may be created closer to that date.", 35),
        
        ("TEXT", "", 16), #blank line
        ("H1", "Data Analysis is Key", 16),
        ("TEXT", "Each college should review the report to identify which courses have an active Canvas presence. Pay close attention to the start_date, student_count, grade_control, and section_type columns, as they are essential to interpreting Canvas presence correctly.", 35),
        
        ("TEXT", "", 16), #blank line
        ("H1", "Importance of Canvas Presence", 16),
        ("TEXT", "The Learning Management System helps students keep track of their grades and easily and conveniently access course materials. To promote faculty use of this best practice, the Office of the Senior Vice President and Provost requires all courses to maintain an active presence in Canvas. For assistance with Canvas troubleshooting, ISU Admin Tools, course design, or other pedagogical questions, contact celt-help@iastate.edu.", 35),
        
        ("TEXT", "", 16), #blank line
        ("H1", "Need help?", 16),
        ("TEXT", "If you have questions about the report or how to interpret it, please reach out to celt-help@iastate.edu. In your message, include a description of the issue, and we will be able to double-check your interpretation.", 16),
    ]