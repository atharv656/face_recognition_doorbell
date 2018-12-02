from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC728087a5bdc48ee727ab84ed337833b0'
auth_token = '3dfddade09d9aaae8c8bf4050f11a189'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+18303315151',
         to='+15184190103'
     )

print(message.sid)