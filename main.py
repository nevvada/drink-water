import os
from twilio.rest import Client

def send_sms():
  account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
  auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
  twilio_phone_number = os.environ.get('TWILIO_PHONE_NUMBER')
  recipient_phone_number = os.environ.get('RECIPIENT_PHONE_NUMBER')

  client = Client(account_sid, auth_token)

  try:
    message = client.messages.create(
      from_=twilio_phone_number,
      to=recipient_phone_number,
      body="""\

    _________________
  /   こんにちは、      \\
  \   drink water! 🚰 /
    -----------------
    |/

   /\_/\\
  ( o o )
=(___)=
    U U

        """
      )

    print("Message has been sent. Message SID: {}".format(message.sid))

  except Exception as error:
    print("Error sending message: {}".format(str(error)))

def lambda_handler(event, context):
  send_sms()
