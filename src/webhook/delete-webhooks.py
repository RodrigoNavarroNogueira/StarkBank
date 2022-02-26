import starkbank

from src.authentication import user

starkbank.user = user

webhook = starkbank.webhook.delete("6349032133754880")

print(webhook)