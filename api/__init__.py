from flask import Blueprint,jsonify,request
from DXsystems_backend.api import register

api=Blueprint("api",__name__)

@api.post("/")
def index():
    return register.save_inquiry(request)

