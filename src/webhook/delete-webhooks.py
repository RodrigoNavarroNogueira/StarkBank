import starkbank

from src.authentication import user

starkbank.user = user

webhook = starkbank.webhook.delete("5549320866627584")

print(webhook)
print('deleted!')
