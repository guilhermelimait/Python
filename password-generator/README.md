p7K@mN9!zQ
# Password Generator - Secure Password Creator

Generate strong, random passwords with customizable length using Python.

## Description

Creates cryptographically secure passwords using the `secrets` module. Ensures each password includes lowercase, uppercase, digits, and (optionally) punctuation. Prompts for length or accepts a CLI length argument and outputs five options at a time.

## Features

- Cryptographically secure (`secrets` module)
- Length input via prompt or CLI argument
- Guarantees mixed character types
- Option to include punctuation
- Generates five sample passwords per run

## Prerequisites

- Python 3.8+
- No external dependencies

## Usage

```bash
# Prompt for length (default 16)
python gerasenha.py

# Provide length via CLI
python gerasenha.py 20
```

## Behavior

- If length < 4, the script resets to 16 and warns.
- Invalid input falls back to 16.
- Uses `secrets.SystemRandom` to shuffle and avoid patterns.

## Dependencies

Standard library only:
- `secrets`
- `string`
- `sys`

## Notes

- Store generated passwords in a password manager.
- Use at least 12 characters for strong security.

---

Part of the [Python Projects Collection](../README.md)
