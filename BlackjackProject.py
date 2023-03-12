import random

# Define classes for PlayingCard, Dealer, Player
class PlayingCard:
    def __init__(self, suit, rank, value = 0):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.name = str(self.rank) + " of " + self.suit

class Dealer:
    card_hand = []
    card_hand_value = 0

    def initial_deal():
        for i in range(2):
            for player in player_list:
                player.card_hand.append(Dealer.deal_card())
                player.card_hand_value = calc_hand_value(player.card_hand)
                
            Dealer.card_hand.append(Dealer.deal_card())
            Dealer.card_hand_value = calc_hand_value(Dealer.card_hand)

    def deal_card():
        dealt_card = deck_of_cards.pop(random.randint(0, len(deck_of_cards) - 1))

        return dealt_card

    def reveal_card():
        return Dealer.card_hand[0]

class Player:
    player_number = 0
    player_play_choices = ["H", "S"]
    player_cont_choices = ["Y", "N"]
    
    def __init__(self):
        Player.player_number += 1
        self.name = "Player" + str(Player.player_number)
        self.card_hand = []
        self.card_hand_value = 0
        self.play_choice = ""
        self.cont_choice = "Y"
        self.chips = 10

    def player_play(self):
        while self.play_choice != "S" and self.card_hand_value <= 21:
            self.play_choice = input("{name}, what would you like to do? Hit (H) or Stand (S): ".format(name = self.name)).upper()

            while self.play_choice not in Player.player_play_choices:
                self.play_choice = input("Invalid option. Please choose either Hit (H) or Stand (S): ").upper()

            if self.play_choice == "H":
                self.card_hand.append(Dealer.deal_card())
                print(show_card_hand(self.name, self.card_hand))
                self.card_hand_value = calc_hand_value(self.card_hand)

        if self.card_hand_value > 21:
            print("Bust!")

    def player_cont(self):
        if self.chips == 0:
            self.cont_choice = "N"
        else:
            self.cont_choice = input("{name}, would you like to continue playing? Yes (Y) or No (N): ".format(name = self.name)).upper()

            while self.cont_choice not in Player.player_cont_choices:
                self.cont_choice = input("Invalid option. Please choose either Yes (Y) or No (N): ").upper()

        if self.cont_choice == "N":
            removed_players.append(player)
        
        
# Initialize a deck of 52 playing cards
def set_deck_of_cards():
    card_ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    card_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    for card_suit in card_suits: 
        for card_rank in card_ranks:
            deck_of_cards.append(PlayingCard(card_suit, card_rank))

    for card in deck_of_cards:
        if type(card.rank) == int:
            card.value = card.rank
        elif card.rank in ["Jack", "Queen", "King"]:
            card.value = 10
        elif card.rank == "Ace":
            card.value = [1, 11]

# Show card hand
def show_card_hand(name, cards):
    ret_str = "{name}: {card}".format(name = name, card = cards[0].name)
    
    if len(cards) == 1:
        return ret_str
    else:
        for i in range(1, len(cards)):
            ret_str += ", {card}".format(card = cards[i].name)

    return ret_str

# Calculate total value of player or dealer card hand
def calc_hand_value(card_hand):
    total = 0
    ace_count = 0

    for card in card_hand:
        if card.rank != "Ace":
            total += card.value
        else:
            ace_count += 1
            
    for i in range(ace_count):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1

    return total

# Decide game winner(s)
def round_winner():
    # Compare card hand values
    def comp_hand_values():
        best_hand_value = Dealer.card_hand_value

        for player in player_list:
            if player.card_hand_value <= 21 and player.card_hand_value >= best_hand_value:
                best_hand_value = player.card_hand_value

        return best_hand_value

    winner_list = []
    best_hand_value = comp_hand_values()

    if Dealer.card_hand_value == best_hand_value:
        winner_list.append(Dealer)
    for player in player_list:
        if player.card_hand_value == best_hand_value:
            winner_list.append(player)

    return winner_list

# Decide who gets the pot and end round
def round_end():
    winner_list = round_winner()
  
    if Dealer in winner_list:
        print("Dealer has won this round and takes the pot.\n")
    else:
        if len(winner_list) == 1:
            print("{name} has won this round and takes the pot.\n".format(name = winner_list[0].name))
            winner_list[0].chips += pot
        elif len(winner_list) == 2:
            print("{name1} and {name2} have won this round and will each take half the pot.\n".format(name1 = winner_list[0].name, name2 = winner_list[1].name))
            winner_list[0].chips += int(pot / 2)
            winner_list[1].chips += int(pot / 2)
        elif len(winner_list) == 3:
            print("{name1}, {name2}, and {name3} have won this round and will each take a third of the pot.\n".format(name1 = winner_list[0].name, name2 = winner_list[1].name, name3 = winner_list[2].name))
            winner_list[0].chips += int(pot / 3)
            winner_list[1].chips += int(pot / 3)
            winner_list[2].chips += int(pot / 3)

    for player in player_list:
        print("{name} has {chip_num} chips.".format(name = player.name, chip_num = player.chips))

    print("")    

    return 0    

# Reset for new round
def round_reset():
    Dealer.card_hand = []
    Dealer.card_hand_value = 0

    for player in player_list:
        player.card_hand = []
        player.card_hand_value = 0
        player.play_choice = ""

    return True

# Logic for gameplay
deck_of_cards = []
player_list = []
removed_players = []
winner_of_round = []
game_pot = 0
game_in_progress = True

print("""Welcome to the Blackjack table!\n
Description:
Each player starts with 10 chips.
To continue playing, a bet of 1 chip is required, which is then doubled for the pot.
The pot goes to the player with the best hand, which does not exceed 21.
If a tie occurs between players, the pot will be split equally.
If the Dealer ties with any players, the Dealer wins the pot.\n""")

number_of_players = input("How many players? (1 - 3): ")

while number_of_players not in ["1", "2", "3"]:
    number_of_players = input("Invalid number of players. Please choose between 1 and 3: ")

number_of_players = int(number_of_players)

for i in range(number_of_players):
    player_list.append(Player())
        
while number_of_players != 0:
    set_deck_of_cards()
    pot = number_of_players * 2

    while game_in_progress:
        Dealer.initial_deal()

        print("\nRound Start!")

        for player in player_list:
            player.chips -= 1
            print("{name} has added 1 chip to the pot.".format(name = player.name))

        print("\nThe current pot is {pot} chips.\n".format(pot = pot))

        print("Initial Deal:")
        print(show_card_hand("Dealer", [Dealer.card_hand[1]]))
        for player in player_list:
            print(show_card_hand(player.name, player.card_hand))
        print("")            
        
        for player in player_list:
            player.player_play()
            print("")

        print(show_card_hand("Dealer", Dealer.card_hand))
        for player in player_list:
            print(show_card_hand(player.name, player.card_hand))
        print("")
                    
        pot = round_end()
        
        game_in_progress = False

    for player in player_list:
        player.player_cont()
        print("")

    for removed_player in removed_players:
        if removed_player in player_list:
            print("{name} has left the table with {chip_num} chip(s).".format(name = removed_player.name, chip_num = removed_player.chips))
            player_list.remove(removed_player)
            number_of_players -= 1

    game_in_progress = round_reset()
