import data
import configuration
import requests

# Создание заказа
def create_new_order():
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_NEW_ORDER_PATH, json=data.order_body,
                         headers=data.headers)

# Получение созданного заказа по трек номеру
def to_get_order_under_track_number(params):
    response_order = requests.get(configuration.URL_SERVICE+configuration.GET_TRACK_NUMBER_PATH, params=params)
    return response_order