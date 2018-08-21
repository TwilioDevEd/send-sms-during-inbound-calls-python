<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Send an SMS during a phone call. 
## Powered by Twilio and Python/Flask

Learn how to send an SMS to someone who's called your Twilio phone number while they're on the call.

This small sample application will say a short message to an inbound caller and, at the same time, send them an SMS.

[Read the full tutorial here!](https://www.twilio.com/docs/sms/tutorials/send-sms-during-phone-call-python)


## Local Development

This project is built using the [Flask](http://flask.pocoo.org/) web framework, Python 3, and the [Twilio Python Helper Library](https://www.twilio.com/docs/libraries/python).

1. First clone this repository and `cd` into it.

   ```bash
   $ git clone https://github.com/TwilioDevEd/send-sms-during-inbound-calls-python.git
   $ cd send-sms-during-inbound-calls-python
   ```

1. Create a new virtual environment with [virtualenv](https://virtualenv.pypa.io/en/latest/):

    ```bash
    $ virtualenv venv
    ```
    
    If you're using a linux or Mac computer, activate your environment with this line:
    ```bash
    $ source venv/bin/activate
    ```
    If you're using a Windows machine, you'll activate your environment in one of two ways:
    
    PowerShell: `. .\venv\Scripts\activate.ps1`
    
    Cmd shell: `.\venv\Scripts\activate.bat`

1. Install the dependencies.

    ```bash
    $ pip install -r requirements.txt
    ```
1. Create an environment file (`.env`) and define your Twilio Account SID and Auth Token. Both of these can be found in your [Twilio console](https://www.twilio.com/console).

   ```bash
   ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
   AUTH_TOKEN = 'your_auth_token'
   ```

1. Start the server.

    ```bash
    $ python calls.py
    ```

1. Expose the application to the wider Internet using [ngrok](https://ngrok.com/).

    ```bash
    $ ngrok https 5000 -host-header="localhost:5000"
    ```

1. Configure Twilio to call your webhooks

  You will need to configure Twilio to call your application when calls are
  received in your [*Twilio Number*](https://www.twilio.com/user/account/messaging/phone-numbers).
  The voice url should look something like this:

  ```
  http://<your-ngrok-subdomain>.ngrok.io/answer
  ```


## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.

