# Web App Deployment Automation Script

This Python script automates the deployment of a web application by performing the following steps:

1. Pull the latest code from a version control system (e.g., Git).
2. Install dependencies using pip.
3. Run the test suite.
4. If the tests pass, restart the web server (e.g., using systemctl).

## Prerequisites

- Python 3.x
- Git
- Pip
- A web server (e.g., Nginx, Apache) with systemctl support

## Usage

1. Clone this repository to your local machine.
2. Update the `config.py` file with your project details and server configuration.
3. Run the script using `python deploy.py`.

## Configuration

Update the `config.py` file with the following information:

- `PROJECT_DIR`: The directory where your project is located.
- `GIT_REPO`: The URL of your Git repository.
- `VENV_NAME`: The name of the virtual environment to create or use.
- `PIP_REQUIREMENTS`: The path to the requirements.txt file containing your project's dependencies.
- `TEST_COMMAND`: The command to run your test suite.
- `SERVER_NAME`: The name of your web server as configured in systemctl.

## License

This project is licensed under the MIT License. See the LICENSE file for details.