# AI-Generated Webpage Monitor

This project was created entirely through interaction with the Cline AI assistant VSCode extension, powered by Claude 3.5 Sonnet through OpenRouter. It's a containerized Python application that monitors webpages for changes at regular intervals.

## Creating This Project with Cline and OpenRouter

This entire project was developed through a conversation with the Cline AI assistant, which uses OpenRouter to connect with Claude 3.5 Sonnet. OpenRouter provides a unified API for accessing various AI models, and in this case, it facilitated the interaction between the VSCode Cline extension and Claude 3.5 Sonnet, enabling a seamless development experience.

Here's how the conversation flowed:

1. Initial Request:
   ```
   create a python script that fetches a web page at regular intervals and compares the differences in the webpage.
   ```

2. Iterative Development:
   - Claude 3.5 Sonnet through Cline first created a basic Python script with continuous monitoring
   - When asked to modify it to run once and save state:
     ```
     instead of a python script that continuously runs I want it to only run once and save the state info to a file, then the next time it runs, compare the site to the previous state info. package this into a docker container so that it runs when the docker container is invoked.
     ```
   - When asked about scheduling:
     ```
     how do i run this at regular intervals?
     ```
   - Finally, documenting the process:
     ```
     output all these commands and responses into a readme file to be used in github. illustate that this project was created entirely with AI.
     ```

### Reproducing This Project

To recreate this project:

1. Install the Cline extension in VSCode
2. Configure Cline to use OpenRouter with Claude 3.5 Sonnet
3. Create a new directory for your project
4. Open the command palette and start a conversation with Cline
5. Follow the conversation flow above
6. Cline will create each file and explain its purpose
7. You can ask follow-up questions to modify or improve the implementation

The power of using Cline with Claude 3.5 Sonnet through OpenRouter is that it:
- Provides access to a powerful AI model through a simple interface
- Understands the full context of your project
- Can create and modify multiple files
- Provides clear explanations of its actions
- Can adapt to changing requirements
- Handles both code and documentation

## Project Structure

```
.
├── webpage_monitor.py     # Main Python script
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
├── docker-compose.yml   # Container orchestration
├── .env                # Environment configuration
├── run-monitor.bat     # Windows run script
└── run-monitor.sh      # Unix run script
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

## Development Process with Cline and Claude 3.5 Sonnet

This project demonstrates the power of AI-assisted development through Cline and OpenRouter. The development process was:

1. Initial Requirements Phase:
   - Stated the basic need for a webpage monitor
   - Claude 3.5 Sonnet created the initial Python script

2. Iterative Improvement Phase:
   - Requested stateful operation instead of continuous running
   - AI refactored the script to use file-based state
   - Added Docker containerization
   - Implemented scheduling through Docker Compose

3. Documentation Phase:
   - Requested GitHub-ready documentation
   - AI generated comprehensive README
   - Added proper .gitignore configuration

Each step was handled through natural conversation with Claude 3.5 Sonnet via Cline, which:
- Understood the context of previous changes
- Made appropriate modifications across multiple files
- Provided clear explanations of changes
- Maintained consistency across the codebase

This development process shows how AI can:
- Accelerate initial development
- Handle complex refactoring
- Manage multiple files and dependencies
- Create comprehensive documentation
- Adapt to changing requirements

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

## Technical Stack

- AI Assistant: Claude 3.5 Sonnet
- AI Platform: OpenRouter
- IDE Integration: Cline VSCode Extension
- Programming Language: Python 3.10
- Containerization: Docker & Docker Compose
- Version Control: Git
