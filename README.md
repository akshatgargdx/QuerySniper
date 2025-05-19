# QuerySniper
In today’s digital age, SQL injection is a major threat to data security. It exploits weak input validation to access or leak sensitive data from databases. This tool scans URLs with crafted payloads to detect vulnerable points and help secure web applications.
 
 
 User enters a target URL in the frontend.
 JavaScript sends the URL via POST to the Flask backend.
 Backend runs the crawler to gather links with parameters.
 Each link is scanned using SQLi payloads:
    Error-based payloads (e.g., ', --)
    Boolean-based payloads (e.g., 1 AND 1=1, 1 AND 1=2)
 Detection results returned to frontend and saved to report.txt.

 Frontend: HTML, CSS, JavaScript
 Backend: Python (Flask)
 Scanner: requests, BeautifulSoup (bs4), urllib
 Others: flask-cors, colorama (optional)
	

	
