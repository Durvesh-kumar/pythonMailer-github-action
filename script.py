import smtplib
from email.mime.text import MIMEText # MINMEText is class that is represents the text of email
from email.mime.multipart import MIMEMultipart # MIMEMultipart is a class tha represents the email message itself

import os


def send_mail(workflow_name, repo_name, workflow_run_id):
    # emial details
    sender_email: os.getenv('SENDER_EMAIL') # type: ignore
    sender_password: os.getenv('SENDER_PASSWORD') # type: ignore
    receiver_email: os.getenv('RECEVER_EMAIL') # type: ignore

    # Email message
    subject = f"Workflow {workflow_name} failed repo {repo_name}"
    body = f"Hi, Workflow {workflow_name} is failed for the repo {repo_name}. Please check the logs more details, \nMore details: \.nMore Run_id {workflow_run_id}"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(body, 'plain')

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, sender_password, text)
        server.quit()

        print('Email send Successfully')
    except Exception as e:
        print(f"Error {e}")

    send_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))