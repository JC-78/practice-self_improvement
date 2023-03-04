import jwt
import smtplib
from email.mime.text import MIMEText
# Generate a JWT with the user's email address as a claim
def generate_jwt(email):
    payload = {'email': email}
    secret = 'meow' # should be set to a secret key that is known only to your backend.
    #options = {'expires_in': '1h'} # Change the expiration time as needed. doesn't work anymore
    #print(jwt.encode(payload, secret, algorithm='HS256', options=options))
    # return jwt.encode(payload, secret, algorithm='HS256', options=options)
     #generates a unique token that is associated with the user's email address.
    return jwt.encode(payload, secret, algorithm='HS256')

# Verify the JWT and return the email address
def verify_jwt(token):
    secret = 'meow' # Change this to your own secret key
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        email = payload['email']
        return email
    except:
        return None #If the JWT is invalid or has expired

# Send an email with the token included
# def send_email(email, token):
#     from_email = '' # Change this to your own email address
#     from_password = '' # Change this to your own email password
#     to_email = email
#     subject = 'Your authentication token'
#     body = f'Please use the following token to complete your authentication: {token}'
    
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = from_email
#     msg['To'] = to_email
    
#     server = smtplib.SMTP('smtp.gmail.com', 587) # Change the SMTP server and port as needed
#     server.starttls()
#     server.login(from_email, from_password)
#     server.sendmail(from_email, to_email, msg.as_string())
#     server.quit()

#I decided not to use above method as I don't want to send credentials over the internet
# Since that's not secure. A more secure alternative to sending email through SMTP directly is to use a
#  third-party email service that provides a secure API for sending emails. One such service is SendGrid.
def send_email(email, token):
    from_email = 'your_email@example.com' # Change this to your own email address
    to_email = email
    subject = 'Your authentication token'
    body = f'Please use the following token to complete your authentication: {token}'
    
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        plain_text_content=body
    )
    
    try:
        sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY')) # Set your SendGrid API key as an environment variable
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

#Method below involves using the Amazon Web Services (AWS) SDK for Python (Boto3) 
# to send the email. You'll need to have an AWS account and an IAM user with permission to send emails using SES. 

# def send_email(email, token):
#     from_email = 'your_email@example.com' # Change this to your own email address
#     to_email = email
#     subject = 'Your authentication token'
#     body = f'Please use the following token to complete your authentication: {token}'

#     # Set up an Amazon SES client
#     ses_client = boto3.client('ses', region_name='us-east-1') # Change the region as needed
    
#     # Send the email
#     response = ses_client.send_email(
#         Source=from_email,
#         Destination={'ToAddresses': [to_email]},
#         Message={
#             'Subject': {'Data': subject},
#             'Body': {'Text': {'Data': body}}
#         }
#     )

#     print(response)

if __name__ == '__main__':
    em=''#add your email address
    token=generate_jwt(em)
    print("token is ",token)
    send_email(em, token)
    original_email=verify_jwt(token)
    print(original_email)
    