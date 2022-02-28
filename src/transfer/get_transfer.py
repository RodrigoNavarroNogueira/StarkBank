import starkbank

from src.authentication import user

starkbank.user = user

transfer = starkbank.transfer.get("6538832094691328")

print(transfer)