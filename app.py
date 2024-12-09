from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # or your email provider's SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'mufaddalmurtaza27@gmail.com'  # your email address
app.config['MAIL_PASSWORD'] = 'eoxi njtd obwi thzl'  # your email password
app.config['MAIL_DEFAULT_SENDER'] = 'mufaddalmurtaza27@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('contact.html')  # Your HTML form

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create email message
        msg = Message(
            'New Message from Contact Form',
            recipients=['mufaddalmurtaza27@gmail.com'],  # Replace with your email
        )
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        # Send email
        try:
            mail.send(msg)
            return redirect(url_for('thank_you'))
        except Exception as e:
            return f"Error: {e}"


@app.route('/thank_you')
def thank_you():
    return "Thank you for contacting us!"

if __name__ == '__main__':
    app.run(debug=True)
