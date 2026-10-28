import datetime

NAME = "rampop"
GITHUB_USER = "rampop01"

def main():
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    print("Name:", f"{NAME} (GitHub: {GITHUB_USER})")
    print("Timestamp:", utc_now.isoformat())

if __name__ == "__main__":
    main()
