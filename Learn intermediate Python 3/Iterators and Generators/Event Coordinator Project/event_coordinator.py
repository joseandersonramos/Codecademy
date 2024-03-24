# 👨‍💼 Event Coordinator Project 👨‍🍳🍽 
# José Anderson Ramos Aquino 03-23-2024
# Working with generators

# Keep the guest_list by default
with open('guest_list.txt', 'w') as file:
  file.write(
"""Tim,22
Tonya,45
Mary,12
Ann,32
Beth,20
Sam,5
Manny,76
Kenton,15
Kenny,27
Dixie,46
Mallory,32
Julian,4
Edward,71
Rose,65"""
)

# Start
guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break

    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age

    line_data = yield name

    # Add a 'name,age' to the guestlist
    if line_data != None:
      text_file.close()
      with open(file_name, 'a') as text_file:
        text_file.write('\n' + line_data)
      text_file = open(file_name,'r')

# Table generators
def table_1(num_seat):
  for seat in range(1, num_seat + 1):
    yield ('Chicken', 'Table 1', 'Seat ' + str(seat))

def table_2(num_seat):
  for seat in range(1, num_seat + 1):
    yield ('Beef', 'Table 2', 'Seat ' + str(seat))

def table_3(num_seat):
  for seat in range(1, num_seat + 1):
    yield ('Fish', 'Table 3', 'Seat ' + str(seat))

# Connected table generator
def combine_tables():
  print('\n\"Meal for table 1\"\n')
  yield from table_1(5)
  print('\n\"Meal for table 2\"\n')
  yield from table_2(5)
  print('\n\"Meal for table 3\"\n')
  yield from table_3(5)

# Assign a table and seat to each guest generator
def assign_seat_to_guest(guests, tables):
  for name in guests:
    yield (name, next(tables))

# Print all the guests in the guestlist
read_guestlist_generator = read_guestlist('guest_list.txt')

print('\"All the guests in the guestlist\"\n')
print(next(read_guestlist_generator)) # Start the generator
read_guestlist_generator.send('Jane,35') # Add Jane
for name in read_guestlist_generator: # Print all the guests
  print(name)

# Print all the guests who are 21 and over
guests_21_and_over_generator = (name for name in guests if guests[name] >= 21)

print('\n\"Names of all guests who are 21 and over\"\n')
for name in guests_21_and_over_generator:
  print(name)

# Assign meals to each table
tables_generator = combine_tables()
for table in tables_generator:
  print(table)

# Assign a table and seat to each guest
assign_seat_to_guest_generator = assign_seat_to_guest(guests, combine_tables())

print('\n\"Assign a table and seat to each guest\"')
for guest in assign_seat_to_guest_generator:
  print(guest)
