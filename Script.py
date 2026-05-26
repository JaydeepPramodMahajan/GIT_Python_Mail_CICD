import smtplib
from email.mime.text import MIMEText #MIMEText is a class which is used to represent the text of the mail
from email.mime.multipart import MIMEMultipart#its a class that represent the email message itself
import os
def send_mail(workflow_name, repo_name):
    sender_email=os.getenv('SENDER_EMAIL')
    sender_password=os.getenv('SENDER_PASSWORD')
    receiver_email=os.getenv('RECEIVER_EMAIL')
    #Email Message
    subject=f"Workflow{workflow_name} failed for repo {repo_name}"
    body=f"Hi,the workflow {workflow_name} failed for the repo {repo_name}. Pleae check the logs for the more detailes.\nMore Detailes: \nRun_ID: {workflow_run_id}"

    msg=MIMEMultipart()
    msg['From']=send_email
    msg['To']=receiver_email
    msg['Subject']=subject
    msg.attach(MIMEText(body,'plain'))
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(send_mail,sender_password)
        text=msg.as_string()
        server.sendmail(sender_email,receiver_email,text)
        server.quit()
        print("Email Senedef Succesfully")
    except Exception as e:
        print(f"Error :{e}")

send_mail(os.getenv('WORKFLOW_NAME'),os.getenv('REPO_NAME'),os.getenv('WORKFLOW_RUN_ID'))

