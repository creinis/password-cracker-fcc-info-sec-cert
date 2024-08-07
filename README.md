## Password Cracker using SHA-1

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
<img src="https://ioflood.com/blog/wp-content/uploads/2023/09/Data-stream-converting-to-hash-Python-hashlib-code-snippets-Python-logo.jpg" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Password Cracker application, follow the instructions in the Setup section below.

## Project Structure

- `password_cracker.py`: Contains the implementation of the SHA-1 password cracking function.
- `main.py`: Entry point to run the password cracking examples and tests.
- `known-salts.txt`: Contains a list of known salts.
- `top-10000-passwords.txt`: Contains a list of the top 10,000 passwords.
- `test_module.py`: Contains unit tests for validating the password cracker.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/password-cracker-fcc-info-sec-cert.git
   cd password-cracker
   ```

2. Run the password cracker script:
   ```bash
   python3 main.py
   ```

## Password Cracker

### Functionality

The Password Cracker application is designed to crack SHA-1 hashed passwords. It supports both salted and unsalted hashes. The function iterates through a list of the top 10,000 passwords, optionally combining them with known salts, and compares the generated hash with the target hash to find a match.

### Functions

#### crack_sha1_hash

This function attempts to crack a given SHA-1 hash by comparing it against precomputed hashes of a list of common passwords. It can optionally use a list of known salts to enhance the cracking process.

### Practical Use Case

The Password Cracker is useful for security professionals and researchers who need to test the strength of hashed passwords by attempting to reverse them using common password lists and known salts.

### Benefits

- **Effective Testing:** Allows for testing password strength and hashing mechanisms.
- **Educational Value:** Provides insight into how password cracking techniques work and the importance of using strong, unique passwords and salts.

### Example Usage

To crack a SHA-1 hash without salts:
```python
import password_cracker

print(password_cracker.crack_sha1_hash('b305921a3723cd5d70a375cd21a61e60aabb84ec'))  # Should return 'sammy123'
```

To crack a SHA-1 hash with salts:
```python
import password_cracker

print(password_cracker.crack_sha1_hash('53d8b3dc9d39f0184144674e310185e41a87ffd5', use_salts=True))  # Should return 'superman'
```

## How to Use

1. Start by running the `main.py` script to see the password cracker in action.
2. Modify the hash inputs in `main.py` to test with different hashes.
3. Explore the `test_module.py` to understand and run the unit tests for validating the functionality.

### Additional Information

- **Dataset:** The application uses `top-10000-passwords.txt` for common passwords and `known-salts.txt` for known salts.
- **Comprehensive Analysis:** The application combines password and salt combinations to ensure thorough testing against the hash.

---
#### This is a FreeCodeCamp Challenge for Information Security Certification
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>