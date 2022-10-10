from flask import Flask
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "YctkDFvaTj"
app.permanent_session_lifetime = timedelta(minutes=2)