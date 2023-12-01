# Importing necessary libraries
from flask import Flask, render_template

# Creating a Flask web application
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def home():
    # Render the HTML template named 'index.html'
    return render_template('index.html')

# Run the application if the script is executed
if __name__ == '__main__':
    # Set debug=True for development purposes
    app.run(debug=True)
