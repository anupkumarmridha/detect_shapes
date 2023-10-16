from app import app  

if __name__ == '__main__':
    app.run()

# Create a callable application for Gunicorn
application = app