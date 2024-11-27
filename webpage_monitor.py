import requests
from bs4 import BeautifulSoup
import json
import difflib
from datetime import datetime
import os
import sys

class WebpageMonitor:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Create directories for state and changes
        os.makedirs('state', exist_ok=True)
        os.makedirs('changes', exist_ok=True)
        
        self.state_file = os.path.join('state', 'previous_state.json')

    def fetch_page(self):
        """Fetch and parse the webpage content."""
        try:
            response = requests.get(self.url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            # Parse HTML and get clean text
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
                
            # Get text and normalize spaces
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            return text
            
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            sys.exit(1)

    def load_previous_state(self):
        """Load the previous state from file."""
        try:
            if os.path.exists(self.state_file):
                with open(self.state_file, 'r', encoding='utf-8') as f:
                    state = json.load(f)
                return state.get('content')
            return None
        except Exception as e:
            print(f"Error loading previous state: {e}")
            return None

    def save_current_state(self, content):
        """Save the current state to file."""
        state = {
            'timestamp': datetime.now().isoformat(),
            'url': self.url,
            'content': content
        }
        
        try:
            with open(self.state_file, 'w', encoding='utf-8') as f:
                json.dump(state, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving state: {e}")
            sys.exit(1)

    def save_changes(self, diff):
        """Save detected changes to a file."""
        if diff:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'changes/changes_{timestamp}.txt'
            
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Changes detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"URL: {self.url}\n")
                    f.write('-' * 80 + '\n')
                    f.write('\n'.join(diff))
                print(f"Changes saved to {filename}")
            except Exception as e:
                print(f"Error saving changes: {e}")
                sys.exit(1)

    def check_for_changes(self):
        """Main function to check for changes."""
        print(f"Checking webpage: {self.url}")
        
        # Get current content
        current_content = self.fetch_page()
        if not current_content:
            return
        
        # Load previous state
        previous_content = self.load_previous_state()
        
        # Compare if we have previous content
        if previous_content:
            diff = list(difflib.unified_diff(
                previous_content.splitlines(),
                current_content.splitlines(),
                fromfile='Previous Version',
                tofile='Current Version',
                lineterm=''
            ))
            
            if diff:
                print("Changes detected!")
                self.save_changes(diff)
            else:
                print("No changes detected.")
        else:
            print("Initial state captured.")
        
        # Save current state
        self.save_current_state(current_content)

def validate_url(url):
    """Validate URL format and accessibility."""
    if not url.startswith(('http://', 'https://')):
        print("Error: URL must start with http:// or https://")
        sys.exit(1)
    
    try:
        response = requests.head(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error accessing URL: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python webpage_monitor.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    validate_url(url)
    
    monitor = WebpageMonitor(url)
    monitor.check_for_changes()
