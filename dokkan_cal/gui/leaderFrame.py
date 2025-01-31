import customtkinter

class LeaderFrame(customtkinter.CTkFrame):
    def __init__(self, master,values, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.label1 = customtkinter.CTkLabel(self,width=150,text="LeaderBuff")
        self.label1.grid_configure(column=0, row=0, padx=15, pady=15,columnspan=2)
        self.label2 = customtkinter.CTkLabel(self,text="ATK&DEF")
        self.label2.grid_configure(column=0, row=1, pady=(0,5), padx=10)
        self.combobox1 = customtkinter.CTkComboBox(self, values=values)
        self.combobox1.set("200")
        self.combobox1.grid_configure(column=1, row=1, padx=10)

        self.label3 = customtkinter.CTkLabel(self,width=150,text="Friend's LeaderBuff")
        self.label3.grid_configure(column=0, row=2, padx=15, pady=15,columnspan=2)
        self.label4 = customtkinter.CTkLabel(self,text="ATK&DEF")
        self.label4.grid_configure(column=0, row=3, pady=(0,5), padx=10)
        self.combobox2 = customtkinter.CTkComboBox(self, values=values)
        self.combobox2.set("200")
        self.combobox2.grid_configure(column=1,row=3, padx=10, pady=(0,20))


    def getBuff(self):
        return int(self.combobox1.get())+int(self.combobox2.get())
    

if __name__ == "__main__":
    window = customtkinter.CTk()
    lframe = LeaderFrame(master=window,values=["1","77", "170","200"])
    lframe.grid_configure(row=0,column=0)
    print(lframe.getBuff())
    window.mainloop()
    