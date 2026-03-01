def mirror_cipher(text):
    # Type and length checks
    assert isinstance(text, str), "QA Error: Input must be a string."
    assert len(text) > 0, "QA Error: Message is empty."

    # Reverse the string
    reversed_text = text[::-1]

    # Shift the first letter by 1
    first_char = reversed_text[0]
    shifted_char = chr(ord(first_char) + 1)

    # Re-attach the rest of the string
    return shifted_char + reversed_text[1:]


# Test Case: "Paddu" -> "uddaP" -> "vddaP"
print(mirror_cipher("Paddu"))
