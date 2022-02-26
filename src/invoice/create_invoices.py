from datetime import datetime, timedelta

import starkbank

from src.authentication import user

starkbank.user = user

def create_invoice():
    invoices = starkbank.invoice.create([
        starkbank.Invoice(
            amount=248,
            descriptions=[{'key': 'Arya', 'value': 'Not today'}],
            discounts=[{'percentage': 10, 'due': datetime.now()+timedelta(days=10)}],
            due=datetime.now()+timedelta(days=10),
            expiration=123456789,
            fine=2.5,
            interest=1.3,
            name="Ed Supremo",
            tags=['New sword', 'Invoice #1234'],
            tax_id="29.176.331/0001-69"
        )
    ])
    return invoices

for invoice in invoices:
   print(invoices)
