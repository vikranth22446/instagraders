import sys
import logging
logging.basicConfig(stream=sys.stderr)
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

app = create_app('development')

if __name__ == '__main__':
    app.secret_key = "secret key"
    app.run()
