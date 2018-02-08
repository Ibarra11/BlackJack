import random
from IPython.display import clear_output

class BlackJack(object):
    def __init__(self):
        self.cards2 = [0,
                       ['AH', 'AD', 'AC', 'AS'], ['2S','2H','2C','2D'],
                       ['3S','3H','3C','3D'], ['4S','4H','4C','4D'], ['5S','5H','5C','5D'],
                       ['6S','6H','6C','6D'], ['7S','7H','7C','7D'], ['8S','8H','8C','8D'],
                       ['9S','9H','9C','9D'], ['JS','JH','JC','JD','QS','QH','QC','QD','KS','KH','KC','KD']
                      ]
        self.playersMoney = 0
        self.playerHand = []
        self.dealersHand = []
        self.bettingAmount = 0
    def setPlayerBettingAmount(self):
        self.bettingAmount = int(input('Player 1 set your betting amount: '))
    def standOrHit(self):
        return input('Enter stand if you wannt to stand or Hit if you want to continue ').upper().startswith('H')
    def setPlayerMoney(self):
        self.playersMoney = int(input('Player 1 enter how much money you have: '))
    def retrieveCard(self):
        while True:
            for el in self.cards2[random.randint(1,len(self.cards2) - 1)]:
                if self.playerHand.count(el) == 0 and self.dealersHand.count(el) == 0:
                    return el
    def addCardToPlayersHand(self):
        card = self.retrieveCard()
        self.playerHand.append(card)
    def displayCards(self):
        print("Player 1's Current Bet: ", self.bettingAmount)
        print('Dealers Current Hand: ', self.dealersHand)
        print('Your current Hand: ', self.playerHand)
    def addCardToDealersHand(self):
        card = self.dealersHand.append(self.retrieveCard())

    def getPlayersCardAmount(self):
        playersTotal = 0
        for card in self.playerHand:
            if card[0] == 'A':
                if (playersTotal + 11) > 21:
                    playersTotal += 1
                else:
                    playersTotal += 11
            elif card[0] == 'J' or card[0] == 'K'or card[0] == 'K':
                playersTotal += 10
            else:
                playersTotal += int(card[0])
        return playersTotal

    def getDealersCardAmount(self):
        dealersTotal = 0
        for card in self.dealersHand:
            if card[0] == 'A':
                if (dealersTotal + 11) > 21:
                    dealersTotal += 1
                else:
                    dealersTotal += 11
            elif card[0] == 'J' or card[0] == 'K'or card[0] == 'Q':
                dealersTotal += 10
            else:
                dealersTotal += int(card[0])
        return dealersTotal

    def dealInitialHand(self):
        self.addCardToPlayersHand()
        self.addCardToPlayersHand()
        self.addCardToDealersHand()
        self.addCardToDealersHand()
    def gameOver(self):
        if self.getPlayersCardAmount() == 21 or self.getPlayersCardAmount() > 21:
            return True
        elif self.getDealersCardAmount() == 21 or self.getDealersCardAmount() > 21:
            return True
        else:
            return False
    def checkHands(self):
        if self.getPlayersCardAmount() == 21:
            print('Congratulations, you have won with a perfect 21')
            self.playersMoney += self.bettingAmount
        elif self.getDealersCardAmount() == 21:
            print('Better luck next time Dealer has just won')
            self.playersMoney -= self.bettingAmount
        elif self.getPlayersCardAmount() < 21 and self.getDealersCardAmount() > 21:
            print('Congratulations, you have just won')
            self.playersMoney += self.bettingAmount
        elif self.getDealersCardAmount() < 21 and self.getPlayersCardAmount() > 21:
            print('Better luck next time Dealer has just won')
            self.playersMoney -= self.bettingAmount
        elif self.getDealersCardAmount() > 21 and self.getPlayersCardAmount() > 21:
            print('This game is a Bust')
    def promptUserToContinue(self):
        continueGame = False
        if self.playersMoney > 0:
            continueGame = input('You currently have  {}.  If you would like to keep playing enter y/n'.format(self.playersMoney)).startswith('y')
            return continueGame
        else:
            print('Thank you for playing!')


    def resetHands(self):
        self.playerHand = []
        self.dealersHand = []

class Game(BlackJack):
    def __init__(self):
        BlackJack.__init__(self)
        self.setPlayerMoney()
        self.startGame()
    def startGame(self):
        self.setPlayerBettingAmount()
        self.dealInitialHand()
        self.displayCards()
        while self.gameOver() != True and self.standOrHit() != False :
            clear_output()
            self.addCardToPlayersHand()
            self.addCardToDealersHand()
            self.displayCards()
        self.checkHands()
        if self.promptUserToContinue() == True:
            clear_output()
            self.resetHands()
            self.startGame()
newGame = Game()
