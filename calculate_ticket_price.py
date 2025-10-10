def calculate_ticket_price(age, is_member):
  if age < 0 or age > 120:
    return "Invalid"

  price = 100000

  if age <= 12:
    price *= 0.5
  elif age >= 60:
    price *= 0.7

  if is_member:
    price *= 0.9

  return int(price)
