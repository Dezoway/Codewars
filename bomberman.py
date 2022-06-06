import random as r
class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self, N, M):
        self.pole = [[Cell(0,0) for x in range(N)] for i in range(N)]
        self.mines = M

    def class_field(self):
        self.coords_mines = []
        while(self.mines != 0):
            k,v = r.randrange(0,len(self.pole)), r.randrange(0,len(self.pole))
            if self.pole[k][v].mine == 0:
                self.pole[k][v].mine = 1
                self.coords_mines+=[[k,v],[k+1,v],[k+1,v+1],[k,v+1],[k-1,v+1],[k-1,v],[k-1,v-1],[k,v-1],[k+1,v-1]]
                self.mines -= 1

    def init(self):
        self.class_field()
        for x in range(len(self.pole)):
            for i in range(len(self.pole)):
                if self.coords_mines.count([x,i]) == 0 and self.pole[x][i].mine==0:self.pole[x][i].around_mines = 0
                else:
                    self.pole[x][i].around_mines = self.coords_mines.count([x,i])




    def show(self):
        #[print(['#' if x.fl_open==False else 'k'for x in t]) for t in self.pole]
        [print(['M' if x.mine==1 else'#' for x in t]) for t in self.pole]
        print('\n')
        [print([x.around_mines for x in t]) for t in self.pole]



pole_game= GamePole(10,12)
pole_game.init()
pole_game.show()


