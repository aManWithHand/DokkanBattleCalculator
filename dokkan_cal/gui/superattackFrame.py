import customtkinter

class SuperAttackFrame(customtkinter.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.segButton1 = customtkinter.CTkSegmentedButton(self, values=["15","20","50"])
        self.segButton1.set("20")
    
    def getBuff(self) -> int:
        return int(self.segButton1.get())
