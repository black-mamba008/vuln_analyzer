# Vulnerability Scanner

A simple web-based vulnerability scanner using Flask and Nmap to scan target IP addresses or domains for open ports and HTTP header vulnerabilities.

## Project Overview

This project aims to provide a simple interface for scanning target IP addresses or domains for open ports and HTTP header vulnerabilities. The scanner uses Nmap to detect open ports and runs checks to identify common security issues in HTTP headers.

## Features

- Scan target IP addresses or domains for open ports using Nmap.
- Detect HTTP header vulnerabilities.
- Simple and intuitive web-based interface.
- Display scan results in an easy-to-read format.

## Installation

### Prerequisites

- Python 3.6+
- Flask
- Nmap installed and added to the system PATH

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/vulnerability-scanner.git
    cd vulnerability-scanner
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure Nmap is installed on your system. You can download it from [Nmap's official site](https://nmap.org/download.html).

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://127.0.0.1:5000`.

3. Enter the target IP address or domain you want to scan and click "Scan".

4. View the scan results on the same page.

## Project Structure

```
vulnerability-scanner/
├── static/
│ ├── styles.css
├── templates/
│ ├── index.html
│ ├── results.html
├── app.py
├── requirements.txt
└── README.md
```
## Contact

If you have any questions or suggestions, feel free to contact me at shahulhameedmaheen2001@gmail.com.

---
