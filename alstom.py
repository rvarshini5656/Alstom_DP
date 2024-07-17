import re

def extract_text1(input_string, start_word):
    # Regex pattern to match text after the specified start_word and colon
    pattern = fr'{start_word}\s*:\s*(.*)'
    match = re.search(pattern, input_string)
    # Check if a match is found
    if match:
        # Extract the matched text and strip any leading/trailing whitespace
        extracted_text = match.group(1).strip()
        return extracted_text
    else:
        return None

# Example usage
input_string = "Name: Graham Gogan\nPosition: Design engineer\nCompany: Alstom"
start_word = "Position"

result = extract_text1(input_string, start_word)
print("Extracted text:", result)
