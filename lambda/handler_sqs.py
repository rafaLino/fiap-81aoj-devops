import json
import time
from datetime import datetime

from utils.sqs_handler import SqsHandler
from utils.base_dao import BaseDAO

sqs = SqsHandler("https://sqs.us-east-1.amazonaws.com/732421282977/espera-entrega")
dao = BaseDAO("eventos-pizzaria")

def detail_handler(event, context):
    print(event)
    for record in event["Records"]:
        payload=record["body"]
        sqs.send(payload)

    return event


def update_handler(event, context):
    while(True):
        response = sqs.getMessage(10)
        if "Messages" in response:
            for message in response["Messages"]:
                msg_body = json.loads(message["Body"])
                dao.put_item({
                    "pedido": str(msg_body["pedido"]),
                    "status": "entregue",
                    "cliente": msg_body["cliente"],
                    "time": str(datetime.now())
                }),
        else:
            break
    
        time.sleep(1)
