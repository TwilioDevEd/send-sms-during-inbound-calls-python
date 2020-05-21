from unittest.mock import patch


def test_answer(app, client):
  res = client.post('/answer', data = {'From': '+1234', 'To': '+5678'})
  say = '<Say voice="alice">Thanks for calling! We just sent you a text with a clue.</Say>'
  assert res.status_code == 200
  assert say in res.get_data(as_text = True)

@patch('twilio.rest.Client.messages')
def test_answer_call_send_message(mock, app, client):
  res = client.post('/answer', data = {'From': '+1234', 'To': '+5678'})
  assert res.status_code == 200
  mock.create.assert_called_with(body="There's always money in the banana stand.", from_='+5678', to='+1234')
