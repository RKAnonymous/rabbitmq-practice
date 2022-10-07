import requests

# Create your views here.
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Quote, QuoteUser
from .serializers import QuoteSerializer, QuoteUserSerializer
from .producer import publish


class QuoteViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()


class QuoteUserViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = QuoteUserSerializer
    queryset = QuoteUser.objects.all()


@api_view(["GET"])
def like(request, pk):

    query = {"username": "john"}
    req = requests.get("http://127.0.0.1:8000/users", params=query, timeout=10)
    data = req.json()
    print(data)

    # try:
    for s in range(len(data)):
        if data[s]["id"]:
            quoteuser = QuoteUser.objects.create(user_id=data[s]["id"], quote_id=pk)
            quoteuser.save()
            publish("quote_liked", pk)
            print("Quoteuser created")
            return Response("Quote liked...", status=status.HTTP_201_CREATED)
    # except Exception as exc:
        
    #     return Response({"exception": exc}, status=status.HTTP_400_BAD_REQUEST)
