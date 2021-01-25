# Import app module
from application import app

# Run on current hostsss
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")