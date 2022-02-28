import starkbank

from src.authentication import user

starkbank.user = user

webhook_invoice = starkbank.webhook.create(
    url="https://bb02-2804-431-c7c6-6080-8ccc-df19-b709-c5ec.ngrok.io",
    subscriptions=[
        "invoice",
    ]
)

print(webhook_invoice)

