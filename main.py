import yagmail
import os 
sender = ""
receiver = """


subject = "This is a python test"

contents = """
Hello, This is my first python code for this week.
""" 

yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))
yag.send(to=receiver,subject=subject, contents=contents)
print("Email Sent!!!")