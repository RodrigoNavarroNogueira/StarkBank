import starkbank

from src.authentication import user

from webhook.create_invoice_webhook import webhook_invoice

starkbank.user = user

if webhook_invoice.subscriptions == "invoice":
    print(webhook_invoice.log.invoice)