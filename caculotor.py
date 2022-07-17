"""secret_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("Yay good job. ")
        break
else:
    print("Sorry you lost")"""



"""income = int(input("What is your income: "))
credit_score = int(input("What is your credit score: "))

if income >= 150000 and credit_score >= 180:
    print("You are eligble for a loan.")
else:
    ("You are not eligble for a loan.")"""
#print("Type help to get the game started.")

"""command = ("")
while True:
    command = input("> ")
    if command == "start":
        print("The car has started.")
    elif command == "stop":
        print("The car has stopped")
    elif command == "help":
        print(
       # Start - to start the car
        #Stop - to stop the car
       # Quit - to exit the car
        )
    elif command == "quit":
        break
    else:
       print("Sorry I didn't get that")"""


"""def main():
    word = input("Please enter a word or number: ")
    palindrome = True
    even_odd = len(word) % 2
    word_len = 0
    if(even_odd):
        word_len = len(word) // 2
    else:
        word_len = int(len(word) / 2)
    for i in range(word_len):
        if(word[i] != word[(0 - len(word)) + (len(word) - i) - 1]):
            palindrome = False
            break
    if(palindrome):
        print(word, "is a palidrome")
    else:
        print(word, "is not a palindrome")
    return
if __name__ == "__main__":
    main()"""

import turtle
t=turtle.Pen()
t.penup()
t.speed(0)
turtle.bgcolor('black')
# Ask the user for the number of sides, default to 4, min 2, max 6
sides = int(turtle.numinput("Number of sides",
            "How many sides in your spiral?", 4,2,6))
colors=["red", "yellow", "blue", "green", "purple", "orange"]
# Our outer spiral loop
for m in range(1,60):
    t.forward(m*4)
    t.width(m//25+1)
    position = t.position() # remember this corner of the spiral
    heading = t.heading()   # remember the direction we were heading
    # Our 'inner' spiral loop,
    # draws a little rosette at each corner of the big spiral
    if (m % 2 == 0):
        for n in range(sides):
            t.pendown()
            t.pencolor(colors[n%sides])
            t.circle(m/4)
            t.right(360/sides - 2)
            t.penup()
    # OR, draws a little spiral at each corner of the big spiral
    else:
        for n in range(3,m):
            t.pendown()
            t.pencolor(colors[n%sides])
            t.forward(n*2/3)
            t.right(360/sides - 2)
            t.penup()
    t.setpos(position)      # reset the position on the big spiral
    t.setheading(heading)   # point in the big spirals direction/heading
    t.left(360/sides + 2)   # move to the next point on the big spiral





