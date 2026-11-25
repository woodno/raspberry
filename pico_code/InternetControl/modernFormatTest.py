#TODO This is the method of writing the html to control the
#LEGO Car expand to get it to function better

from HtmlControlPage import HtmlControlPage
html = """<!DOCTYPE html>
<html>
    <head> <title>Pico W</title> </head>
    <body> <h1>Pico W</h1>
        <p>{stateis}</p>
    </body>
</html>
"""
state = "on"
response = html.format(stateis=state)
print (response)

htmlpage = HtmlControlPage()
response2 = htmlpage.html.format(stateis=state, name=" john")
print (response2)