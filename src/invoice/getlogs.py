import starkbank

from src.authentication import user

starkbank.user = user

log = starkbank.invoice.log.get("5673227409948672")

print(log)