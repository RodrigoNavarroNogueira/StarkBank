import starkbank

from src.authentication import user

starkbank.user = user

id_invoice = '4621996717506560'
invoice = starkbank.invoice.get(id_invoice)

print(invoice)
