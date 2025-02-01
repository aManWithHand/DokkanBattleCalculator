import customtkinter
import dokkan_cal.gui as gui
import dokkan_cal as dkc

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

class App(customtkinter.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Dokkan Battle Calculator")
        self.geometry(f"{600}x{700}")
        self.grid_columnconfigure((0,1,3),weight=1)

#------------------DEF GUI------------------------------------------------#
        self.defInput1 = gui.PhaseFrame(self,"PHASE1 (before attack)")
        self.defInput1.grid_configure(column=1, row=0, pady=15, padx=15)
        self.defInput2 = gui.PhaseFrame(self,"PHASE2 (attacking)")
        self.defInput2.grid_configure(column=1, row=1, pady=(0,15))
        self.defInput3 = gui.LinkFrame(self)
        self.defInput3.grid_configure(column=1, row=2, pady=(0,15))

        self.defInput4 = gui.LeaderFrame(self,values=["1","77", "170","200"])
        self.defInput4.grid_configure(column=2, row=1, pady=(0,0))
        self.defInput5 = gui.StatusFrame(self)
        self.defInput5.grid_configure(column=2, row=0, pady=(0,0))
        
        #add input for SA might use CTkSegmentedButton
        self.defOutput1 = gui.OutputFrame(self,"DEF")
        self.defOutput1.grid(column=1,row=4,pady=(15,15))
        self.defButton1 = customtkinter.CTkButton(self,text="calculate",command=self.calDEF)
        self.defButton1.grid(column=1,row=3)

#------------------LOGIC--------------------------------------------------#
        self.defList = [dkc.Defence(stat=self.defInput5, leader=self.defInput4, phase1=self.defInput1, phase2=self.defInput2, link=self.defInput3, out=self.defOutput1)]
    
    def calDEF(self):
        self.defList[0].cal()
        self.defList[0].show()
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
