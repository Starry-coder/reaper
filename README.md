<div align="center">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python Version">
  <h1>🕷️ Reaper</h1>
  <p><b>Automated Security Reconnaissance Toolkit</b></p>
  <img src="https://img.shields.io/github/license/Starry-coder/reaper" alt="License">
</div>

---

## Overview

**Reaper** is a modular, extensible Python toolkit designed for automated security reconnaissance. It streamlines the process of gathering information about web applications, network services, and system vulnerabilities, making it an essential tool for penetration testers, bug bounty hunters, and security researchers.

## Features

- 🔍 **HTTP Checks**: Analyze web endpoints for common issues and misconfigurations.
- 🔑 **Password Auditing**: Check for weak or default credentials.
- 🚪 **Port Scanning**: Discover open ports and running services.
- 📊 **Reporting**: Generate comprehensive, readable reports of findings.
- 🧩 **Modular Design**: Easily extend with custom modules.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Starry-coder/reaper.git
   cd reaper
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script with desired options:
```bash
python reaper.py --help
```

Typical usage:
```bash
python reaper.py --target example.com --modules http_check,portscan,passwd_check
```

## Modules

- **http_check.py**: Performs HTTP endpoint analysis, checks for headers, status codes, and common vulnerabilities.
- **passwd_check.py**: Audits for weak or default passwords on services.
- **portscan.py**: Scans target hosts for open ports and service banners.
- **report.py**: Aggregates results and generates a readable report.

## Example

```bash
python reaper.py --target 192.168.1.1 --modules portscan,http_check
```


