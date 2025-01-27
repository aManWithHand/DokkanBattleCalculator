import customtkinter
import dokkan_cal as dk
import dokkan_cal.gui as gui

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

class App(customtkinter.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Dokkan Battle Calculator")
        self.geometry(f"{400}x{600}")
        self.grid_columnconfigure((0,2),weight=1)

        self.test1 = gui.InputFrame(self,"PHASE1 (before attack)")
        self.test1.grid(column=1,row=0)
        self.test2 = gui.InputFrame(self,"PHASE2 (attacking)")
        self.test2.grid(column=1,row=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
