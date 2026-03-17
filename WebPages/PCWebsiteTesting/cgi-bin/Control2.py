#Info from https://realpython.com/python-http-server/
#The purpose of this code is to test the legocar button controls
#To start a web server go to a terminal and type....
#python3 -m http.server
#To call something in the directory call
#localhost:8080 will list the files in the directory
#localhost:8080/testScript.py
#This delivers everything but does not act as a python script
#create a new folder called cgi-bin under this directory
#start the webserver like this
#python3 -m http.server --cgi
#This tells the server to serve up .py pages using scripting instead of literals
#from a web browser call http://localhost:8000/cgi-bin/Control2.py
#To find how to access this from any browser on the local network
#in the terminal type ipconfig /all
#Look for the lease obtaied field which should match
#when you started the server.
#So now the call could be for example
#http://192.168.0.209:8000/cgi-bin/Control2.py
import os
print(
f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buttons and Slider Example</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f4f4f9;
        }}
        /* Container for the rows of buttons */
        .button-container {{
            display: flex;
            flex-direction: column;
            gap: 15px; /* Spacing between the top and bottom rows */
            margin-bottom: 40px;
        }}
        /* Flexbox handles centering the buttons within each row */
        .button-row {{
            display: flex;
            justify-content: center;
            gap: 15px; /* Spacing between buttons in the same row */
        }}
         /* Button Styling */
        button {{
            padding: 10px 25px;
            font-size: 16px;
            cursor: pointer;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            transition: background-color 0.3s;
        }}

        button:hover {{
            background-color: #0056b3;
        }}

        /* Styling for the slider container */
        .slider-group {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }}

        input[type="range"] {{
            width: 250px;
            cursor: pointer;
        }}
</style>
</head>
<body>
<form id="myForm"  method="GET">
    <div class="button-container">
        <div class="button-row">
            <button id="btn1">Button 1</button>
            <button id="btn2">Button 2</button>
        </div>
        <div class="button-row">
            <button id="btn3">Button 3</button>
            <button id="btn4">Button 4</button>
            <button type="submit" name="Right" value="R" id="btn5">Right</button>
        </div>
    </div>

    <div class="slider-group">
        <label for="volumeSlider"><strong>Value Slider:</strong></label>
        <input type="range" id="volumeSlider" name="volumeSlider" onChange=submit() min="0" max="100" value="50">
    </div>
</form>
<ul>
  <li><b>CONTENT_TYPE:</b> {os.getenv("CONTENT_TYPE")}</li>
  <li><b>HTTP_USER_AGENT:</b> {os.getenv("HTTP_USER_AGENT")}</li>
  <li><b>QUERY_STRING:</b> {os.getenv("QUERY_STRING")}</li>
  <li><b>REQUEST_METHOD:</b> {os.getenv("REQUEST_METHOD")}</li>
</ul>
</body>
</html>"""
)
