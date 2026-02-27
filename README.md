# Helpdesk Ticket Triage Tool (Python CLI Automation Project)
A structured Python-based CLI project demonstrating rule-based incident categorization and priority assignment in IT support environments.

## Why this project
In many support environments, ticket quality and prioritization are inconsistent. This project demonstrates structured troubleshooting thinking by applying clear rules to classify incidents, assign priority, and suggest next steps.

## Features
- Categorizes tickets (Account, Network, Software, Hardware, Other)
- Assigns priority (P1–P4) based on impact and urgency keywords
- Provides a recommended next action for the technician
- Outputs a clean triage summary in the terminal

## How to run
1. Clone or download this repository
2. Run the tool:

```bash
python triage.py

Example input
VPN is down and I can’t access email. This is urgent.

Example output
Category: Network
Priority: P1 (Critical)
Recommended action: Check connectivity/VPN status, verify outage scope, escalate if widespread.

Planned Enhancements
Add CSV/JSON input support for batch triage
Add unit tests
Add basic logging
Optional: integrate AI-assisted response suggestions (future enhancement)

Author
Talix Doccy
