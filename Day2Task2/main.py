import re

def is_valid_variable_name(var_name):
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return bool(re.match(pattern, var_name))

# Test the function
variable_names = ["_validName", "valid_name1", "2invalid", "invalid-name", "AnotherValid_Name"]
for name in variable_names:
    print(f"{name}: {is_valid_variable_name(name)}")
