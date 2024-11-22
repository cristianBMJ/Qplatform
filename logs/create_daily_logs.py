import os
from datetime import datetime

def create_daily_log(base_path="logs"):
    # Get current date
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}.md"
    
    # Define full path
    full_path = os.path.join(base_path, filename)
    
    # Create logs directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)
    
    # Check if the file already exists to avoid overwriting
    if not os.path.exists(full_path):
        # Create the log file with a template
        with open(full_path, "w") as file:
            file.write(f"# Daily Log - {today}\n\n")
            file.write("## 1. Objective:\n- [ ] Define today’s goal(s).\n\n")
            file.write("## 2. Tasks Completed:\n- \n\n")
            file.write("## 3. Challenges or Blockers:\n- \n\n")
            file.write("## 4. Learnings:\n- \n\n")
            file.write("## 5. Plan for Tomorrow:\n- \n\n")
        print(f"Log file created: {full_path}")
    else:
        print(f"Log file already exists: {full_path}")

if __name__ == "__main__":
    create_daily_log()
