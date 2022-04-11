from email.parser import Parser
import os
import pandas as pd

mail_from = []
mail_to = []
mail_cc = []
mail_subject = []
mail_body = []
mail_date = []
errorlist = []

for dir, folders, filenames in os.walk("./maildir"):
    for filename in filenames:
        fullpath = os.path.join(dir, filename)
        with open(fullpath, "r") as f:
            try:
                maildata = f.read()
                parsed_mail = Parser().parsestr(maildata)
                mail_from.append(parsed_mail['from'])
                mail_to.append(parsed_mail['to'])
                mail_cc.append(parsed_mail['cc'])
                mail_subject.append(parsed_mail['subject'])
                mail_body.append(parsed_mail.get_payload())
                mail_date.append(parsed_mail['date'])
            except:
                errorlist.append(fullpath)

with open('./error_list.txt', 'w') as f:
    for item in errorlist:
        f.write("%s\n" % item)

mail_dict = {"from": mail_from, "to": mail_to, "cc": mail_cc, "subject": mail_subject, "body": mail_body, "date": mail_date}
mail_df = pd.DataFrame(mail_dict)
mail_df.to_csv("./emails.csv", index=False)
