# Python File Organizer (OOP and SOLID)

A highly testable, object-oriented CLI utility written in Python to automate file organization. 

## Key Architecture and Patterns

- Single Responsibility Principle (SRP): Separated file discovery logic from disk operations.
- Open/Closed Principle (OCP): File-to-folder mapping is handled by a configuration dictionary. Adding support for new file types does not require modifying execution logic classes.
- Dependency Injection: The DirectoryOrganizer depends on abstractions, injecting the FileMover at instantiation, allowing for effortless unit testing.
- Automated Testing: Implemented integration/behavior tests using pytest and its safe tmp_path fixture to prevent state pollution.
- Automated CI: Continuous Integration pipeline via GitHub Actions executes the test suite on every push.

## Getting Started

### Prerequisites
- Python 3.8+
- Linux/Unix environment (Makefile support)

### Installation and Setup

1. Clone the repository:
    git clone https://github.com/DenisIvanov42/file-organizer.git
    cd file-organizer

2. Set up virtual environment:
    python3 -m venv .venv
    source .venv/bin/activate

3. Install dependencies:
    pip install -r requirements.txt

## Usage

You can use the provided Makefile to quickly run or test the project.

### Run the Application
To run the script and organize the local ./database directory:
    make run

### Run Tests
To execute the automated pytest suite:
    make test
