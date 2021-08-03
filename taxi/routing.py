from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from trips.consumers import TaxiConsumer
from taxi.middleware import TokenAuthMiddlewareStack # new

application = ProtocolTypeRouter({
    # 'websocket': URLRouter([
    #     path('taxi/', TaxiConsumer),
    # ]),
    'websocket': TokenAuthMiddlewareStack( # changed
        URLRouter([
            path('taxi/', TaxiConsumer),
        ])
    ),
})
