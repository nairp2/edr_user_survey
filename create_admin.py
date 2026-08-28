from db import create_admin_user
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_admin.py <username> <password>")
        sys.exit(1)
    create_admin_user(sys.argv[1], sys.argv[2])
    print("Admin user '{sys.argv[1]}' created/updated.")