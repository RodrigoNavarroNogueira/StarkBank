import starkbank

from src.authentication import user

starkbank.user = user

invoices = starkbank.invoice.query(
    after="2020-10-18",
    before="2022-02-25",
    limit=10,
)

for invoice in invoices:
    print(invoice)