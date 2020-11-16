class Player ():
    name = "" # the name of this player, string
    age = -1  # the age of this player, int
    run = -1  # the running skill of this player, int
    swim = -1 # the swimming skill of this player, int
    climb = -1 # the climbing skill of this player, int
    index = -1 # the index of this player on adv_map, int
    pos = None # the position of this player, (x,y)
    day = -1   # the number of elapsed days of this player, int
    
    def __str__(self):                
        retval = "Name: %s\tage: %d\tpos: (%d,%d) after %d days"%(self.name, self.age, self.pos[0], self.pos[1], self.day)       
        if self.index == len(adv_map):
            retval = "Name: %s\tage: %d\tpos: Goal after %d days"%(self.name, self.age, self.day)       
        return retval     
    
#homework#4 area start----------------------------------------------------------      
    def __init__(self,name,age,run,swim,climb):
    # something do here
    # initialize all the attributes of this player
        self.pos = (0,0)
        self.index = 0
        self.day = 0        
        self.name = name
        self.age = age
        self.run = run
        self.swim = swim
        self.climb = climb
    
    def __cmp__(self,other):
    # something do here    
    # return 1 if the number of elapsed days of this player is larger than that of other player
    # return -1 if the number of elapsed days of this player is smaller than that of other player
    # return 0 otherwise
        if self.day>other.day:
            return 1
        elif self.day<other.day:
            return -1
        else :
            return 0
    
    def move(self):                
    # something do here
    # move player according to his skill and terrain
        if self.pos != adv_map[len(adv_map)-1][0]:
            self.day= self.day +1        
            if adv_map[self.index][1] == 1:
                for i in range(self.run):
                    self.index = self.index + 1
                    self.pos = adv_map[self.index][0]
                    if self.pos == adv_map[len(adv_map)-1][0]:
                        break
                    if adv_map[self.index][1] != 1:
                        break
            if adv_map[self.index][1] == 2:
                for i in range(self.swim):
                    self.index = self.index + 1
                    self.pos = adv_map[self.index][0]
                    if self.pos == adv_map[len(adv_map)-1][0]:
                        break
                    if adv_map[self.index][1] != 2:
                        break                    
            if adv_map[self.index][1] == 3:
                for i in range(self.run):
                    self.index = self.index + 1
                    self.pos = adv_map[self.index][0]
                    if self.pos == adv_map[len(adv_map)-1][0]:
                        break
                    if adv_map[self.index][1] != 3:
                        break                        
        pass
    
    def select_equip(self):
    # something do here
    # output: 1 if player selects running equipment
    #         2 if player selects swimming equipment
    #         3 if player selects climbing equipment
    # selects the most useful equipment for this player
    # each equipment increases the skill of this player by 1
        num_plain = 0
        num_water = 0
        num_mount = 0
        for i in range(len(adv_map)-self.index):
            if adv_map[self.index+i][1] == 1:
                num_plain = num_plain + 1
            elif adv_map[self.index+i][1] == 2:
                num_water = num_water + 1
            else :
                num_mount = num_mount + 1
        select_run = num_plain/(self.run+1) + num_water/self.swim + num_mount/self.climb
        select_swim = num_plain/self.run + num_water/(self.swim+1) + num_mount/self.climb
        select_climb = num_plain/self.run + num_water/self.swim + num_mount/(self.climb+1)
        if (select_run<=select_swim and select_run<=climb):
            self.run = self.run + 1
        elif select_swim<select_climb:
            self.swim = self.swim + 1
        else :
            self.climb = self.climb + 1
        return 1
    
def make_map(m_filename):
    
    # something do here
    
    # input: string m_filename
    
    # output: list of tuples

    # each tuple consists of position (x,y) and terrain variable z: ((x,y),z)
    
    # z = 1 : plain z = 2 : water z = 3 : mountain
    
    t = open(m_filename,"r")
    
        
    
    initial_map = []
    
    fin_map = []
    
    for line in t:
    
        each_num = []
    
        for i in range(len(line.strip())):
    
            each_num.append(int(line.strip()[i]))
    
        initial_map.append(each_num)
    
            
    
    fin_map.append(((0,0),int(initial_map[0][0])))
    
    x = 0
    
    y = 0
    
    maps = 0
    
    for i in range(len(initial_map)):
    
        for j in range(len(initial_map[i])):
    
            if initial_map[i][j]!=0:
    
                maps = maps+1
    
                    
    
    while len(fin_map)!=maps:
    
        if x-1>=0:
    
            if initial_map[y][x-1]!=0:
    
                if ((x-1,y),initial_map[y][x-1]) not in fin_map:
    
                    fin_map.append(((x-1,y),initial_map[y][x-1]))
    
                    x = x-1
    
        if x+1<len(initial_map[0]):
    
            if initial_map[y][x+1]!=0:
    
                if ((x+1,y),initial_map[y][x+1]) not in fin_map:
    
                    fin_map.append(((x+1,y),initial_map[y][x+1]))
    
                    x = x+1
    
        if y-1>=0:
    
            if initial_map[y-1][x]!=0:
    
                if ((x,y-1),initial_map[y-1][x]) not in fin_map:
    
                    fin_map.append(((x,y-1),initial_map[y-1][x]))
    
                    y = y-1
    
        if y+1<len(initial_map):
    
            if initial_map[y+1][x]!=0:
    
                if ((x,y+1),initial_map[y+1][x]) not in fin_map:
    
                    fin_map.append(((x,y+1),initial_map[y+1][x]))
    
                    y = y+1
    
        
    
    return fin_map


def make_advs(a_filename):
    # something do here
    # input: string a_filename
    # output: list of Players
    t = open(a_filename,"r")
    players = []
    man = []
    
    for line in t:
        man.append(line.strip().split(','))
        
    for i in range(len(man)):
        players.append(Player(man[i][0],int(man[i][1]),int(man[i][2]),int(man[i][3]),int(man[i][4])))    
    
    return players
    
# homework 4 area end ----------------------------------------------------------
m_filename = "map.txt"
a_filename = "player.txt"
# read the map information and make the path
adv_map = make_map(m_filename)
# read the players information and make the list of Players
advs = make_advs(a_filename)
end_flag = True
s_equip = ["","running", "swimming", "climbing"]

while end_flag:  
    num_day = input("Enter the number of days: ")
    # Advance the adventure by input days
    for i in range(num_day):        
        for j in range(len(advs)):   
            # players who doesn't arrive at the goal select equipment every 5 days
            if (advs[j].day %5 == 0 and advs[j].day != 0):
                if advs[j].index != len(adv_map):
                    new_equip = advs[j].select_equip()
                    #print the player's name and selected equipment
                    print "%s selects %s equipment!"%(advs[j].name,s_equip[new_equip])
            # players who doesn't arrive at the goal move by using their move function
            if advs[j].index != len(adv_map):
                advs[j].move()            
            
    end_flag = False
    # if all players arrive at the goal, halt the while loop
    for i in range(len(advs)):        
        print advs[i]
        if (advs[i].index < len(adv_map)):
            end_flag = True
            
advs.sort()
print "After the adventure..."
for i in range(len(advs)):
    print advs[i]