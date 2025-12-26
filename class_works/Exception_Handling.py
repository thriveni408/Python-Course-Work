#To handle ZeroDivisionError

try:
    a=10/0

except ZeroDivisionError:
    print("You can't divide a number with zero")

else:
    print("You have divided successfully")

finally:
    print("End of the try block")

print("rest of the code")

#To handle NameError

try:
    a=b/0

except NameError:
    print("You didn't define the variable")

else:
    print("You have divided successfully")

finally:
    print("End of the try block")

print("rest of the code")


##To handle TypeError

try:
    a=int([1,2,3])

except TypeError:
    print("You can change this data type into other one")

else:
    print("You have divided successfully")

finally:
    print("End of the try block")

print("rest of the code")


#To handle errors in a single line

try:
    a=int([1,2,3])

except (ZeroDivisionError,NameError,TypeError,KeyError,IndexError) as e:
    print("Error Occured:",e)
else:
    print("You have divided successfully")

finally:
    print("End of the try block")

print("rest of the code")


#To handle all kind of errors

try:
    a=a+[1,2,3]

except Exception as e:
    print("Error Occured:",e)
else:
    print("You have divided successfully")

finally:
    print("End of the try block")

print("rest of the code")


#raise keyword
try:
    a=input(input("Enter the number:"))
    if a<0:
        raise Exception("Negative number not allowed")
except Exception as e:
        print("Error Occured:",e)
else:
    print("You have divided successfully")

finally:
    print("End of the try block")

print("rest of the code")


#nested try and except block    
            
try:
    a=input(input("Enter the number:"))
    try:
        a=b/10
    except Exception as e:
        print("Error Occured:",e)
except Exception as e:
    print("Error Occured:",e)


else:
    print("You have divided successfully")

finally:
    print("End of the try block")

print("rest of the code")


    
            


























