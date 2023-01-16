# salutation = 'Mr.'
# name = 'Kwon'
# product = 'Gun', verbed = ' ', room = 'house', animals = 'tiger', amount = '1,000$', spokesman = 'Kim', job_title = 'owner', percent = '70'

letter = 'Dear {salutation} {name}, \n' \
         'Thank you for your letter. \n' \
         'We are sorry that our {product} {verbed} in your {room}. \n' \
         'Please note that it should never be used in a {room}, especially near nay {animals}. \n' \
         'Send us your receipt and {amount} for shipping and handling. \n' \
         'We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}. \n' \
         'Thank you for your support. Sincerely, {spokesman} {job_title} \n'\
         .format(salutation = 'Mr', name = 'Kwon', product = 'Gun', verbed = ' ', room = 'house', animals = 'tiger', amount = '1,000$', spokesman = 'Kim', job_title = 'owner', percent = '70')
print(letter)