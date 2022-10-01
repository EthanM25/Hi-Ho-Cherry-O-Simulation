import random


# spin function

def spin_gen():
    spinner = [1, 2, 3, 4, -2, -2, 10]
    result = random.choice(spinner)
    return result


# Player Class

class Player():
    def __init__(self):
        self.tree = 10
        self.basket = 0
        self.spins = 0
    def play(self):
        spin = spin_gen()
        self.spins += 1
        if spin != -2 and spin != 10:
            self.tree -= spin
            self.basket += spin
            #print(f"removed {spin} from the tree")
        if spin == 10:
            self.tree = 10
            self.basket = 0
            #print("emptied basket")
        if spin == -2:
            if self.basket > 1:
                self.basket -= 2
                self.tree += 2
                #print("removed two")
            if self.basket == 1:
                self.basket -= 1
                self.tree += 1
                #print("removed one")
        #print(f"status: tree: {self.tree} basket: {self.basket}")
    def check_win(self):
        if self.tree <= 0:
            return True
        else:
            return False

            
            
# game function

def play_game(playernum, times):
    spinlist = []
    for _ in range(times):
        playerlist = []
        for num in range(playernum):
            name = "P" + str(num + 1)
            name = Player()
            playerlist.append(name)
        on = False
        while on == False:
            for players in playerlist:
                players.play()
                result = players.check_win()
                if result == True:
                    total_spins = 0
                    for players in playerlist:
                        total_spins += players.spins
                    spinlist.append(total_spins)
                    on = True
    return f"\nGame stats for {playernum} player(s) with {times} trial(s)\nMinimum game length: {min(spinlist)}\nMaximum game length: {max(spinlist)}\nAverage game length: {sum(spinlist)/ len(spinlist)}"



    
# running with different test cases (can be configured)
print(play_game(1, 10000))
print(play_game(2, 10000))
print(play_game(4, 10000))






