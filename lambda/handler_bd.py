from utils.base_dao import BaseDAO
from datetime import datetime


def source_handler(event, context):
    dao = BaseDAO("eventos-pizzaria")
    dao.put_item({
        "pedido": event["detail"]["pedido"],
        "status": event["detail"]["status"],
        "cliente": event["detail"]["cliente"],
        "time": datetime.now()
    })

    return True
