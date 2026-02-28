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

## 🚀 How to Run
Ensure you have Docker installed, then run:
```bash
docker-compose up --build