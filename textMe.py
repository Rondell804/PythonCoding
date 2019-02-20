from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC025bb223536be5edd0d6203949a9f5ea"
# Your Auth Token from twilio.com/console
auth_token  = "d399a53dc640314afabc0a80cbb4a2d0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18048366840",
    from_="+18044099326",
    body="This is a test! Hello, Rondell")

print(message.sid)
