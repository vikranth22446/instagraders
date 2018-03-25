from app import create_app

application = create_app('development')

application.secret_key = "secret key"
application.run()
