from models.borrower import Borrower

b = Borrower()
data = {}
data['national_code'] = '026000000'
data['first_name'] = 'armin'
data['last_name'] = 'rezaei'
data['father_name'] = 'kamal'
data['birth_date'] = '2020-01-01'
data['phone'] = "02177777777"
data['mobile'] = "09390000000"
data['address'] = "teh"
data['postal_code'] = "5555555555"
b.create(data)
