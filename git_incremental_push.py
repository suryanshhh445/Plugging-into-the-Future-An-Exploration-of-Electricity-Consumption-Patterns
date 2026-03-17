import os
import subprocess
import time

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")

def push_incrementally():
    # Iterate through all files in the current directory
    for root, dirs, files in os.walk('.'):
        # Skip the .git directory
        if '.git' in dirs:
            dirs.remove('.git')
        
        for file in files:
            # Skip this script itself
            if file == 'git_incremental_push.py':
                continue
                
            file_path = os.path.join(root, file)
            print(f"Staging and committing: {file_path}")
            
            # Stage the specific file
            run_command(f'git add "{file_path}"')
            
            # Create a commit with a descriptive message based on the filename
            commit_message = f"Add {file} and initialize related components"
            run_command(f'git commit -m "{commit_message}"')
            
            # Optional: Add a small delay to make timestamps vary slightly
            # time.sleep(1) 

    print("Finished committing all files individually. Now run 'git push -u origin master'")

if __name__ == "__main__":
    push_incrementally()