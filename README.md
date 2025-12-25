# StaffManager Pro: HR Staff Management System
University Project (PROGRAMMING IN PYTHON - Midterm)

StaffManager Pro: HR Staff Management System
StaffManager Pro is a lightweight HR management system built with FastAPI and a Python CLI
client, using simple text files for storage. It provides essential HR operations through a clean API and
an interactive client interface.

Implemented Features Overview :
1. Core Authentication
Secure Login: Users authenticate against records in users.txt
Initial Setup: Automatically creates a default admin user (admin/1234) if none exists

2. Department Management (CRUD)
Complete Create, Read, Update, Delete operations for departments
List view displayed as a formatted table with headers

3. Staff Management (Comprehensive)
Add, Update, Delete staff records (ID, Name, Department ID, Position, Salary)
Case-insensitive name search
Salary adjustment (increase/decrease with negative salary protection)
Staff promotion (position update)
All list and search results shown in clean, aligned tables with column headers

4. Attendance Tracking
Record daily Present/Absent status for any staff member
View complete attendance history for a staff ID in formatted summary

5. Client Interface
Menu-driven console application
Clear, readable output with proper table formatting
No direct file access from client - all operations via API
