from app import create_app
from flask import abort, redirect, url_for

app = create_app()





app.run(host='0.0.0.0')
