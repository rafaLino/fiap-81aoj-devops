from utils.base_dao import BaseDAO
from datetime import datetime


def source_handler(event, context):
    dao = BaseDAO("eventos-pizzaria")
    print(event)
    dao.put_item({
        "pedido": str(event["detail"]["pedido"]),
        "status": event["detail"]["status"],
        "cliente": event["detail"]["cliente"],
        "time": str(datetime.now())
    })

    return True
