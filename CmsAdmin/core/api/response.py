from rest_framework.response import Response
from rest_framework import status


def success(data: dict):
    return Response(data, status=status.HTTP_200_OK)
