





main()


def main () :
    x = input("Enter a number: ")
    while (True):

        try:
            x = int(x)
            return x
        except ValueError:
                print("Please enter a valid integer")


