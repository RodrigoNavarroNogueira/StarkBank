import starkbank

from src.authentication import user

starkbank.user = user

id_invoice = '4594189220184064'
invoice = starkbank.invoice.get(id_invoice)

print(invoice)
