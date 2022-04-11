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

def get_raw_text(emails):
    email_text = []
    for email in emails.walk():
        if email.get_content_type() == 'text/plain':
            email_text.append(email.get_payload())
    return ''.join(email_text)

for dir, folders, filenames in os.walk("./maildir"):
    for filename in filenames:
        fullpath = os.path.join(dir, filename)
        with open(fullpath, "r") as f:
            try:
                maildata = f.read()
                parsed_mail = Parser().parsestr(maildata)
                mail_from.append(parsed_mail['From'])
                mail_to.append(parsed_mail['To'])
                mail_cc.append(parsed_mail['Cc'])
                mail_subject.append(parsed_mail['subject'])
                if parsed_mail.get_content_type() == 'text/plain':
                    mail_body.append(get_raw_text(parsed_mail))
                else:
                    mail_body.append('')
                mail_date.append(parsed_mail['date'])
            except:
                errorlist.append(fullpath)

if len(errorlist) > 0:
    with open('./error_list.txt', 'w') as f:
        for item in errorlist:
            f.write("%s\n" % item)

def remove_comma(thislist):
    for i in range(len(thislist)):
        if thislist[i] is not None:
            thislist[i] = thislist[i].replace(';', ' ')
    return thislist

mail_from = remove_comma(mail_from)
mail_to = remove_comma(mail_to)
mail_cc = remove_comma(mail_cc)
mail_subject = remove_comma(mail_subject)
mail_date = remove_comma(mail_date)
mail_body = remove_comma(mail_body)


mail_dict = {"from": mail_from, "to": mail_to, "cc": mail_cc, "subject": mail_subject, "date": mail_date, "body": mail_body}
mail_df = pd.DataFrame(mail_dict)
mail_df.to_csv("./emails.csv", index=False, sep=";")
print(mail_df)