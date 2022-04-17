import json
import logging
import sys

import greengrasssdk

# Logging
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# SDK Client
client = greengrasssdk.client("iot-data")

# Counter
my_counter = 0
max_value = 1
def lambda_handler(event, context):
    global my_counter
    global max_value
    #TODO1: Get your data
    #print(json.dumps(event))
    #TODO2: Calculate max CO2 emission
    curr = float(event["message"])
    if curr > max_value:
        max_value = curr
    client.publish(
        topic="hello/world/pubsub",
        payload=json.dumps(
            {"message": "Hello world! Sent from Greengrass Core.  Invocation Count: {}".format(max_value)}
        ),
    )
    #if max_value < int(json.dumps(event)):
    #    max_value = int(json.dumps(event))

    #TODO3: Return the result
    my_counter += 1

    return