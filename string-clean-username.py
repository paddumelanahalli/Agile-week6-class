def clean_username(raw_name):
    # Check if the input is actually a string
    assert isinstance(raw_name, str), "QA Error: Input must be a string."

    # Remove extra spaces and fix capitalization
    cleaned = raw_name.strip().title()

    # Check if the name is empty after cleaning
    assert len(cleaned) > 0, "QA Error: Name cannot be empty."

    return cleaned


# Test Cases
print(clean_username("   paddu   "))  # Output: Paddu
print(clean_username("ALAN TURING"))  # Output: Alan Turing
print(clean_username(""))  # Output: Alan Turing
