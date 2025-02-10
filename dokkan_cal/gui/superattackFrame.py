import customtkinter

class SuperAttackFrame(customtkinter.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.label1 = customtkinter.CTkLabel(self, text="SUPERATTACK BUFF", width=width)
        self.label1.grid_configure(column=0, row=0,padx=15, pady=(15,5), columnspan=2)
        self.label2 = customtkinter.CTkLabel(self, text="Number of SA")
        self.label2.grid(column=0, row=1)

        self.segButton1 = customtkinter.CTkSegmentedButton(self, values=["1","2","3","4","5"], height=40)
        self.segButton1.grid_configure(column=1, row=1)
        self.segButton1.set("1")

        self.label3 = customtkinter.CTkLabel(self, text="Value")
        self.label3.grid(column=0, row=2)
        self.entry1 = customtkinter.CTkEntry(self)
        self.entry1.grid(column=1, row=2)
        self.entry1.insert(0,"0")
    
    def getBuff(self) -> int:
        buff = int(self.segButton1.get()) * int(self.entry1.get())
        return buff
