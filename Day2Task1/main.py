import re

def is_valid_student_id(student_id):
    pattern = r"^\d{2}-\d{5}$"
    return bool(re.match(pattern, student_id))

# Test the function
student_ids = ["15-00041", "99-12345", "123-4567", "1A-23456", "12-3456A"]
for sid in student_ids:
    print(f"{sid}: {is_valid_student_id(sid)}")
