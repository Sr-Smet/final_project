import pytest
import senter_stand_request
import data

# Получение номера трека
def get_track_number():
    resp_new_body = senter_stand_request.create_new_order()
    return resp_new_body.json()["track"]

# Передача номера трека
params = data.params.copy()
params["t"] = get_track_number()

# Позитивный тест
def positive_assert():
    request = senter_stand_request.to_get_order_under_track_number(params)
    assert request.status_code == 200

# Проверка статуса кода
def test_track_status():
    positive_assert()

# Сметанин Андрей, Марс08А — Финальный проект. Инженер по тестированию плюс