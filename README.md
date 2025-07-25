# Pytest Automation Framework (Personal Project)

This repository showcases my **personal learning project** to practice **automated testing** using **Pytest** with Python.

## 📌 Project Overview

This project was created to deepen my understanding of:
- Writing clean, reusable test cases with **Pytest**
- Using **fixtures**, **assertions**, and **parameterization**
- Organizing test modules for maintainability and scalability
- Generating test reports to visualize test results
- Managing Python virtual environments and dependencies
- Using **Git** and **GitHub** for version control and collaboration

I wrote approximately **20 test cases** covering positive, negative, and edge-case scenarios for a sample web application / API.

## ✅ Key Highlights

- Automated functional and unit tests with **Pytest**
- Practiced good test structure and naming conventions
- Created reusable fixtures to avoid repetitive code
- Parameterized tests to cover multiple data sets efficiently
- Produced clear, readable output in the terminal and optional HTML reports
- Managed dependencies in a `requirements.txt` file

## ⚙️ Tech Stack

- **Language:** Python 3.x
- **Framework:** Pytest
- **Environment:** venv (virtual environment)
- **Version Control:** Git & GitHub

## 🚀 How to Run This Project

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<your-username>/pytest-automation-framework.git
   cd pytest-automation-framework
   
2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate
   
3. Install dependencies:
   pip install -r requirements.txt

4. Run the tests:
   pytest -v

   Or run with a simple HTML report:
   pytest --html=report.html

📂 Folder Structure
pytest-automation-framework/
│
├── tests/               # Test modules organized by feature or component
│   ├── test_sample.py   # Example test file
│   └── ...
├── requirements.txt     # Project dependencies
├── README.md            # This file
└── venv/                # Virtual environment (not tracked in Git)

✏️ Author
OLA KOYA
