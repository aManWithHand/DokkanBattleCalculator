class Core():
    @staticmethod
    def buff(start_def,buff_list):
        total_def=start_def
        for percent in buff_list:
            total_def += int(percent*total_def/100)
        return total_def