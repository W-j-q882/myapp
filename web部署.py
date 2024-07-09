import os
import subprocess

def pull_latest_code():
    print("Pulling latest code from the repository...")
    subprocess.run(["git", "pull"], check=True)

def install_dependencies():
    print("Installing dependencies using pip...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

def run_test_suite():
    print("Running test suite...")
    result = subprocess.run(["python", "-m", "unittest", "discover"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Tests failed!")
        print(result.stdout)
        return False
    print("All tests passed!")
    return True

def restart_web_server():
    print("Restarting web server...")
    subprocess.run(["systemctl", "restart", "your_web_server_service_name"], check=True)

if __name__ == "__main__":
    try:
        pull_latest_code()
        install_dependencies()
        if run_test_suite():
            restart_web_server()
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
