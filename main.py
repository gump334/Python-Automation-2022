import yagmail
import os
#import time
#import schedule
import pandas


def send_email():
  sender = "blackcloudgeeks@gmail.com"


  subject = "This is a python test"

  contents = """
  Hello, This is my first python code for this week.
  """
  df = pandas.read_csv('contacts.csv')
  print(df)
  # for 
  # yag = yagmail.SMTP(user=sender, password=os.getenv("WINPASSWORD"))
  # yag.send(to=receiver,subject=subject, contents=contents)
  # print("Email Sent!!!")


# schedule.every(1).minutes.do(send_email)
# while True:
#   schedule.run_pending()
#   #time.sleep(1)
  


    