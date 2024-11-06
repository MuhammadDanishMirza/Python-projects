v = 0


def check_email(email):
    global v
    j, k, l = 0, 0, 0

    if "@" in email:
        if email.count('@') == 1:
            local_part, domain_part = email.split("@")
            if len(local_part) > 6:
                if local_part[0].isalpha():
                    for i in local_part:
                        if i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isspace():
                            k = 1
                        elif i == '.' or i == '_' or i == '-' or i == '(' or i == ')' or i == ',' or i.isdigit() or i == '"':
                            continue
                        else:
                            l = 1

                    if j == 1:
                        print("You cannot enter the uppercase letter in your email address")

                    if k == 1:
                        print("You cannot enter space in your email address")

                    if l == 1:
                        print("You cannot Enter the special characters [excluding.- _ @ ( ) , ]")

                    if j == 0 and k == 0 and l == 0:
                        if domain_part == 'gmail.com' or domain_part == 'outlook.com' or domain_part == 'hotmail.com':
                            v = 3
                else:
                    print("First letter should be alphabet not digit")
            else:
                print("Your email should be greater than 16 characters")
        else:
            print("You should include @ in your email address only one time")
    else:
        print("You should include @ in your email address")


while True:
    # email is in small caps 
    # gmail.com should be added
    # must be greater than 16 characters including gmail.com
    # first character should not be digit 
    # @ should be occurred at lest one
    # @ should not be occurred more than one time
    # email should not include characters like !#$%^&*+=|\{[]}?/><:;"*-+/"
    # email should not contain spaces
    print("Enter 'quit' at any time time to exit the program")
    email = input("Please Enter Your Email Address: ")

    check_email(email)
    if v == 3 or email.lower() == "quit":
        break

print("Your Email is verified You entered correct email.")
print("------------Email Validation finished-----------")
