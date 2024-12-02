from typing import Union, Optional

from django.utils.functional import Promise
from rest_framework import status
from rest_framework.exceptions import APIException

from commons.dataclasses import BaseDataClass


class ApiErrorData(BaseDataClass):
    detail: Union[str, Promise]
    code: Optional[str] = None


class ExtendedAPIException(APIException):
    def __init__(self, detail=None, code=None):
        if isinstance(detail, ApiErrorData):
            super().__init__(detail=detail.detail, code=detail.code)
            return
        super().__init__(detail, code)


class BadRequestException(ExtendedAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
