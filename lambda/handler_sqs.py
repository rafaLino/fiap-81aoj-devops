import json

from utils.sqs_handler import SqsHandler
from utils.base_dao import BaseDAO

sqs = SqsHandler("https://sqs.us-east-1.amazonaws.com/732421282977/espera-entrega")
dao = BaseDAO("eventos-pizzaria")

def detail_handler(event, context):
    for record in event["Records"]:
        payload=record["body"]
        sqs.send(payload)

    return event


def update_handler():
    while(True):
        response = sqs.getMessage(10)
        for message in response["Messages"]:
            dao.update_item(
                key={"pedido": message["pedido"]},
                update_expression="set status=:status",
                expression_attribute_values={":status": "entregue"}
            )
    
    time.sleep(1)


if __name__ == "__main__":
    update_handler()