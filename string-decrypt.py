def generate_cipher_map(shift, decrypt=False):
    # DEFENSIVE GUARD: Ensure shift is a valid integer 0-25
    assert isinstance(shift, int), "QA Error: Shift must be an integer."
    assert 0 <= shift < 26, "QA Error: Shift must be between 0 and 25."

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Using Slicing to create the shifted version
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # If decrypt is True, we map Shifted -> Normal
    # If decrypt is False, we map Normal -> Shifted
    if decrypt:
        return dict(zip(shifted_alphabet, alphabet))
    else:
        return dict(zip(alphabet, shifted_alphabet))


def process_message(message, cipher_map):

    # DEFENSIVE GUARD: Ensure message is a string
    assert isinstance(message, str), "QA Error: Message must be a string."

    # Analysis using a SET (to check for unique characters)
    unique_chars = set(message.lower().replace(" ", ""))
    if len(unique_chars) > 10:
        print("--- QA NOTE: High Entropy Message (More than 10 unique chars) ---")

    result = []
    for char in message.lower():
        # Look up character in our Dictionary map
        if char in cipher_map:
            result.append(cipher_map[char])
        else:
            # Keep spaces, numbers, and punctuation as they are
            result.append(char)

    # Professional way to turn a list back into a string
    return "".join(result)

if __name__ == "__main__":
    print("=== Paddu's Secure Messaging Tool ===")

    try:
        # 1. SETTINGS
        secret_shift = 3
        original_text = "Hello UCSC Agile Students!"

        # 2. ENCRYPTION PHASE
        encryption_map = generate_cipher_map(secret_shift, decrypt=False)
        encrypted_msg = process_message(original_text, encryption_map)

        print("Original:  " + original_text)
        print("Encrypted: " + encrypted_msg)

        print("-" * 30)

        # 3. DECRYPTION PHASE
        decryption_map = generate_cipher_map(secret_shift, decrypt=True)
        decrypted_msg = process_message(encrypted_msg, decryption_map)

        print("Decrypted: " + decrypted_msg)

        # 4. TESTING A DEFENSIVE GUARD (Uncomment to see it work)
        # process_message(12345, encryption_map)

    except AssertionError as e:
        print("STOP! Defensive Guard Triggered: " + str(e))
