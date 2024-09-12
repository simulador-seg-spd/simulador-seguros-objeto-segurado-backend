from flask import jsonify
from src.dto.response_dto import ResponseErrorDto, ResponseSuccessDto

def resp_ok(status=200,resource="", message="", data=None, **extras):
    """
    Responses ok
    """
    if not resource:
        resource = ""

    if not message:
        message = "The request was successful"

    response_model = ResponseSuccessDto(
        status=status,
        message=message,
        resource=resource,
        dados=data,
    )
    if type(data) == dict:
        response_model.set_response(data)
    else: 
        if data:
            response_model.set_response(data.dict())

    response = response_model.model_dump()
    print(response)
    response.update(extras)
    resp = jsonify(response)
    resp.status_code = status

    return resp

def resp_error(status=400,resource="", errors={}, msg="",transaction_id=""):
    """
    Responses ERROR
    """
    if not type(errors)==dict and not type(errors)==str:
        try:
            errors = errors.message
        except Exception as e:
            errors = e
    response_model = ResponseErrorDto(
        status=status,
        message=msg,
        resource=resource,
        errors=errors,
        transactionId=transaction_id
    )

    resp = jsonify(response_model.model_dump())

    resp.status_code = status

    return resp