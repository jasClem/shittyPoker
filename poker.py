import random


class Card(object):
    # Create Card Class

    cardRanks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    # Create card rank variables

    cardSuits = ('♠', '♦', '♥', '♣')
    # Create card suit variables

    def __init__(self, rank, suit):
        # Initialize card attributes

        self.rank = rank
        # Create rank

        self.suit = suit
        # Create suit

    def __str__(self):
        # Define card strength

        if self.rank == 11:
            rank = 'J'
            # Create Jack

        elif self.rank == 12:
            rank = 'Q'
            # Create Queen

        elif self.rank == 13:
            rank = 'K'
            # Create Elvis

        elif self.rank == 14:
            rank = 'A'
            # Create Ace

        else:
            rank = self.rank
            # Create Number cards

        return str(rank) + self.suit
        # Return card rank and suit

    def __eq__(self, other):
        return self.rank == other.rank
        # Define card rank equal to

    def __ne__(self, other):
        return self.rank != other.rank
        # Define card rank does not equal

    def __lt__(self, other):
        return self.rank < other.rank
        # Define card rank less than

    def __le__(self, other):
        return self.rank <= other.rank
        # Define card rank less than equal

    def __gt__(self, other):
        return self.rank > other.rank
        # Define card rank greater than

    def __ge__(self, other):
        return self.rank >= other.rank
        # Define card rank greater than equal


class Deck(object):
    # Create Deck Class

    def __init__(self):
        # Initialize deck attributes

        self.deck = []
        # Create deck

        for suit in Card.cardSuits:
            for rank in Card.cardRanks:
                card = Card(rank, suit)
                self.deck.append(card)
                # For each suit & rank, add a card to the deck

    def shuffle(self):
        # Define shuffle

        random.shuffle(self.deck)
        # Shuffle deck

    def __len__(self):
        # Define deck size

        return len(self.deck)
        # Return deck size

    def deal(self):
        # Define dealing cards

        if len(self) == 0:
            return None
        # Check for cards

        else:
            return self.deck.pop(0)
        # Deal cards


