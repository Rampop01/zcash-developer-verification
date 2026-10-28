import datetime
import secrets

NAME = "rampop"
GITHUB_USER = "rampop01"

def main():
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    random_val = secrets.token_hex(16)
    
    print("Name:", f"{NAME} (GitHub: {GITHUB_USER})")
    print("Timestamp:", utc_now.isoformat())
    print("Random Value:", random_val)

if __name__ == "__main__":
    main()
