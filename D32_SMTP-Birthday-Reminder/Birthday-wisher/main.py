import random
import datetime as dt
import pandas
import smtplib

my_email = "h100dayspythontestingnow@hotmail.com"
password = "fttmldXXXXXXXXXXXXck"  # get info from google keep
##################### Extra Hard Starting Project ######################
LETTERFILES = {1: "D32_SMTP-Birthday-Reminder/Birthday-wisher/letter_templates/letter_1.txt",
               2: "D32_SMTP-Birthday-Reminder/Birthday-wisher/letter_templates/letter_2.txt",
               3: "D32_SMTP-Birthday-Reminder/Birthday-wisher/letter_templates/letter_3.txt"}


# 1. Update the birthdays.csv
# done

today = (dt.datetime.now().month, dt.datetime.now().day)
print(today)


data = pandas.read_csv(
    "D32_SMTP-Birthday-Reminder/Birthday-wisher/birthdays.csv")

birthdays_dict = {(datarow["month"], datarow["day"]): datarow
                  for (index, datarow) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    letter_to_use = LETTERFILES[random.randint(1, 3)]
    print(letter_to_use)
# 4. Send the letter generated in step 3 to that person's email address.
    with open(letter_to_use, "r") as letter:
        # letter.read() returns a STR, while letter.readlines() return a list
        letter_contents = letter.read()
        letter_contents = letter_contents .replace(
            "[NAME]", birthday_person["name"])
        print(letter_contents)
        # print(type(letter_contents))
        with smtplib.SMTP("smtp.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            # to_addrs should be birthday_person["email"]
            # I am using the testing email in the meantime
            connection.sendmail(from_addr=my_email,
                                to_addrs="h100dayspythontestingnow@myyahoo.com",
                                msg=f"Subject:Hey! Happy Birthday\n\n{letter_contents}")
            print("mail sent")
