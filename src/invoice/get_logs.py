import starkbank

from src.authentication import user

starkbank.user = user

log = starkbank.invoice.log.get("5219354056589312")

print(log)