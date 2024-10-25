# DevTest

**Developer**: Nambala Santosh Rama Raju

## Project Overview
DevTest is a Django-based web application that allows users to upload Excel or CSV files, generates a summary report from the data, and emails the report as HTML body content. This README provides the setup instructions, functionality, and deployment process for the project.

## Features
1. **File Upload**: The web page accepts Excel and CSV files from users.
2. **Data Summary Report**: Automatically generates a report summarizing file contents, including statistics like unique states, customer pins, and DPD values.
3. **Email Report**: The summary is sent via email to `tech@themedius.ai`.
4. **Deployment**: Hosted on PythonAnywhere for easy access.

## Project Setup

### Installation

1. **Clone the Repository**:
   ```
   git clone https://github.com/Raju1422/Medius.git
   cd DevTest
   ```
2. **Create and Activate Virtual Environment**:
  ```
  python3 -m venv env
source env/bin/activate
```
3. **Install Dependencies**:
    ```
    pip install -r requirements.txt
    ```
4.  **Run the Server**:
```
python manage.py runserver
```
    
