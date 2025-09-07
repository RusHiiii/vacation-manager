# Stage 1: Base build stage
FROM python:3.13-slim AS builder

# Install Poetry
RUN pip install --upgrade pip && \
    pip install poetry

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

# Create and set the app directory
RUN mkdir /app
WORKDIR /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy only the Poetry files first (for better caching)
COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only main --no-root

# Stage 2: Production stage
FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

RUN useradd -m -r app && \
   mkdir /app && \
   chown -R app /app

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory
WORKDIR /app

# Copy application code
COPY --chown=app:app . .

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production

# Switch to non-root user
USER app

# Create static folder for building front files
RUN mkdir /app/vacation_manager/static

# Start app
CMD ["/app/docker/app/start.sh"]

