
Scroll down and click **Commit changes**.

Commit message: `Update README with project overview and usage`

✅ Now your repo reads like a real project.

---

## Step 3 — Add the Python file (`triage.py`)

Go back to the main repo page (Code tab).  
Click **Add file → Create new file**.

File name (type exactly):  
`triage.py`

Paste this code:

```python
from dataclasses import dataclass

@dataclass
class TriageResult:
    category: str
    priority: str
    recommendation: str


def triage_ticket(description: str) -> TriageResult:
    text = description.lower()

    # Category rules
    if any(k in text for k in ["password", "login", "locked", "mfa", "reset"]):
        category = "Account / Access"
        recommendation = "Verify identity, reset credentials/MFA, confirm access restored."
    elif any(k in text for k in ["wifi", "network", "vpn", "internet", "dns", "offline"]):
        category = "Network"
        recommendation = "Check connectivity, VPN/Wi-Fi status, confirm outage scope, escalate if widespread."
    elif any(k in text for k in ["outlook", "excel", "app", "software", "install", "update", "crash"]):
        category = "Software / Application"
        recommendation = "Reproduce issue, check updates, verify permissions, reinstall if needed."
    elif any(k in text for k in ["printer", "keyboard", "mouse", "monitor", "laptop", "hardware"]):
        category = "Hardware"
        recommendation = "Check power/cables, run basic diagnostics, swap peripherals if available."
    else:
        category = "General Support"
        recommendation = "Gather details (who/what/when), reproduce issue, document steps, route appropriately."

    # Priority rules (simple impact/urgency signals)
    urgent = any(k in text for k in ["urgent", "asap", "immediately", "down", "outage", "cannot", "can't"])
    high_impact = any(k in text for k in ["all users", "everyone", "entire", "company", "multiple", "system down"])
    low_impact = any(k in text for k in ["minor", "when you can", "not urgent", "low priority"])

    if high_impact and urgent:
        priority = "P1 (Critical)"
    elif urgent:
        priority = "P2 (High)"
    elif low_impact:
        priority = "P4 (Low)"
    else:
        priority = "P3 (Medium)"

    return TriageResult(category=category, priority=priority, recommendation=recommendation)


def main() -> None:
    print("=== Helpdesk Ticket Triage Tool ===")
    description = input("Describe the issue: ").strip()

    if not description:
        print("No description provided. Exiting.")
        return

    result = triage_ticket(description)

    print("\n--- Triage Summary ---")
    print(f"Category: {result.category}")
    print(f"Priority: {result.priority}")
    print(f"Recommended action: {result.recommendation}")


if __name__ == "__main__":
    main()
