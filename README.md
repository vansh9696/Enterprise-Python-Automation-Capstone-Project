# Enterprise Python Automation Capstone Project

An end-to-end, production-ready Python automation tool designed for automated telemetry log fetching, dynamic PDF executive report generation, and cron-like background scheduling.

---

## 🚀 Features

* **CLI Interface**: Full control via `click` command-line options.
* **Telemetry Data Engine**: Aggregates microservices uptime, latency, and request metrics using `pandas`.
* **Dynamic PDF Generation**: Professional table-structured PDF reports built with `reportlab`.
* **Automated Scheduler**: Background job execution engine powered by `apscheduler`.
* **Package Ready**: Built with standard `pyproject.toml` packaging specifications.

---

## 🛠️ Architecture & Tech Stack

```text
enterprise-automation-capstone/
├── app/
│   ├── __init__.py
│   ├── cli.py          # Click CLI Command Gateway
│   ├── generator.py    # ReportLab PDF Generation Engine
│   ├── scheduler.py    # APScheduler Background Cron Engine
│   └── fetcher.py      # Telemetry Data Aggregator (Pandas)
├── pyproject.toml      # Build Metadata & Dependencies
└── README.md           # Documentation


⚙️ Installation & Setup

# Clone the repository
git clone [https://github.com/vansh9696/enterprise-automation-capstone.git]
cd enterprise-automation-capstone

# Create & Activate Virtual Environment
python -m venv .venv
.\.venv\Scripts\activate   # Windows PowerShell

# Install Editable Package
pip install -e .
🏃 Usage Examples
1. Generate PDF Report Instantly

python -m app.cli generate --output My_First_Report.pdf

2. Start Automated Background Scheduler

python -m app.cli schedule --interval 10
