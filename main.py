def get_item_price():
  state = input("Enter the abbreviaiton for your state:\n")
  tax_dict = {"NJ":0.066,
             "DE":0.00,
             "OR":0.00,}
  tax_rate = tax_dict[state]
  return tax_rate
  
  # need to get the price of the item
  item_name = input("what item are you buying")
  price = float(input("What is the price of the item"))
  return item_name, price

def calculate_tax(price, tax_rate):
  sales_tax = price * tax_rate
  total = sales_tax + price
  return total, sales_tax