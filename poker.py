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
        # Create a list to store totalPoint

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
        # Define play

        for i in range(len(self.hands)):
            sortedHand = sorted(self.hands[i], reverse=True)
            # Sort each hand high to low

            hand = ""

            for card in sortedHand:
                hand = hand + str(card) + " "
            print("Player " + str(i + 1) + ": " + hand)
            # Display each player's hand

    def point(self, hand):
        # Define points to calculate score

        sortedHand = sorted(hand, reverse=True)
        pointList = []

        for card in sortedHand:
            pointList.append(card.rank)
        cardSum = pointList[0] * 13 ** 4 + pointList[1] * 13 ** 3 + pointList[2] * 13 ** 2 + pointList[3] * 13 \
                  + pointList[4]
        return cardSum

    def isRoyal(self, hand):
        # Checks for Royal Flush

        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 10
        curSuit = sortedHand[0].suit
        curRank = 14
        totalPoint = h * 13 ** 5 + self.point(sortedHand)
        for card in sortedHand:
            if card.suit != curSuit or card.rank != curRank:
                flag = False
                break
            else:
                curRank -= 1
        if flag:
            print('Royal Flush')
            self.totalPoints.append(totalPoint)
        else:
            self.isStraightFlush(sortedHand)

    def isStraightFlush(self, hand):
        # Checks for Straight Flush

        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 9
        curSuit = sortedHand[0].suit
        curRank = sortedHand[0].rank
        totalPoint = h * 13 ** 5 + self.point(sortedHand)
        for card in sortedHand:
            if card.suit != curSuit or card.rank != curRank:
                flag = False
                break
            else:
                curRank -= 1
        if flag:
            print('Straight Flush')
            self.totalPoints.append(totalPoint)
        else:
            self.isFour(sortedHand)

    def isFour(self, hand):
        # Checks for Four of a Kind

        sortedHand = sorted(hand, reverse=True)
        h = 8
        curRank = sortedHand[
            1].rank
                # since it has 4 identical ranks,the 2nd one in the sorted list must be the identical rank
        count = 0
        totalPoint = h * 13 ** 5 + self.point(sortedHand)
        for card in sortedHand:
            if card.rank == curRank:
                count += 1
        if not count < 4:
            print('Four of a Kind')
            self.totalPoints.append(totalPoint)

        else:
            self.isFull(sortedHand)

    def isFull(self, hand):
        # Checks for a Full House

        sortedHand = sorted(hand, reverse=True)
        h = 7
        totalPoint = h * 13 ** 5 + self.point(sortedHand)
        rankList = []
        # create a list to store ranks

        for card in sortedHand:
            rankList.append(card.rank)
        rank1 = sortedHand[0].rank
        # The 1st rank and the last rank should be different in a sorted list
        rank2 = sortedHand[-1].rank
        numRank1 = rankList.count(rank1)
        numRank2 = rankList.count(rank2)
        if (numRank1 == 2 and numRank2 == 3) or (numRank1 == 3 and numRank2 == 2):
            print('Full House')
            self.totalPoints.append(totalPoint)

        else:
            self.isFlush(sortedHand)

    def isFlush(self, hand):
        # Checks for a Flush

        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 6
        totalPoint = h * 13 ** 5 + self.point(sortedHand)
        curSuit = sortedHand[0].suit
        for card in sortedHand:
            if not (card.suit == curSuit):
                flag = False
                break
        if flag:
            print('Flush')
            self.totalPoints.append(totalPoint)

        else:
            self.isStraight(sortedHand)

    def isStraight(self, hand):
        # Checks for a Straight

        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 5
        totalPoint = h * 13 ** 5 + self.point(sortedHand)
        curRank = sortedHand[0].rank
        # this should be the highest rank
        for card in sortedHand:
            if card.rank != curRank:
                flag = False
                break
            else:
                curRank -= 1
        if flag:
            print('Straight')
            self.totalPoints.append(totalPoint)

        else:
            self.isThree(sortedHand)

    def isThree(self, hand):
        # Checks for Three of a Kind

        sortedHand = sorted(hand, reverse=True)
        h = 4
        totalPoint = h * 13 ** 5 + self.point(sortedHand)
        curRank = sortedHand[2].rank
        # In a sorted rank, the middle one should have 3 counts if flag=True
        rankList = []
        for card in sortedHand:
            rankList.append(card.rank)
        if rankList.count(curRank) == 3:
            print("Three of a Kind")
            self.totalPoints.append(totalPoint)

        else:
            self.isTwo(sortedHand)

    def isTwo(self, hand):
        # Checks for Two Pair

        sortedHand = sorted(hand, reverse=True)
        h = 3
        totalPoint = h * 13 ** 5 + self.point(sortedHand)
        rank1 = sortedHand[
            1].rank
        # in a five cards sorted group, if isTwo(), the 2nd and 4th card should have another identical rank
        rank2 = sortedHand[3].rank
        rankList = []
        for card in sortedHand:
            rankList.append(card.rank)
        if rankList.count(rank1) == 2 and rankList.count(rank2) == 2:
            print("Two Pair")
            self.totalPoints.append(totalPoint)

        else:
            self.isOne(sortedHand)

    def isOne(self, hand):
        # Checks for One Pair

        sortedHand = sorted(hand, reverse=True)
        h = 2
        totalPoint = h * 13 ** 5 + self.point(sortedHand)
        rankList = []
        # create an empty list to store ranks
        rankCount = []
        # create an empty list to store number of count of each rank
        for card in sortedHand:
            rankList.append(card.rank)
        for each in rankList:
            count = rankList.count(each)
            rankCount.append(count)
        if rankCount.count(2) == 2 and rankCount.count(
                1) == 3:
            # There should be only 2 identical numbers and the rest are all different
            print("One Pair")
            self.totalPoints.append(totalPoint)

        else:
            self.isHigh(sortedHand)

    def isHigh(self, hand):
        # Check for High Card

        sortedHand = sorted(hand, reverse=True)
        h = 1
        totalPoint = h * 13 ** 5 + self.point(sortedHand)
        rankList = []
        # create a list to store ranks
        for card in sortedHand:
            rankList.append(card.rank)
        print("High Card")
        self.totalPoints.append(totalPoint)


def main():
    # Main game

    chips = 0
    playerList =[]
    numHands = 0
    while True:
        try:
            numHands = int((input('Enter the number of players (2-10): ')))
        except ValueError:
            print('\nError! Value must be an integer between 2 & 10. Try again.\n')
        else:
            if numHands < 2 or numHands > 10:
                print("\nNumber of players must be between 2 & 10.\n")
            else:
                break

    # Ask user for number of hands to play

    game = Poker(numHands)

    # Play round of poker
    game.play()

    # Display results of round
    print('\n')
    for i in range(numHands):
        curHand = game.hands[i]
        print("Player " + str(i + 1) + ": ", end="")
        game.isRoyal(curHand)

    maxpoint = max(game.totalPoints)
    maxindex = game.totalPoints.index(maxpoint)

    # Display winner of round
    print('\nPlayer %d wins' % (maxindex + 1))


main()
