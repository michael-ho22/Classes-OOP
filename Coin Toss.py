import CoinClass as c # first line is always import name of the file


# The main function.
def main():
       # Create an object from the Coin class.
          # this creates an instance called 'my_coin' of the class 'Coin()'
       my_coin = c.Coin()
       # my_coin is the actualy object, c.coin is the blueprint
       
       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           
           my_coin.__sideup = 'Heads' #__ hides the attributes, so even if you try to change here, it won't effect anything

           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           


       

# Call the main function.

main()
