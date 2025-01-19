from flask import Flask
from flaskr import create_app

app = create_app(None)


app.run(debug=True)
