from typing import Any
from pydantic import BaseModel
from abc import ABC, abstractmethod

class ResponseDtoAbstract(ABC):
    @abstractmethod
    def set_response(self, response):
        raise NotImplementedError

class ResponseSuccessDto(BaseModel,ResponseDtoAbstract):
    ok: bool = True
    status: int
    message: str
    resource: str
    data:Any = None
    def set_response(self, response):
        self.data = response



class ResponseErrorDto(BaseModel,ResponseDtoAbstract):
    ok: bool = False
    status: int
    resource: str
    message: str
    transactionId: str
    errors: Any = None

    def set_response(self, response):
        self.errors = response