from main.routes.security.token import TokenFactory as TF
from jose import jwt

TOKEN_SECRET_KEY = 'dktokentestkey'
TOKEN_ALGORITM = 'HS256'

'''
Verifies that the create_token method creates a token with the given fields
'''
def test_create_token ():
    data = {"test":"name", "snack":"gummy"}

    result_token = TF.create_token(data=data)

    result_decoded = jwt.decode(result_token, key=TOKEN_SECRET_KEY, algorithms=TOKEN_ALGORITM)

    assert result_decoded["test"] != None 
    assert result_decoded["snack"] != None
    assert result_decoded["exp"] != None
