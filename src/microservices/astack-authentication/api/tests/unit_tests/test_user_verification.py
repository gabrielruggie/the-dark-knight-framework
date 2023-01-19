from main.utilities.verify_user_credentials import VerifyUserFactory as factory

'''
Verifies that only passwords with both an uppercase letter and number are accepted
'''
def test_verify_correct_password ():
    correct_pw = "hell0World"
    too_short_pw = "hel0Wd"
    no_uppercase_let = "hell0world"
    no_number = "helloWorld"
    all_lowercase = "helloworld"

    assert factory.verify_correct_password(correct_pw) == True
    assert factory.verify_correct_password(too_short_pw) == False 
    assert factory.verify_correct_password(no_uppercase_let) == False 
    assert factory.verify_correct_password(no_number) == False
    assert factory.verify_correct_password(all_lowercase) == False

'''
Verifies that only valid emails are accepted
'''
def test_verify_email ():
    valid_email1 = "gruggie77@gmail.com"
    valid_email2 = "gruggie@gmail.com"
    valid_email3 = "GRUGGIE@AOL.net"
    invalid_email1 = "gruggiegmail.com"
    invalid_email2 = "@gmail.com"
    invalid_email3 = "gruggie@gmail"
    invalid_email4 = "gruggie@gmail.darknet"

    assert factory.verify_email(valid_email1) == True
    assert factory.verify_email(valid_email2) == True
    assert factory.verify_email(valid_email3) == True
    assert factory.verify_email(invalid_email1) == False
    assert factory.verify_email(invalid_email2) == False
    assert factory.verify_email(invalid_email3) == False
    assert factory.verify_email(invalid_email4) == False
     
