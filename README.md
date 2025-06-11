# Simple CLI Password Manager

A secure, command-line password manager written in Python. It uses AES-256
encryption to store your passwords in a local, portable file.

## Features

-   **Strong Encryption:** Uses the `cryptography` library (Fernet) for
    authenticated AES-128-CBC encryption.
-   **Secure Key Derivation:** Uses PBKDF2 with a strong iteration count to
    protect your master password from brute-force attacks.
-   **Atomic Saves:** Never risk a corrupted password file. Saves are written
    to a temporary file before replacing the original.
-   **Inactivity Timeout:** Automatically saves and locks the vault after 5
    minutes of inactivity.
-   **Graceful Exit:** Catches `Ctrl+C` to ensure your work is always saved.
-   **Simple Commands:** Manage your passwords with an intuitive interactive
    session (`get`, `set`, `list`, `del`).

## Prerequisites

-   Python 3.6+
-   Git

## Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```

2.  Install the required Python libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

**To create a new vault:**

Run the script with a filename that does not yet exist.

```sh
python password_manager.py my_vault.safe
```

**To open an existing vault:**

Run the script with the path to your vault file.

```sh
python password_manager.py my_vault.safe
```

### Interactive Commands

-   `get <service>`: Retrieve the password for a service.
-   `set <service> <user> <pass>`: Add or update a password.
-   `del <service>`: Delete a password entry.
-   `list`: List all services stored in the vault.
-   `help`: Show the command list.
-   `exit`: Save changes and lock the vault.

