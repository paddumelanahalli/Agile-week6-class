def formal_greet_unsafe(name, title):
    # No guards, no cleaning, no checks.
    # It assumes the user is perfect.
    return "Greetings, " + title + " " + name

"""
2. Why it is Unsafe (The "Crash" Scenarios)

Scenario A (The Type Crash):
print(formal_greet_unsafe(12345, "Mr."))
Result: TypeError (Python crashes because it can't add a number to a string). The program stops completely.

Scenario B (The Logic Garbage):
print(formal_greet_unsafe("   ", "Dr."))
Result: "Greetings, Dr.    "
QA Note: It "works," but the output is ugly and unprofessional. It passed bad data into our database.

Scenario C (The Missing Case):
print(formal_greet_unsafe("paddu", "prof"))
Result: "Greetings, prof paddu"
QA Note: It looks messy because it didn't enforce .title() capitalization.
"""
def formal_greet(name, title="Mx."):
    # 1. THE TYPE GUARD: Is it a string?
    assert isinstance(name, str), "QA Error: Name must be a string."
    assert isinstance(title, str), "QA Error: Title must be a string."

    # 2. THE CONTENT GUARD: Is it empty?
    clean_name = name.strip()
    assert len(clean_name) > 0, "QA Error: Name cannot be blank."

    # 3. THE LOGIC: Format and Return
    # We use .title() to ensure "paddu" becomes "Paddu"
    return "Greetings, " + title + " " + clean_name.title()

# --- The Pytest for it ---

import pytest

def test_formal_greet_success():
    # Positive Test
    result = formal_greet("paddu", "Prof.")
    assert result == "Greetings, Prof. Paddu"

def test_formal_greet_empty_fail():
    # Negative Test: Should catch the empty string
    with pytest.raises(AssertionError) as excinfo:
        formal_greet("   ")
    assert "Name cannot be blank" in str(excinfo.value)
