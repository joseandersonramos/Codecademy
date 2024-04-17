# 👧Aisha's Greetings Project
# José Anderson Ramos Aquino 4/16/2024

from contextlib import contextmanager

# Personalized greeting cards
class Personalized:
  def __init__(self, sender, receiver):
    self.sender = sender
    self.receiver = receiver
    self.personalized_card = open(f'{sender}_personalized.txt', 'w')
  
  def __enter__(self):
    self.personalized_card.write(f'Dear {self.receiver}\n')
    return self.personalized_card

  def __exit__(self, *exc):
    self.personalized_card.write(f'\nSincerely, {self.sender}')
    self.personalized_card.close()

# Generic greeting cards
@contextmanager
def generic(card_type, sender, recipient):

  template_card = open(card_type)
  new_card = open(f'{sender}_generic.txt', 'w')

  try:
    new_card.write(f'Dear {recipient}\n')
    new_card.write(f'{template_card.read()}\n')
    new_card.write(f'Sincerely, {sender}')
    yield new_card
  
  finally:
    new_card.close()
    template_card.close()

# Generic thank you card (Customer Mwenda)
with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as customer1_card:
  print('Mwenda Card Generated!')

# Verify that the order was printed
print()
with open('Mwenda_generic.txt') as card:
  print(card.read())

# Personalized greeting card (Customer Jhon)
with Personalized('Jhon', 'Michael') as personalized_card:

  jhons_message = "I am so proud of you! Being your friend for all these years has been nothing but a blessing. \
  I don't say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always."

  personalized_card.write(jhons_message)
  print('\nJhon Card Generated!')

print()
with open('Jhon_personalized.txt') as card:
  print(card.read())

# Generic happy birthday card and personalized card (Customer Josiah)
with generic('happy_bday.txt', 'Josiah', 'Remy') as colleague_card, Personalized('Josiah', 'Esther') as sister_card:

  josiahs_message = "Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a \
  pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!"

  sister_card.write(josiahs_message)
  print('\nJosiah Cards Generated!\n')

with open('Josiah_generic.txt') as colleague_card, open('Josiah_personalized.txt') as sister_card:
  print(colleague_card.read())
  print()
  print(sister_card.read())
