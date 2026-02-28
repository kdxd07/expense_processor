# Use a lightweight Python image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copy the dependency files
COPY pyproject.toml uv.lock ./

# Install 'uv' and project dependencies
RUN pip install uv && uv sync --frozen

# Copy the rest of the source code
COPY . .

# Command to run the application
CMD ["uv", "run", "src/main.py"]