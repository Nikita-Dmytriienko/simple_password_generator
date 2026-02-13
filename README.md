# Simple Password Generator

A command-line tool for generating secure random passwords.

## Usage

Basic usage:
```bash
python passgen.py
```

### Options

- `-l, --length` - Password length (default: 12)
- `-c, --count` - Number of passwords to generate (default: 1)
- `--no-digits` - Exclude numbers
- `--no-special` - Exclude special characters
- `--no-digits-and-special` - Exclude both numbers and special characters

### Examples

```bash
# Generate a 20-character password
python passgen.py -l 20

# Generate 5 passwords
python passgen.py -c 5

# Generate a password without digits
python passgen.py -l 16 --no-digits

# Generate 3 passwords, 16 characters each
python passgen.py -l 16 -c 3
```

## Requirements

- Python 3.x

## Security

This tool uses Python's `secrets` module for cryptographically secure random generation.
