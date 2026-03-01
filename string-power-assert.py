import pytest

#Test 1: The Type Shield (Integer vs. String)
# Goal: Stop the program if the user passes a number where a name should be.
def test_type_shield():
    print("Running Test 1: Type Shield...")
    user_input = 12345  # This should be a string!
    try:
        assert isinstance(user_input, str), "CRITICAL: Input must be text, not a number!"
        print("Test 1 Failed: It let a number through!")
    except AssertionError as e:
        print("Test 1 Success: Caught the bad type -> " + str(e))

# Test 2: The "Empty Space" Trap
#Goal: Catch users who try to bypass a 'Required' field by just hitting the spacebar.
def test_empty_logic():
    print("\nRunning Test 2: Empty Space Trap...")
    username = "      "
    try:
        assert len(username.strip()) > 0, "VALIDATION ERROR: Field cannot be empty or just spaces."
        print("Test 2 Failed: It allowed a blank name!")
    except AssertionError as e:
        print("Test 2 Success: Caught the empty string -> " + str(e))

# Test 3: The Boundary Guard (Shift Range)
#Goal: In our Cipher, the shift must be 0-25. Let's see what happens if we try a shift of 100.
def test_boundary_check():
    print("\nRunning Test 3: Boundary Guard...")
    bad_shift = 100
    try:
        assert 0 <= bad_shift < 26, "LOGIC ERROR: Shift must be between 0 and 25."
        print("Test 3 Failed: It allowed an impossible shift!")
    except AssertionError as e:
        print("Test 3 Success: Caught the out-of-range shift -> " + str(e))

#Test 4: The Format Enforcer (Email)
# Goal: Ensure a string contains a specific character before processing it.
def test_email_format():
    print("\nRunning Test 4: Format Enforcer...")
    email = "paddu_at_ucsc.edu" # Missing the @ symbol
    try:
        assert "@" in email, "FORMAT ERROR: Missing the @ symbol in email."
        print("Test 4 Failed: It accepted a broken email!")
    except AssertionError as e:
        print("Test 4 Success: Caught the missing @ -> " + str(e))

# Test 5: The Membership Check (Forbidden Characters)
# Goal: Stop the program if a "Secret Key" contains characters that aren't allowed.
def test_forbidden_chars():
    print("\nRunning Test 5: Forbidden Characters...")
    secret_key = "Pass123!" # We don't want symbols in this specific key
    forbidden = "!"
    try:
        assert forbidden not in secret_key, "SECURITY ERROR: Forbidden symbol '!' detected."
        print("Test 5 Failed: It allowed the forbidden symbol!")
    except AssertionError as e:
        print("Test 5 Success: Caught the illegal character -> " + str(e))

# Test 6: The "Mirror" Logic Verification
# Goal: A positive test to prove the logic actually works when the data is correct.
def test_logic_verification():
    print("\nRunning Test 6: Logic Verification...")
    # Does 'a' shifted by 1 actually become 'b'?
    alphabet = "abc"
    shifted = alphabet[1:] + alphabet[:1] # becomes "bca"
    try:
        assert shifted[0] == "b", "MATH ERROR: Shift logic is incorrect."
        print("Test 6 Success: Logic verified! 'a' shifted to 'b'.")
    except AssertionError as e:
        print("Test 6 Failed: The math is wrong -> " + str(e))

if __name__ == "__main__":
    # This calls the pytest engine directly from your code
    import pytest
    pytest.main([__file__])
