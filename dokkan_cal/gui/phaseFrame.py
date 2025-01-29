import customtkinter

class PhaseFrame(customtkinter.CTkFrame):
    def __init__(self, master, text, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        
        #self.button1 = customtkinter.CTkButton(self,width=150, state="disable", text=text, fg_color="#213c52",command=self.testButton)
        #self.button1.grid(column=0, row=0, padx=15, pady=15)
        self.label1 = customtkinter.CTkLabel(self,width=150, text=text)
        self.label1.grid(column=0, row=0, padx=15, pady=15)

        self.entry1 = customtkinter.CTkEntry(self)
        self.entry1.grid(column=0, row=1, pady=(0,5))
        self.entry2 = customtkinter.CTkEntry(self)
        self.entry2.grid(column=0, row=2, pady=(0,5))
        self.entry3 = customtkinter.CTkEntry(self)
        self.entry3.grid(column=0, row=3, pady=(0,15))

    def getBuff(self):
        return int(self.entry1.get())+int(self.entry2.get())+int(self.entry3.get())
    
    def testButton(self):
        print(self.getBuff())