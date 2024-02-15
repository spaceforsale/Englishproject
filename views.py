from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for the views page
@app.route('/views')
def views():
    return render_template('views.html')

# Define a route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()