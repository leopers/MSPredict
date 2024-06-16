import sys
import os
from flask import Flask

#solving the problem of not finding the app module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
