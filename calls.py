from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

from settings import ACCOUNT_SID, AUTH_TOKEN

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer():
    """Respond to incoming phone calls with a 'Hello world' message"""

    # Start our TwiML response
    resp = VoiceResponse()

    caller = request.values.get('From')
    twilio_number = request.values.get('To')
    send_sms(caller, twilio_number)

    # Read a message aloud to the caller
    resp.say("hello world!", voice='alice')

    return str(resp)


def send_sms(to_number, from_number):

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    try:
        client.messages.create(
            body='Thanks for calling!',
            from_=from_number,
            to='+353016183000'
        )
    except TwilioRestException as exception:
        # Check for invalid mobile number error from Twilio
        if exception.code == 21614:
            print("Uh oh, looks like this caller can't receive SMS messages.")

if __name__ == "__main__":
    app.run(debug=True)
