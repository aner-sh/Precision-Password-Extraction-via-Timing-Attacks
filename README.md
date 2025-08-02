# Precision-Password-Extraction-via-Timing-Attacks
This Python script performs statistical inference on HTTP response delays to deduce password characters in a timing attack scenario. By measuring and analyzing the response time of a remote server over multiple request cycles, it identifies the most probable character at each password position based on timing anomalies.

# 🔎 Statistical Inference on Response Delays

A timing attack framework for inferring password characters by analyzing subtle differences in HTTP response times. This tool uses statistical analysis to detect timing anomalies associated with partial password correctness, allowing for character-by-character reconstruction.

---

## 🚀 Overview

This project performs a **statistical timing attack** to extract a password from a remote server by:

1. Sending repeated POST requests with password guesses.
2. Measuring server response time for each character position.
3. Detecting small timing variations statistically to infer correct characters.
4. Constructing the password character by character.

The attack is passive and does **not rely on server error messages** or brute-force enumeration. It exploits the premise that correct guesses cause a slightly longer processing delay.

---

## 🧠 Core Features

- **Custom Character Set**  
  Supports any combination of characters (default: `A-Z`, `a-z`, `0-9`).

- **Position-by-Position Password Recovery**  
  Infers each character independently based on measurable delay differences.

- **Statistical Analysis Over Multiple Cycles**  
  Mitigates noise and outliers by collecting response times across many repetitions (`CYCLES`).

- **Immediate Success Detection**  
  If the server returns a specific success code (e.g., `'1'`), the character is instantly marked as correct.

- **Highly Configurable**  
  Adjust password length, character set, server URL, and number of cycles for different targets or challenges.

---

## 📄 Code Structure

### `measure_response_time(position, char)`
- Sends a POST request with a guess at the given position.
- Returns the response time and server message.
- Replaces all other password characters with `.` as placeholders.

### `find_character_for_position(position)`
- Tries all characters in the character set for one specific password position.
- Collects response times across `CYCLES` to build an average.
- Calculates deviation from the mean to determine the most likely character.
- Returns the character with the highest timing anomaly.

### `break_password()`
- Iterates through each position in the password.
- Uses `find_character_for_position()` to identify the best guess.
- Assembles and prints the full password at the end.

---

## ⚙️ Configuration

Inside the script, you can adjust:

| Variable           | Description                                             |
|--------------------|---------------------------------------------------------|
| `CHAR_SET`         | Set of characters to test (default: alphanumeric)       |
| `PASSWORD_LENGTH`  | Length of the password to crack                         |
| `URL`              | Server base URL to target                               |
| `CYCLES`           | Number of cycles to collect timings (higher = slower)   |

---

## ⚠️ Disclaimer

> This tool is intended **strictly for educational and research purposes**.  
> Do not use it on systems you do not own or have explicit permission to test. Unauthorized access is illegal and unethical.

---
