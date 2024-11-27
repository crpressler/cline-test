# AI-Generated Webpage Monitor

This project was created entirely through interaction with an AI assistant. It's a containerized Python application that monitors webpages for changes at regular intervals.

## Project Creation Process

This project was created through a series of AI-guided steps:

1. Initially created a Python script for continuous monitoring
2. Refactored to a stateful approach that saves webpage state between runs
3. Containerized with Docker for portability
4. Added Docker Compose for scheduled monitoring

## Project Structure

```
.
├── webpage_monitor.py     # Main Python script
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container configuration
├── docker-compose.yml    # Container orchestration
├── .env                  # Environment configuration
├── run-monitor.bat       # Windows run script
└── run-monitor.sh        # Unix run script
```

## Features

- Monitors any webpage for content changes
- Maintains state between checks
- Saves detailed change logs
- Runs in a Docker container
- Configurable check intervals
- Cross-platform support

## Dependencies

- Docker
- Docker Compose

## Configuration

Edit the `.env` file to configure the monitor:

```env
# URL to monitor (required)
WEBPAGE_URL=https://example.com

# Check interval in seconds (default: 300)
CHECK_INTERVAL=300
```

## Usage

### Method 1: Continuous Monitoring (Recommended)

1. Start the monitor:
   ```bash
   docker-compose up -d
   ```

2. View logs:
   ```bash
   docker-compose logs -f
   ```

3. Stop monitoring:
   ```bash
   docker-compose down
   ```

### Method 2: Single Check

Windows:
```batch
run-monitor.bat https://example.com
```

Unix:
```bash
chmod +x run-monitor.sh
./run-monitor.sh https://example.com
```

## Output Structure

The monitor creates two directories:

- `./state/`: Contains the current state of monitored webpages
  - `previous_state.json`: Latest webpage state
  
- `./changes/`: Contains change history
  - `changes_YYYYMMDD_HHMMSS.txt`: Generated when changes are detected

Example change file:
```
Changes detected at 2024-02-20 15:30:45
URL: https://example.com
--------------------------------------------------------------------------------
--- Previous Version
+++ Current Version
@@ -1,4 +1,4 @@
-Old content
+New content
```

## Docker Details

### Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY webpage_monitor.py .
RUN mkdir -p /app/state /app/changes

VOLUME ["/app/state", "/app/changes"]
ENTRYPOINT ["python", "webpage_monitor.py"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  webpage-monitor:
    build: .
    volumes:
      - ./state:/app/state
      - ./changes:/app/changes
    environment:
      - WEBPAGE_URL=${WEBPAGE_URL:-https://example.com}
    entrypoint: >
      /bin/sh -c '
      while true; do
        python webpage_monitor.py $$WEBPAGE_URL;
        echo "Waiting for next check...";
        sleep ${CHECK_INTERVAL:-300};
      done'
```

## Development Process

This project was developed through an AI-assisted process:

1. Initial requirements gathering and script creation
2. Iterative improvements based on feedback:
   - Added state persistence
   - Containerized the application
   - Added Docker Compose for scheduling
   - Created cross-platform run scripts

The entire codebase, including this README, was generated through AI interaction, demonstrating the potential of AI-assisted development in creating practical, production-ready applications.

## Notes

- The monitor uses a simple text-based comparison after cleaning HTML
- Changes are detected based on text content, not visual changes
- State and changes are persisted in local directories
- The Docker container runs with minimal privileges
- Logs are available through Docker Compose

## Error Handling

The monitor includes robust error handling for:
- Invalid URLs
- Network issues
- File system operations
- State management
- Container operations

Errors are logged clearly and the application fails gracefully when needed.
