import  yagmail
import os
import time

sender = 'namtranwechs@gmail.com'
receiver = 'trannam21593@gmail.com'

subject = "This is the subject"

contents = """
Here is the content of the email
Hi!
"""

while True:
  yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
  yag.send(to=receiver, subject=subject, contents=contents)

  print("Email Sent!\n")
  time.sleep(60)