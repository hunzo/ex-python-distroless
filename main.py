from flask import Flask
from datetime import datetime

import os 
app = Flask(__name__)

@app.get("/")
def main():

    print(os.environ.get('TEST', 'Nooooooooo'))
    return {
        "status": f"python3 distroless @{datetime.now()}"
    }
