from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the mangas page
@app.route('/mangas')
def mangas():
    return render_template('mangas.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Additional routes (example for a future extension)
@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

# API endpoint for JSON response (optional, can be expanded for API usage)
@app.route('/api/contact_info')
def api_contact_info():
    return {
        "email": "support@mangaverse.com",
        "phone": "+91-1234567890"
    }

# Run the app
if __name__ == '__main__':
    # Enable debug mode and allow reloading for development
    app.run(debug=True)

