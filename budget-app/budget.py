import math

class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    cat_len = len(self.name)
    side = (30-cat_len)//2
    out_string = ""
    out_string += side*"*"+self.name+side*"*"+"\n"
    for i in self.ledger:
      #check len of description only first 23 characters should be displayed
      #
      if len(i["description"]) > 23:
        new_desc = i["description"][:23]
        #print(len(new_desc))
      else:
        new_desc = i["description"]
      if "." in str(i["amount"]):
        space =30-(len(new_desc)+ len(str(i["amount"])))
        out_string += ("{}{}{}".format(new_desc,space*" ",i["amount"]))
      else:
        space =30- (len(new_desc)+ len(str(i["amount"]))+3)
        out_string += ("{}{}{}.00".format(new_desc,space*" ",i["amount"]))
      out_string += "\n"
    out_string += "Total: {}".format(self.get_balance())
    return out_string 

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for i in self.ledger:
      balance += i["amount"]
    return balance

  def transfer(self,  amount,category):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to {}".format(category.name))
      category.deposit(amount,"Transfer from {}".format(self.name))
      return True
    else:
      return False

  def check_funds(self, amount):
     
    if self.get_balance() < amount:
      return False
    else:
      return True

def round_down(num, divisor=10):
    return num - (num%divisor)

def create_spend_chart(categories):
  """
  @args list containing categories
  """
  total_spending = 0
  ## using to get the total from each categorie to calculate the percentage
  for categorie in categories:
    for item in categorie.ledger:
      #only get the spending
      if item["amount"] < 0:
        total_spending += item["amount"]*(-1)


  percent_arr = []
  name_arr = []
  print_string = ""
  for categorie in categories:
    temp_total = 0
    name_arr.append(categorie.name)
    for item in categorie.ledger:
      if item["amount"] < 0:
        temp_total += item["amount"]*(-1)
    
    #percentage of total math.floor
    #print(round(((temp_total/total_spending)*100)/10,-1))
    #
    #print(int(round_down((temp_total/total_spending)*100)))
    percent_arr.append(int(round_down((temp_total/total_spending)*100)))
  #print(name_arr, percent_arr)
  print_string += ("Percentage spent by category\n")
  for i in range(10,-1, -1):
    if i < 10:
      if i == 0:
        print_string += "  {}|".format(i*10)
      else:
        print_string += " {}|".format(i*10)
    else:
      print_string += "{}|".format(i*10)
    for num in percent_arr:
      if num >= i*10:
        print_string += " o "
      else:
        print_string += "   "
      
    print_string += " \n"
    #print(print_string)


  print_string += ("    {}-\n".format(len(name_arr)*"---"))
  #get longest string then use a while loop to iterate over each one
  longest_string = max(name_arr, key=len)
  name_arr = [i.capitalize() for i in name_arr]
  count = 0
  while len(longest_string) != count:
    print_string += "    "
    for word in name_arr:
      if len(word) == len(longest_string):
        
        print_string += " {} ".format(word[count])

      elif len(word) < count+1:
        print_string += "   "
      else:
        print_string += " {} ".format(word[count])

    count += 1
    print_string += " "
    print_string += "\n"
    #print(print_string)
  
  #print(len(print_string))
  print_string = print_string[:-1]
  return print_string
