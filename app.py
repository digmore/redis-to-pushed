#!/usr/bin/python -u
import os
import pushed
import redis
import traceback

config = {
    'CHANNEL': 'notifications',
    'APP_KEY': None,
    'APP_SECRET': None,
    'PUSHED_ID': None,
}

print "Launching redis to pushed component"

# TODO: die if not all params
# take config items from environment where present
for configitem in config:
    if configitem in os.environ:
        config[configitem] = os.environ[configitem]

p = pushed.Pushed(config['APP_KEY'], config['APP_SECRET'])

try:
    red = redis.StrictRedis("redis")
    red_pubsub = red.pubsub()
    red_pubsub.subscribe(config['CHANNEL'])
except:
    print "Failed to subscribe to channel"

try:
    while True:
        for item in red_pubsub.listen():
            if item['data'] == 1:
                continue
            try:
                print type(item['data'])
                print "Attemping to send notification: '", item['data'], "'"
                shipment = p.push_pushed_id(item['data'], config['PUSHED_ID'])
                print "  Success, shipment ID was ", shipment
            except pushed.PushedAPIError as e:
                print "Pushed API exception:", traceback.format_exc()
            except requests.exceptions.RequestException as e:
                print "HTTP request exception:", traceback.format_exc()
except Exception as e:
    print traceback.format_exc()

