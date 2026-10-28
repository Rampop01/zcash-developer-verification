# Zcash Developer Verification

Verification project for the **Zcash Developers Quest** on Gleyo.

- **Participant Name:** `rampop`
- **GitHub Username:** `rampop01`

---

## Quest Objective
Prove the participant can clone → edit → run → commit → branch → merge → document.

### Task Requirements
1. A program that prints, in one run:
   - **Participant Name**: `rampop`
   - **Current Timestamp**: UTC & Local formatted timestamp
   - **Random Value**: 128-bit cryptographically secure hex value
2. Repository demonstrates Git workflow: 3 initial commits, branch creation, file modification, and branch merge.
3. README contains exact run commands.

---

## How to Run

### Run Command
Ensure Python 3 is installed, then run:

```bash
python3 main.py
```

### Example Output
```text
==============================================================
           ZCASH DEVELOPER VERIFICATION - RUN OUTPUT
==============================================================
1. Participant Name : rampop (GitHub: @rampop01)
2. Current Timestamp: 2026-10-28T12:35:10Z (UTC)
                     Wed, 28 Oct 2026 13:35:10 +0100 (Local)
3. Random Value     : 3d5e8f497a1c2b60e9d4a7f18b32c50e (128-bit hex)
==============================================================
Status: VERIFIED
==============================================================
```

---

## Git Workflow Verification
Verify commit history and merge branch:
```bash
git log --graph --oneline --all
```
