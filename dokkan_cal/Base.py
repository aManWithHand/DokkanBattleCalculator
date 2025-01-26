class Base():
    def __init__(self):
        self.buffPhase1 = []
        self.buffPhase2 = []
        self.beforeAttack = 0
        self.attacking=0
        
    def buff(start_def,buff_list):
        total_def=start_def
        for percent in buff_list:
            total_def += int(percent*total_def/100)
        return total_def