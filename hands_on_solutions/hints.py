import random
def gimme(exercise):
    """
    call this function with the exercise number to get help when you're stuck!
    """
    trying_to_be_funny = ["meaning of life",
                          "what is actually going to make me happy",
                          "What should I do in Bordeaux",
                          "how to spell excercize",
                          "how make the best tahini cookies", "how do zucchini grow",
                          "which country has the most pet cats per capita",
                          "is it worth it to automate this",
                          "card game recommendations", "how to put a train on a boat",
                          "which is the best beach",
                          "what to do in your spare time"]

    if exercise == "1.1":
        hint = "Could np.random.uniform be what you are looking for?"
    elif exercise == "1.2":
        hint = "Write a for loop: at each iteration append a 1 or a 0 to a list."
    elif exercise == "2.1":
        hint = "You access the element like so myarray[i,j]."
    elif exercise == "2.2":
        hint = "To get all elements from one dimension you can use the ':' instead of a number."
    elif exercise == "2.4":
        hint = "Try passing a list in place of a slice to get an irregular subset. For another hint call me with '2.4.2'!"
    elif exercise == "2.42":
        hint = "Slicing also works with multiple colons: '[start:end:step]' or even '[::step]'."
    elif exercise == "2.5":
        hint = "Indexing to set a value works the same way as indexing to get a value. Find the slice you need and set it equal to 1. For another hint call me with '2.5.2'!"
    elif exercise == "2.5.2":
        hint = "For some patterns it may be helpful to do two separate operations of setting sliced indices to one. For another hint call me with '2.5.3'."
    elif exercise == "2.5.3":
        hint = "For the last pattern, consider how you can maybe use the meshgrid function in combination with boolean indexing."
    elif exercise == "2.7":
        hint = "You can use slices to get the value at only every third index [::step]."
    elif exercise == "2.8":
        hint = "The image has a dimension for each color channel. Change only the values in one of them, using a slice, by multiplying them by e.g. 1.5."
    elif exercise == "2.9":
        hint = "Black has the rgb value (0,0,0). For another hint call me with '2.9.2'."
    elif exercise == "2.9.2":
        hint = "This time you want to change all the colors, but only in a part of the picture (only the pixels in a plus shape). For another hint call me with '2.9.3'."
    elif exercise == "2.9.3":
        hint = "Draw the horizontal bar of the plus first. Then in a separate operation draw the vertical bar."
    elif exercise == "2.10":
        hint = "You can look at the saliency by plotting it on top of the image. For another hint call me with '2.10.2'."
    elif exercise == "2.10.2":
        hint = "To look up a bunch of coordinates in an array, pass a list of x and y coordinates like array[y,x]."
    elif exercise == "2.11":
        hint = "np.mgrid and boolean indexing will come in handy! For another hint call me with '2.11.2'."
    elif exercise == "2.11.2":
            hint = "Make a meshgrid where the number zero is in the center for both row and column arrays. Now compute (x)**2 + (y)**2. Lastly, use boolean indexing tp select all cases where the numbers in x and y are smaller than the radius**2 you want."
    elif exercise == "3.1":
            hint = "The subject mean should be the mean of each row. For another hint pass '3.1.2'."
    elif exercise == "3.1.2":
                hint = "Row means are computed with the mean() funtion and the argument axis=1.For another hint pass '3.1.3'."
    elif exercise == "3.1.3":
                hint = "If an array has the wrong dimensions to broadcast for another array you could try adding more dimensions using np.newaxis."
    elif exercise == "4.2":
                hint = "it may be useful to reshape the array. For another hint, pass '4.2.2'."
    elif exercise == "4.2.2":
                hint = "There are many ways of doing this. You could try fancy indexing or maybe read the documentation of `np.chose`."
# -- https://stackoverflow.com/questions/26325652/fastest-way-to-keep-one-element-over-two-from-long-numpy-arrays

    ### NONSENSE
    elif exercise == "meaning of life":
                    hint = "42"
    elif exercise == "what is actually going to make me happy":
                    hint = "Solving these exersises! Also, try asking the reverse question: https://www.goodreads.com/book/show/2863072-the-situation-is-hopeless-but-not-serious"
    elif exercise == "what to do in Bordeaux":
                    hint = "Oysters are a local specialty. Excellent seafood restaurants are just around the corner"
    elif exercise == "how to spell excercize":
                    hint = "exercise"
    elif exercise == "how make the best tahini cookies":
                    hint = "Its pretty much like making Shortbread, so the butter needs to be a little cold. \n 100g Tahini\nA bit of Salt\n75g Butter\n70g Sugar\n100g Flour\n75g ground almonds\nSesame seeds - for the looking-yummy-factor\n Set the oven to ~170°C. Mix butter, salt and sugar. Don't go too easy on the salt - I love the sweet and salty thing :)Then add flour and almonds. Mix mix mix mix. Once it has become a cumbly mass, add the tahini. You might need some water to smoothen the consistency. Roll it into balls, throw the balls into the sesame seeds. Place on the tray and then bake for 10-15min."
    elif exercise == "how do zucchini grow":
                        hint = "Every plant produces male and female flowers. Insects need to transport pollen from a male to a female flower to fertilize it."
    elif exercise == "which country has the most pet cats per capita":
                        hint = "New Zealand"
    elif exercise == "is it worth it to automate this":
                        hint = "https://xkcd.com/1205/"
    elif exercise == "card game recommendations":
                        hint = "Play Exploding Kittens!"
    elif exercise == "how to put a train on a boat":
                        hint = "I dont know, but go and talk to Tiziano about it!"
    elif exercise == "which is the best beach":
                        hint = "I heard Arcachon is pretty nice!"
    elif exercise == "what to do in your spare time":
                        hint = "Get involved in organzizng ASPP 2022!"

    else:
        q = random.choice(trying_to_be_funny)
        hint = f"I don't know anything about this one! Try asking about another exercise or how about some advice on '{q}'?"

    print(hint)
