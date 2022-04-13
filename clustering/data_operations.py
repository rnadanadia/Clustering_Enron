import os
import pandas as pd
from email.parser import Parser
"""
A File to handle all data operations.

"""

class Preprocessing():
    """
    A class that manage all preprocessing operations.

    """

    def __init__(self) -> None:
        pass

    def all_data_to_csv(self):
        """
        A function that convert all emails to csv file.

        """
        print('Converting all emails to csv file...')
        mail_from = []
        mail_to = []
        mail_cc = []
        mail_subject = []
        mail_body = []
        mail_date = []
        errorlist = []

        for dir, folders, filenames in os.walk("./data/maildir"):
            for filename in filenames:
                print(filename)
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
                            mail_body.append(self.get_raw_text(parsed_mail))
                        else:
                            mail_body.append('')
                        mail_date.append(parsed_mail['date'])
                    except:
                        errorlist.append(fullpath)

        if len(errorlist) > 0:
            print('Error txt files was generated')
            with open('./error_list.txt', 'w') as f:
                for item in errorlist:
                    f.write("%s\n" % item)

        print('Starting to remove comma from data...')
        mail_from = self.remove_comma(mail_from)
        mail_to = self.remove_comma(mail_to)
        mail_cc = self.remove_comma(mail_cc)
        mail_subject = self.remove_comma(mail_subject)
        mail_date = self.remove_comma(mail_date)
        mail_body = self.remove_comma(mail_body)
        print('Finished removing comma from data...')

        print('Starting to save data to csv file...')
        mail_dict = {"from": mail_from, "to": mail_to, "cc": mail_cc, "subject": mail_subject, "date": mail_date, "body": mail_body}
        mail_df = pd.DataFrame(mail_dict)
        mail_df.to_csv(".data/emails.csv", index=False, sep=";")
        print('Finished saving data to csv file...')

    def get_raw_text(self, emails):
        """
        A function to get raw text from emails.

        :param emails: A list of emails.
        :return: A list of raw text.
        """
        email_text = []
        for email in emails.walk():
            if email.get_content_type() == 'text/plain':
                email_text.append(email.get_payload())
        return ''.join(email_text)

    def remove_comma(self, thislist):
        """
        A function to remove comma from list.

        :param thislist: A list of emails.
        :return: A list of emails without comma.
        """
        for i in range(len(thislist)):
            if thislist[i] is not None:
                thislist[i] = thislist[i].replace(';', ' ')
        return thislist

    @staticmethod
    def create_sample_csv(sample_prcentage: float = 0.1):
        """
        A function to create sample csv file.

        :param sample_prcentage: A float number to define sample size.
        """
        print('Starting to create sample csv file...')
        mail_df = pd.read_csv("./data/emails.csv", sep=";")
        mail_df = mail_df.sample(frac=sample_prcentage)
        mail_df.to_csv("./data/sample.csv", index=False, sep=";")
        print('Finished creating sample csv file...')

# Test sample
# preprocessing = Preprocessing()
# preprocessing.all_data_to_csv()

# Preprocessing.create_sample_csv()
