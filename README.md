# Password Generator

A simple command-line password generator written in Python. Pick a length and get a random password made of letters, numbers, and symbols.

## Features

- Interactive menu (generate a password or quit)
- Custom password length
- Uses uppercase and lowercase letters, digits, and punctuation
- Input validation for non-numeric values and lengths that are too short
- No external dependencies, just the Python standard library

## Requirements

- Python 3.6 or higher

## Usage

1. Save the script as `password_generator.py`.
2. Run it from your terminal:

   ```bash
   python password_generator.py
   ```

3. Choose an option from the menu:

   ```
   1. Make a password
   2. Quit
   ```

4. If you pick `1`, enter the length you want and the password is printed.

## Example

```
------------------------------
   Password Generator
------------------------------

1. Make a password
2. Quit
Pick one: 1
How long should it be? 12
Your password: k#9Tz!qW2@mB

1. Make a password
2. Quit
Pick one: 2
Bye!
```

## How It Works

The `make_password(length)` function builds a pool of characters from `string.ascii_letters`, `string.digits`, and `string.punctuation`. It then picks one character at random from the pool for each position until the password reaches the requested length.

## Rules and Validation

| Input | Result |
| --- | --- |
| Length of 4 or more | Password is generated |
| Length below 4 | Asks for a longer password |
| Non-numeric length | Shows an error and returns to the menu |
| Invalid menu choice | Shows an error and returns to the menu |

## Security Note

This project uses Python's `random` module, which is fine for learning and casual use but is **not cryptographically secure**. For real passwords, replace `random.choice` with `secrets.choice`:

```python
import secrets

pw += secrets.choice(chars)
```

## Possible Improvements

- Option to exclude symbols or ambiguous characters (like `l`, `1`, `O`, `0`)
- Guarantee at least one letter, digit, and symbol in every password
- Copy the password to the clipboard
- Generate multiple passwords at once

## License

Free to use and modify. Add a license of your choice (for example, MIT) if you plan to share this project.
