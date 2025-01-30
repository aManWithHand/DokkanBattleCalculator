import customtkinter
from ..base import Base

class OutputFrame(customtkinter.CTkFrame):
    def __init__(self, master,text, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.label1 = customtkinter.CTkLabel(self,fg_color="#484c4d",text=text,width=width)
        self.label1.grid(column=0, row=0, padx=15, pady=(15,5))

        self.label2 = customtkinter.CTkLabel(self,width=width,text="Phase1: 254613")
        self.label2.grid(column=0, row=1, padx=15, pady=(0,5))
        self.label3 = customtkinter.CTkLabel(self,width=width,text="Phase2: 254613")
        self.label3.grid(column=0, row=2, padx=15, pady=(0,5))
        self.label4 = customtkinter.CTkLabel(self,width=width,text="    SA: 254613")
        self.label4.grid(column=0, row=3, padx=15, pady=(0,5))

    def show(self,base:Base):
        #get data from base and show in OutputFrame
        self.label2.configure(text=f"Phase1: {base.beforeAttack:7}")
        self.label3.configure(text=f"Phase2: 254613")
        self.label4.configure(text=f"    SA: 254613")
