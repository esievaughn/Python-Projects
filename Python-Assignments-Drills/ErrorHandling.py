

def getinfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return var1,var2


def compute():
    go = True
    while go:           #while cycles back through question after error, so user can still input code instead of having the program stop completely
        var1,var2 = getinfo()
        try: 
            var3 = int(var1) + int(var2) 
            go = False
        except ValueError as e:          #catch for ValueError; e is added to ValueError to display an internal error code
            print("{}: \n\You did not provide a numeric value.".format(e)) #try block provides an error message to user if user input wrong data--in this case, string instead of int
        except:                 #error that may not have predicted; \n\--doubles slash is two lines down; ensures string goes on next line
            ("\n\Oops, you provided invalid input, program will close now.")
    print("{} + {} = {}".format(var1,var2,var3))



        


if __name__ == "__main__":
    compute()#calls compute because the getinfo() function is called within the while loop
