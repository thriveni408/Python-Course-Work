data={'leela@gmail.com':1234,
      'chintu@gmail,com':5678,
      'thriveni@gmail.com':9012
      }
mail=input("Enter the mail: ")
pwd=int(input("Enter the Password: "))

if data.get(mail)==pwd:
    print("Valid Login")
else:
    print("Invalid Login")