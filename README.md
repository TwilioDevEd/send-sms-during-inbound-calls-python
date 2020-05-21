<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Send an SMS during a phone call. Powered by Twilio and Python/Flask

![](https://github.com/TwilioDevEd/send-sms-during-inbound-calls-python/workflows/Flask/badge.svg)

> We are currently in the process of updating this sample template. If you are encountering any issues with the sample, please open an issue at [github.com/twilio-labs/code-exchange/issues](https://github.com/twilio-labs/code-exchange/issues) and we'll try to help you.

## About

Learn how to send an SMS to someone who's called your Twilio phone number while they're on the call.

This small sample application will say a short message to an inbound caller and, at the same time, send them an SMS.

[Read the full tutorial here!](https://www.twilio.com/docs/sms/tutorials/send-sms-during-phone-call-python)

Implementations in other languages:

| .NET | Java | Node | PHP | Ruby |
| :--- | :--- | :----- | :-- | :--- |
| [Done](https://github.com/TwilioDevEd/send-sms-during-inbound-calls-csharp)  | [Done](https://github.com/TwilioDevEd/send-sms-during-inbound-calls-java)  | [Done](https://github.com/TwilioDevEd/send-sms-during-inbound-calls-node)  | [Done](https://github.com/TwilioDevEd/send-sms-during-inbound-calls-php) | [Done](https://github.com/TwilioDevEd/send-sms-during-inbound-calls-ruby) |

## Features
- [Flask](http://flask.pocoo.org/) web framework
- [Twilio Python Helper Library](https://www.twilio.com/docs/libraries/python)
- Unit tests using [`pytest`](https://docs.pytest.org/en/latest/)

## Set up

### Requirements

- [Python](https://www.python.org/) >= **3.6.x** version

### Twilio Account Settings

You need to collect all the config values to run the application.

| Config Value  | Description |
| :-------------  |:------------- |
TWILIO_ACCOUNT_SID / TWILIO_AUTH_TOKEN | In [Twilio Account Settings](https://www.twilio.com/console).

### Local development

1. First clone this repository and `cd` into it.

   ```bash
   git clone https://github.com/TwilioDevEd/send-sms-during-inbound-calls-python.git
   cd send-sms-during-inbound-calls-python
   ```

2. Create the virtual environment, load it and install the dependencies.

   ```bash
   make install
   ```

   If you're using a Windows machine, you'll activate your environment in one of two ways:
   
   PowerShell: `. .\venv\Scripts\activate.ps1`
   
   Cmd shell: `.\venv\Scripts\activate.bat`

3. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   cp .env.example .env
   ```

   See [Twilio Account Settings](#twilio-account-settings) to locate the necessary environment variables.

4. Start the server, the following command will run the application on port 5000. Before running the following command, make sure the virtual environment is activated.

   ```bash
   make serve
   ```

6. Expose the application to the wider Internet using [ngrok](https://ngrok.com/).

    ```bash
    ngrok http 5000 -host-header="localhost:5000"
    ```

7. Configure Twilio to call your webhooks

   You will need to configure Twilio to call your application when calls are
   received in your [*Twilio Number*](https://www.twilio.com/console/phone-numbers/incoming).
   The voice url should look something like this:

   ```
   https://0f72e8a8.ngrok.io/answer
   ```

8. Finally, call your Twilio number to test it out.

That's it!

### Test

To run the tests locally, execute the following command. Before running the following command, make sure the virtual environment is activated.

```bash
python3 -m pytest
```

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* The CodeExchange repository can be found [here](https://github.com/twilio-labs/code-exchange/).
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.

