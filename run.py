# Import the create_app function from the 'app' module.
from app import create_app

# Call the create_app function to create our application.
app = create_app()

# Check if this script is being run directly (not imported as a module).
if __name__ == "__main__":
    app.run()
