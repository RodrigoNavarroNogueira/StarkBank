import starkbank

from src.authentication import user

starkbank.user = user

webhook_invoice = starkbank.webhook.create(
    url="https://6b01-2804-431-c7c6-6080-58ee-4529-7e59-a0e0.ngrok.io",
    subscriptions=[
        "invoice",
    ]
)

print(webhook_invoice)

