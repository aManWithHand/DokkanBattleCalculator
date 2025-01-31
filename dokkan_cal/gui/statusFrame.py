import customtkinter

#define StatusFrame to input baseDef baseAtk
    
class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.label1 = customtkinter.CTkLabel(self,width=150, text="Base status")
        self.label1.grid_configure(column=0, row=0, padx=15, pady=15, columnspan=2)

        self.label2 = customtkinter.CTkLabel(self,text="DEF")
        self.label2.grid_configure(column=0, row=1, pady=(0,5), padx=10)
        self.entry1 = customtkinter.CTkEntry(self)
        self.entry1.grid(column=1, row=1, pady=(0,5))
        self.entry1.insert(0,"0")
        
        #add ATK and HP
        # self.entry2 = customtkinter.CTkEntry(self)
        # self.entry2.grid(column=0, row=2, pady=(0,5))
        # self.entry3 = customtkinter.CTkEntry(self)
        # self.entry3.grid(column=0, row=3, pady=(0,15))

    def getDef(self):
        return int(self.entry1.get())

if __name__ == "__main__":
    window = customtkinter.CTk()
    sframe = StatusFrame(master=window)
    sframe.grid_configure(row=0,column=0)
    print(sframe.getDef())
    window.mainloop()