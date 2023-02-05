from dotenv import dotenv_values 
from twilio.rest import Client

config = dotenv_values(".env")

account_sid = config["TWILIO_ACCOUNT_SID"] 
auth_token = config["TWILIO_AUTH_TOKEN"]
twilio_phone_number = config["TWILIO_SEND_PHONE_NUMBER"]
recipient_phone_number = config["RECIPIENT_PHONE_NUMBER"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=twilio_phone_number,
    to=recipient_phone_number,
    body="""

 ________________
/     こんにちは、      \\
\   drink water! 🚰   /
 ------------------
              \| 

╭━━━╮┈┈╱╲┈┈┈╱╲
┃╭━━╯┈┈▏▔▔▔▔▔▕
┃╰━━━━━▏╭▆┊╭▆▕
╰┫╯╯╯╯╯▏╰╯▼╰╯▕
┈┃╯╯╯╯╯▏╰━┻━╯▕
┈╰┓┏┳━┓┏┳┳━━━╯
┈┈┃┃┃┈┃┃┃┃┈┈┈┈
┈┈┗┻┛┈┗┛┗┛┈┈┈┈

    """
)

print("Message has been sent. Message SID: {}".format(message.sid))