class Poker(object):
    # Create Poker Class

    def __init__(self, numHands):
        # Initialize poker attributes

        self.deck = Deck()
        # Create new deck

        self.deck.shuffle()
        # Shuffle deck

        self.hands = []
        # Create list of hands

        self.totalPoints = []
        # Create a list to store total_point

        cardsPerHand = 5
        # Set number of cards in each hand

        for i in range(numHands):
            hand = []
            # Create each hand

            for j in range(cardsPerHand):
                hand.append(self.deck.deal())
                # Deal cards to each hand

            self.hands.append(hand)
            # Add cards to hand


    def play(self):
        # Define gameplay

        for i in range(len(self.hands)):
            sortedHand = sorted(self.hands[i], reverse=True)
            # Sort hand high to low

            hand = ""
            # Create
            for card in sortedHand:
                hand = hand + str(card) + " "
            print("Hand " + str(i + 1) + ": " + hand)

    def point(self, hand):

        # point()function to calculate partial score
        sortedHand = sorted(hand, reverse=True)
        ranklist = []
        for card in sortedHand:
            ranklist.append(card.rank)
        c_sum = ranklist[0] * 13 ** 4 + ranklist[1] * 13 ** 3 + ranklist[2] * 13 ** 2 + ranklist[3] * 13 + ranklist[4]
        return c_sum

    def isRoyal(self, hand):

        # returns the total_point and prints out 'Royal Flush' if true, if false, pass down to isStraightFlush(hand)
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 10
        Cursuit = sortedHand[0].suit
        Currank = 14
        total_point = h * 13 ** 5 + self.point(sortedHand)
        for card in sortedHand:
            if card.suit != Cursuit or card.rank != Currank:
                flag = False
                break
            else:
                Currank -= 1
        if flag:
            print('Royal Flush')
            self.totalPoints.append(total_point)
        else:
            self.isStraightFlush(sortedHand)

    def isStraightFlush(self, hand):

        # returns the total_point and prints out 'Straight Flush' if true, if false, pass down to isFour(hand)
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 9
        Cursuit = sortedHand[0].suit
        Currank = sortedHand[0].rank
        total_point = h * 13 ** 5 + self.point(sortedHand)
        for card in sortedHand:
            if card.suit != Cursuit or card.rank != Currank:
                flag = False
                break
            else:
                Currank -= 1
        if flag:
            print('Straight Flush')
            self.totalPoints.append(total_point)
        else:
            self.isFour(sortedHand)

    def isFour(self, hand):

        # returns the total_point and prints out 'Four of a Kind' if true, if false, pass down to isFull()
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 8
        Currank = sortedHand[
            1].rank  # since it has 4 identical ranks,the 2nd one in the sorted listmust be the identical rank
        count = 0
        total_point = h * 13 ** 5 + self.point(sortedHand)
        for card in sortedHand:
            if card.rank == Currank:
                count += 1
        if not count < 4:
            flag = True
            print('Four of a Kind')
            self.totalPoints.append(total_point)

        else:
            self.isFull(sortedHand)

    def isFull(self, hand):

        # returns the total_point and prints out 'Full House' if true, if false, pass down to isFlush()
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 7
        total_point = h * 13 ** 5 + self.point(sortedHand)
        mylist = []  # create a list to store ranks
        for card in sortedHand:
            mylist.append(card.rank)
        rank1 = sortedHand[0].rank  # The 1st rank and the last rank should be different in a sorted list
        rank2 = sortedHand[-1].rank
        num_rank1 = mylist.count(rank1)
        num_rank2 = mylist.count(rank2)
        if (num_rank1 == 2 and num_rank2 == 3) or (num_rank1 == 3 and num_rank2 == 2):
            flag = True
            print('Full House')
            self.totalPoints.append(total_point)

        else:
            flag = False
            self.isFlush(sortedHand)

    def isFlush(self, hand):

        # returns the total_point and prints out 'Flush' if true, if false, pass down to isStraight()
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 6
        total_point = h * 13 ** 5 + self.point(sortedHand)
        Cursuit = sortedHand[0].suit
        for card in sortedHand:
            if not (card.suit == Cursuit):
                flag = False
                break
        if flag:
            print('Flush')
            self.totalPoints.append(total_point)

        else:
            self.isStraight(sortedHand)

    def isStraight(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 5
        total_point = h * 13 ** 5 + self.point(sortedHand)
        Currank = sortedHand[0].rank  # this should be the highest rank
        for card in sortedHand:
            if card.rank != Currank:
                flag = False
                break
            else:
                Currank -= 1
        if flag:
            print('Straight')
            self.totalPoints.append(total_point)

        else:
            self.isThree(sortedHand)

    def isThree(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 4
        total_point = h * 13 ** 5 + self.point(sortedHand)
        Currank = sortedHand[2].rank  # In a sorted rank, the middle one should have 3 counts if flag=True
        mylist = []
        for card in sortedHand:
            mylist.append(card.rank)
        if mylist.count(Currank) == 3:
            flag = True
            print("Three of a Kind")
            self.totalPoints.append(total_point)

        else:
            flag = False
            self.isTwo(sortedHand)

    def isTwo(self, hand):  # returns the total_point and prints out 'Two Pair' if true, if false, pass down to isOne()
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 3
        total_point = h * 13 ** 5 + self.point(sortedHand)
        rank1 = sortedHand[
            1].rank  # in a five cards sorted group, if isTwo(), the 2nd and 4th card should have another identical rank
        rank2 = sortedHand[3].rank
        mylist = []
        for card in sortedHand:
            mylist.append(card.rank)
        if mylist.count(rank1) == 2 and mylist.count(rank2) == 2:
            flag = True
            print("Two Pair")
            self.totalPoints.append(total_point)

        else:
            flag = False
            self.isOne(sortedHand)

    def isOne(self, hand):  # returns the total_point and prints out 'One Pair' if true, if false, pass down to isHigh()
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 2
        total_point = h * 13 ** 5 + self.point(sortedHand)
        mylist = []  # create an empty list to store ranks
        mycount = []  # create an empty list to store number of count of each rank
        for card in sortedHand:
            mylist.append(card.rank)
        for each in mylist:
            count = mylist.count(each)
            mycount.append(count)
        if mycount.count(2) == 2 and mycount.count(
                1) == 3:  # There should be only 2 identical numbers and the rest are all different
            flag = True
            print("One Pair")
            self.totalPoints.append(total_point)

        else:
            flag = False
            self.isHigh(sortedHand)

    def isHigh(self, hand):  # returns the total_point and prints out 'High Card'
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 1
        total_point = h * 13 ** 5 + self.point(sortedHand)
        mylist = []  # create a list to store ranks
        for card in sortedHand:
            mylist.append(card.rank)
        print("High Card")
        self.totalPoints.append(total_point)


def main():
    # Main game

    numHands = eval(input('Enter number of hands to play: '))
    # Ask user for number of hands to play

    while (numHands < 2 or numHands > 10):
        numHands = eval(input('Enter number of hands to play: '))
        # Check that number of hands is between 2 & 10

    game = Poker(numHands)

    # Play round of poker
    game.play()

    # Display results of round
    print('\n')
    for i in range(numHands):
        curHand = game.hands[i]
        print("Hand " + str(i + 1) + ": ", end="")
        game.isRoyal(curHand)

    maxpoint = max(game.totalPoints)
    maxindex = game.totalPoints.index(maxpoint)

    # Display winner of round
    print('\nHand %d wins' % (maxindex + 1))


main()
