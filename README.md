# Expense Processor CLI 🚀

A professional-grade data pipeline that automates the ingestion, validation, and analysis of financial expense data.

## 🏗️ Architecture Overview
This project follows a modular pipeline architecture:
1. **Ingestion**: Scans the `/data` directory for multiple CSV files using `pathlib`.
2. **Validation**: Uses **Pydantic** to enforce strict data types and business rules (e.g., preventing negative amounts).
3. **Storage**: Securely moves validated data into a **PostgreSQL** database using batch processing.
4. **Analytics**: Automatically generates financial reports using SQL aggregations.
5. **Orchestration**: Fully containerized using **Docker Compose** for environment parity.

## 🛠️ Tech Stack
- **Python 3.13** (Managed by `uv`)
- **Pydantic** (Data Validation)
- **PostgreSQL 15** (Database)
- **Docker & Docker Compose** (Containerization)
- **Psycopg2** (Database Driver)


# Expense Processor CLI 🚀

A professional-grade data pipeline built to automate the ingestion, validation, and analysis of financial expense data. This application is fully containerized and designed for high reliability and scalability.

---

## 🏗️ Application Architecture Overview
The system follows a **Modular Pipeline Architecture**, separating concerns into distinct layers to ensure the code is maintainable and scalable.

```text
[Data Source] -> [Ingestion Layer] -> [Processing] -> [Persistence] -> [Presentation]
      |               |                 |              |               |
      v               v                 v              v               v
[CSV Files] -> [pathlib Discovery] -> [Pydantic] -> [PostgreSQL] -> [SQL Reports]
                      ^                 |              ^
                      |                 v              |
               [.env Config]     [Error Logging] [Docker Volumes]



Git Workflow Explanation:
This project follows professional Feature Branching standards:

feature/data-modeling: Environment setup and Pydantic schema.

feature/csv-ingestion: File discovery and logging logic.

feature/database-integration: PostgreSQL schema and connection bridge.

feature/docker-setup: Containerization and orchestration.

main: The stable production branch where all features are merged.

## 🚀 How to Run
Ensure you have Docker installed, then run:
```bash
docker-compose up --build


Assumptions and Challenges
Race Condition: Handled the startup delay where Python tries to connect before PostgreSQL is ready.

Precision: Used DECIMAL(12, 2) for currency to avoid floating-point errors.

Resilience: Designed to log individual row errors without stopping the entire pipeline.