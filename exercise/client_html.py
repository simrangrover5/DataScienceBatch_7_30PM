from server_html import app

site = app()

@site.route(r"/index")
def home():
    return \
"""<!DOCTYPE html>
<html>
<body> <p> AAYUSH </p> </body>
</html>"""

site.run()
