import re

def find_upper_lower_sequences(text):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, text)

# Test the function
sample_text = "Hello World, this is a Test String with Upper and lower Cases."
sequences = find_upper_lower_sequences(sample_text)
print("Found sequences:", sequences)