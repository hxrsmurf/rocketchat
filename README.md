# RocketChat Incoming/Outgoing [Webhook](https://rocket.chat/docs/administrator-guides/integrations/) Configurations

These configurations use [Rocket Chat](https://rocket.chat/) to send SMS via [FlowRoute](https://www.flowroute.com/) API.

Release Notes:
- 2020 Dec 13
  - Updated formatting
  - Added Twilio and Discord WebHooks

- 2020 May 25
  - Added [incoming_hook_twilio.src](https://github.com/hxrsmurf/rocketchat/blob/master/incoming_hook_twilio.src) to support incoming Twilio SMS/MMS


- 2019 November 29 
  - Updated [outgoing_hook.src](https://github.com/hxrsmurf/rocketchat/blob/master/outgoing_hook.src) to support RocketChat's built-in token
  - Updated [outgoing_hook.src](https://github.com/hxrsmurf/rocketchat/blob/master/outgoing_hook.src) to listen on all private channels
  - Updated [incoming_hook.src](https://github.com/hxrsmurf/rocketchat/blob/master/incoming_hook.src) to route multiple incoming texts

Links:
- https://rocket.chat/docs/administrator-guides/integrations/
- https://developer.flowroute.com/api/messages/v2.1/send-an-sms/
- https://developer.flowroute.com/api/messages/v2.1/receive-an-mms/
