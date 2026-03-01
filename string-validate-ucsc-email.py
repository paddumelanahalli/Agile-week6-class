def validate_ucsc_email(email):
    # Check if it is a string
    assert isinstance(email, str), "QA Error: Email must be a string."

    email = email.lower().strip()

    # Check for @ and the correct domain
    assert "@" in email, "Invalid Format: Missing '@'."
    assert email.endswith("ucsc.edu"), "Access Denied: Use @ucsc.edu only."

    # Extract the username
    username = email.split("@")[0]
    assert len(username) > 0, "Invalid Format: No username found."

    return f"Hello, {username}!"


# Test Cases
print(validate_ucsc_email("student@ucsc.edu"))
