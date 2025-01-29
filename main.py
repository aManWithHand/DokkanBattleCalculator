import customtkinter
import dokkan_cal.gui as gui

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

class App(customtkinter.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Dokkan Battle Calculator")
        self.geometry(f"{400}x{600}")
        self.grid_columnconfigure((0,1,2),weight=1)
#------------------DEF GUI------------------------------------------------#
        self.defInput1 = gui.PhaseFrame(self,"PHASE1 (before attack)")
        self.defInput1.grid(column=1,row=0,pady=15)
        self.defInput2 = gui.PhaseFrame(self,"PHASE2 (attacking)")
        self.defInput2.grid(column=1,row=1,pady=(0,15))
        #add input for SA might use CTkSegmentedButton
        self.defOutput1 = gui.OutputFrame(self,"DEF")
        self.defOutput1.grid(column=1,row=3,pady=(15,15))
        self.defButton1 = customtkinter.CTkButton(self,text="calculate",command=self._calDEF)
        self.defButton1.grid(column=1,row=2)
    
    def _calDEF(self):
        #self.defOutput1.show()
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
