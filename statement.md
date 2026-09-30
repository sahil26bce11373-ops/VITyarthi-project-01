# Problem Statement

## Title

Command-Line Password Generator

## Background

Weak and reused passwords are one of the most common causes of compromised accounts. Coming up with strong, random passwords by hand is slow, and people tend to fall back on predictable patterns such as names, dates, or simple words. A small tool that produces random passwords on demand makes this easier.

## Objective

Build a simple, interactive command-line program in Python that generates random passwords of a length chosen by the user.

## Requirements

1. Show a menu with two options: generate a password, or quit.
2. Keep showing the menu until the user chooses to quit.
3. When the user chooses to generate a password, ask for the desired length.
4. Build the password from a mix of:
   - Uppercase and lowercase letters
   - Digits
   - Punctuation symbols
5. Pick each character randomly from that combined pool.
6. Print the generated password.

## Input

| Input | Description |
| --- | --- |
| Menu choice | `1` to generate a password, `2` to quit |
| Password length | A whole number, 4 or greater |

## Output

- The generated password, printed as `Your password: <password>`
- A goodbye message when the user quits
- An error message for any invalid input

## Constraints and Validation

- The password length must be at least 4 characters.
- Non-numeric length input must be handled without crashing.
- Any menu choice other than `1` or `2` must show an error and return to the menu.
- Only the Python standard library may be used (`random` and `string`).

## Sample Run

```
------------------------------
   Password Generator
------------------------------

1. Make a password
2. Quit
Pick one: 1
How long should it be? 10
Your password: v@4Kd!8rQz

1. Make a password
2. Quit
Pick one: 2
Bye!
```

## Edge Cases

| Case | Expected behavior |
| --- | --- |
| Length entered as text (e.g. `abc`) | Prints "That's not a number, try again." and returns to the menu |
| Length below 4 (e.g. `2`) | Prints "Needs to be at least 4 characters." |
| Menu choice such as `5` | Prints "Not a valid option." |
| Negative or zero length | Rejected by the minimum length rule |

## Note on Security

The `random` module is not cryptographically secure. It is acceptable for learning purposes, but a production tool should use the `secrets` module instead.

## Possible Extensions

- Let the user exclude symbols or look-alike characters
- Guarantee at least one letter, digit, and symbol in every password
- Generate several passwords in one run
- Copy the result to the clipboard
