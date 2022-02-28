import starkbank

from src.authentication import user

starkbank.user = user

webhook = starkbank.webhook.get("6373426172264448")

print(webhook)