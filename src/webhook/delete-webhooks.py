import starkbank

from src.authentication import user

starkbank.user = user

webhook = starkbank.webhook.delete("6113019218100224")

print(webhook)
print('deleted!')
