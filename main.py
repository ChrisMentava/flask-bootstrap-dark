from flask import Flask, render_template

# Create Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    """Route for the home page"""
    return render_template('index.html')

if __name__ == '__main__':
    # Run the application on 0.0.0.0:5000 as per guidelines
    app.run(host='0.0.0.0', port=5000)
