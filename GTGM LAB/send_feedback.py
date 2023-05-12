from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('./Home')

@app.route('/send_feedback', methods=['POST'])
def submit_feedback():
    from_address = 'test@gvwgroup.pl'
    to_address = 'daniilberegovoj62@gmail.com'
    subject = 'New feedback {}'
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Create message object
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject.format(name)
    msg.attach(MIMEText(message))

    # Connect to SMTP server and send email
    with smtplib.SMTP('in-v3.mailjet.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(from_address, '5050a138d87efd8d813adef8e2f36c31')
        smtp.sendmail(from_address, to_address, msg.as_string())

    return 'Your feedback has been submitted successfully!'

if __name__ == '__main__':
    app.run()
