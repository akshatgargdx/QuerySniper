QuerySniper is a Python-based web vulnerability scanner that automatically detects SQL Injection (SQLi) vulnerabilities in web applications. It injects crafted payloads into URL parameters, analyzes responses, and flags potential SQLi points. This tool helps developers identify and fix SQLi risks before they can be exploited.
Features
URL-based scanning with SQL injection payloads
Basic crawling to scan multiple internal links

Detection of error-based and boolean-based SQL injections

Simple and clean web interface

Real-time scanning and result display

Python backend with Flask and a lightweight frontend

Technologies Used
Backend
Python 3
Flask
Requests
BeautifulSoup4
Flask-CORS
Urllib

Frontend
HTML
CSS
JavaScript


Installation
Clone the repository:

bash
git clone https://github.com/akshatgargdx/QuerySniper.git
Navigate into the project folder:

bash
cd QuerySniper
Install required Python packages:

nginx
pip install -r requirements.txt
If the requirements.txt file is not present, you can install manually:

nginx
pip install flask requests beautifulsoup4 flask-cors
Run the application:

nginx
python app.py
Open your browser and go to:

arduino
http://localhost:5000
Usage
Enter the target website URL in the input field.

Click the "Scan" button.

View scan results in real time.

Project Structure
csharp
QuerySniper/
│
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Web UI
├── static/
│   ├── style.css          # Stylesheet
│   └── script.js          # Frontend logic
├── scanner/
│   └── core.py            # Scanning and SQLi detection logic
├── requirements.txt       # Python dependencies
License
This project is licensed under the MIT License. Feel free to use and modify it.

