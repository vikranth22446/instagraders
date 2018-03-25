import sys
import logging
logging.basicConfig(stream=sys.stderr)
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

application = create_app('development')

application.secret_key = "secret key"
application.run()
