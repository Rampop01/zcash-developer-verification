#!/usr/bin/env python3
"""
Zcash Developer Verification
Quest Task: Print participant name, current timestamp, and a generated random value.
"""

import datetime
import secrets

PARTICIPANT_NAME = "rampop"
GITHUB_USERNAME = "rampop01"

def main():
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    local_now = datetime.datetime.now().astimezone()
    entropy = secrets.token_hex(16)

    separator = "=" * 62
    print(separator)
    print("           ZCASH DEVELOPER VERIFICATION - RUN OUTPUT")
    print(separator)
    print(f"1. Participant Name : {PARTICIPANT_NAME} (GitHub: @{GITHUB_USERNAME})")
    print(f"2. Current Timestamp: {utc_now.strftime('%Y-%m-%dT%H:%M:%SZ')} (UTC)")
    print(f"                     {local_now.strftime('%a, %d %b %Y %H:%M:%S %z')} (Local)")
    print(f"3. Random Value     : {entropy} (128-bit hex)")
    print(separator)
    print("Status: VERIFIED")
    print(separator)

if __name__ == "__main__":
    main()
