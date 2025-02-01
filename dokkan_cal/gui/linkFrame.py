import customtkinter

class LinkFrame(customtkinter.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.label1 = customtkinter.CTkLabel(self,width=150, text="LINK BUFF")
        self.label1.grid(column=0, row=0, padx=15, pady=15)

        self.entry1 = customtkinter.CTkEntry(self)
        self.entry1.grid(column=0, row=1, pady=(0,15))
        self.entry1.insert(0,"0")

    def getBuff(self):
        try:
            return float(self.entry1.get())
        except:
            return 0
        
    
