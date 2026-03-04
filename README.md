# Expense Processor CLI 🚀
A professional-grade data pipeline built to automate the Ingestion (Extract), Validation (Transform), and Analysis (Load) of financial expense data. This application is fully containerized to ensure high reliability and environment consistency.

## Expense Processor Architecture 🏗️
The system follows a Modular Pipeline Architecture, ensuring a clean separation of concerns between data handling and business logic.

Ingestion Layer: Automatically scans the /data directory for multiple CSV files using pathlib.

Validation Layer: Employs Pydantic to enforce strict data types and business rules (e.g., ensuring amounts are always positive).

Persistence Layer: Securely migrates validated data into PostgreSQL. It uses Idempotent Logic (TRUNCATE) to ensure fresh synchronization.

Analytics Engine: Generates real-time financial reports using SQL aggregations for total spending and category breakdowns.

## Expense Processor Tech Stack 🛠️
Python 3.13: Utilizing modern features like type hinting and uv package management.

Pydantic: For industry-standard data validation and schema enforcement.

PostgreSQL 15: Relational database chosen for financial data precision.

Docker & Docker Compose: For "Plug-and-Play" deployment and environment parity.

Psycopg2: High-performance database driver for PostgreSQL.

Pytest: Comprehensive unit testing for model validation.

## Expense Processor Project Structure 📂
.
├── src/
│   ├── database/       # DB Connection and SQL execution
│   ├── models/         # Pydantic data schemas
│   ├── utils/          # CSV processing and Analytics logic
│   └── main.py         # Application Entry Point
├── data/               # Folder for incoming CSV files
├── tests/              # Unit tests for data integrity
├── Dockerfile          # Container instructions
└── docker-compose.yml  # Multi-container orchestration

## Expense Processor Execution Guide 🚀
1. Prerequisites
Ensure you have Docker and Docker Compose installed.

2. Environment Configuration
Create a .env file in the root folder:
DB_NAME=expense_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432
DATA_FOLDER=./data

3. Build and Start
docker-compose up --build

## Expense Processor Key Features 📉
Idempotency: Designed to be re-run safely. It clears old data before syncing, ensuring the report always reflects current files.

Precision Handling: Uses DECIMAL(12, 2) in SQL to prevent floating-point errors in financial calculations.

Error Resilience: Individual row failures are logged as errors without stopping the entire pipeline processing.

Self-Documenting: Extensive use of Python Docstrings and type hints for professional collaboration.

## Expense Processor Development Workflow 🔄
This project maintains a professional commit history with clear feature branching:

main: Production-stable branch.

feature/data-modeling: Pydantic schema setup.

feature/database-integration: PostgreSQL bridge logic.

feature/docker-setup: Environment containerization.

# To view the visual commit graph:
git log --oneline --graph --all