# Import the create_app function from the 'app' module.
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
