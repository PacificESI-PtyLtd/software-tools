#!/usr/bin/env python3
#
# -----------------------------------------------------------------------------
"""
Simple script to verify .htpasswd passwords
"""
# -----------------------------------------------------------------------------

import getpass

from passlib.apache import HtpasswdFile


# -----------------------------------------------------------------------------

def verify_password(htpasswd_path, username, password):
    """
    Verify a password against a .htpasswd file
    
    Args:
        htpasswd_path: Path to .htpasswd file
        username: Username to check
        password: Password to verify
    
    Returns:
        bool: True if password is correct, False otherwise
    """
    ht = HtpasswdFile(htpasswd_path)
    return ht.check_password(username, password)


# -----------------------------------------------------------------------------

def main():
    # Get inputs
    htpasswd_path = input("Path to .htpasswd file: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    # Verify
    if verify_password(htpasswd_path, username, password):
        print("✓ Password is correct!")
    else:
        print("✗ Password is incorrect!")


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()


# -----------------------------------------------------------------------------


