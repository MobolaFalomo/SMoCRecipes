from flask import Blueprint
auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
	return <h1>this is our homepage<h1/>
