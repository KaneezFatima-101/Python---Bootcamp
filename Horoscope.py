next = True
while (next == True):
    print(''' Today's Horoscope
    1. Aquarius
    2. Pisces
    3. Aries
    4. Taurus
    5. Gemini
    6. Cancer
    7. Leo
    8. Virgo
    9. Libra
    10. Scorpio
    11. Sagittarius
    12. Capricorn
    ''')

    num = int(input("Enter the number of your sign: "))

    if num == 1:
        print("Hi, Aquarius\n"
            "This might seem like a typical day early on, but as each hour goes by, you could start to see more and more\n"
            "mysterious actions and events cropping up. Who are the perpetrators? What are they up to!? If you look beneath\n"
            "the surface, you will start to see a pattern and an agenda. This is something exciting, and you should not ignore\n"
            "it. Try to get involved in their shenanigans and you will have a lot of fun. They could use a bright, witty """
            "person like you!")
    elif num == 2:
        print("Hi, Pisces\n"
            "A relationship that you thought was broken beyond all repair still has some life in it. Figure out how you can\n"
            "put it on the road to recovery. There are two people involved in this messy situation, and each of you has your\n"""
            "own apologies to make. Be a hero and be the first one to extend an olive branch. Call or e-mail them today.\n"
            "Let them know you're thinking about them and be honest about how you feel. Let down your guard and speak from the heart.")
    elif num == 3:
        print("Hi, Aries\n"
              "Accidents are called accidents for a reason. They happen through no one person's concerted efforts. They just\n"
              "happen. If you are involved in a fender bender or any other type of collision (real or metaphorical), avoid taking\n"
              "it personally. Things happen, and every time you can let the stress roll off of your back, you grow and learn.\n"
              "Of course, if you are in a situation where you know someone is working against you, you should feel free to unsheath\n"
              "your claws.")
    elif num == 4:
        print("Hi, Taurus\n"
              "The art of flirtation takes a lot of time to learn, but you are becoming quite an expert. It's time to stop \n"
              "holding back and start using those killer skills you have learned! If you have someone in your sights, romantically \n"
              "speaking, today is the day to make that connection. Ask a pertinent question or two and help them see you in a \n"
              "new light. If you are currently in a relationship, get ready for things to go to a much hotter level.")
    elif num == 5:
        print("Hi, Gemini\n"
              "You need to know where to go for the information that will help you most in life. Instead of asking friends for \n"
              "advice on how to fatten up your rapidly thinning piggy bank, ask an expert. Friends are who you should talk to \n"
              "about your love life, work hassles, and other personal issues. But when it comes to credit, investments, and your \n"
              "savings account, you don't want to mix those two worlds. Sharing too much about how much money you make or have \n"
              "could also create unnecessary friction.")
    elif num == 6:
        print("Hi, Cancer \n"
              "Get out your finest fine-toothed comb because you'll need to go over some very fine print one more time. There \n"
              "are an awful lot of small details that could grow into big, embarrassing issues later on down the line if you don't\n"
              "nip them in the bud now. Probably the last thing you want to do is proofread or double-check your work one more \n"
              "time, but you should do it. It will save you a lot more of your time (and your pride) in the long run.")
    elif num == 7:
        print("Hi, Leo\n"
              "Despite the fact that you're feeling better than you have in a while, right now is not the time to go out and \n"
              "celebrate. You are not overly impulsive as a rule, but today you should behave even more conservatively than usual. \n"
              "Bide your time and the right opportunity to have a blast will present itself soon enough. Skip any splurges and \n"
              "stay close to home. You can have just as celebratory a time cuddled up with a good book or your partner as you \n"
              "can at a big party.")
    elif num == 8:
        print("Hi, Virgo \n"
              "Today is a great day to try a new food, hobby, sport, or adventure that you have always been just a little to \n"
              "scared to try before. Your fears are starting to vanish and your courage is growing, in part because your mind \n"
              "is hungry for new stimulation—even if that stimulation is based on fear! You will be totally fiery and full of \n"
              "energy, so put it to good use by pushing the envelope and pushing past one or two of the boundaries you've built \n"
              "for yourself.")
    elif num == 9:
        print("Hi, Libra\n"
              "If you are stuck in the middle of a dilemma right now, doing something that you think is right (even if you aren't \n"
              "totally sure it's right) is better than doing nothing at all. Stop trying to nail down every single detail. You \n"
              "can't eliminate every potential problem. It's time to start acting! Things are never going to be perfect, so if \n"
              "you're waiting until they are, you will be waiting a very long time—too long, in fact. You need to keep moving \n"
              "even if you don't know exactly where you're going.")
    elif num == 10:
        print("Hi, Scorpio\n"
              "Can you have too many friends? The answer, you may be beginning to fear, is yes! There are only so many free \n"
              "hours in your week, and it might be getting tough to prioritize who gets to share them with you. Friendships \n"
              "take as much work as anything else does, but the payoff is truly rewarding. See what you can do to show your \n"
              "friends how much you care.")
    elif num == 11:
        print("Hi, Sagittarius\n"
              "The people you associate with today will be very important. Some people will seem to be right on your wavelength, \n"
              "but others may drive you absolutely crazy! As soon as you feel that someone is rubbing you the wrong way, distance \n"
              "yourself from them. You aren't in the right frame of mind to deal with feeding people's egos or sacrificing your \n"
              "own desires. What you need now is to be surrounded by people who get you, the people who use the same shorthand you use.")
    elif num == 12:
        print("Hi, Capricorn\n"
              "Are you running the risk of getting too big for your britches? Just in case, you should give yourself a reality \n"
              "check today before someone else does! Make an effort to get more grounded. Spend time with people who live a \n"
              "different lifestyle. Get a glimpse of what their biggest issues, goals, and concerns are. Just a little bit of \n"
              "effort will wake you up to the reality of your situation and make you much more grateful for what you have.")
    else:
        print("Have you entered the correct number??")

    cont = input("Do you want to continue (Y/N)??\n")
    if cont == 'y' or cont == 'Y':
        next = True
    else:
        next = False