import starkbank

from src.authentication import user

starkbank.user = user

webhook_invoice = starkbank.webhook.create(
    url="https://7a5a-2804-431-c7c6-6080-f5a3-14ea-2781-3d83.ngrok.io",
    subscriptions=[
        "invoice",
    ]
)

print(webhook_invoice)

