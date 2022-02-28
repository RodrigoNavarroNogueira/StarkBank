import starkbank

from src.authentication import user

starkbank.user = user

webhook = starkbank.webhook.delete("5267593728360448")

print(webhook)
print('deleted!')
