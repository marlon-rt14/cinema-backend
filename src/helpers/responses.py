from flask import jsonify 
from http import HTTPStatus


def bad_response(
    ok=False,
    msg="Internal server error",
    data=None,
    status=HTTPStatus.INTERNAL_SERVER_ERROR,
):
    return (jsonify({"ok": ok, "msg": msg, "data": data}), status)


def success_response(
    data,
    msg="Success",
    ok=True,
    status=HTTPStatus.ACCEPTED,
):
    return (jsonify({"ok": ok, "msg": msg, "data": data}), status)
