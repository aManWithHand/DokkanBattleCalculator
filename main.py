import customtkinter
import dokkan_cal.gui as gui
import dokkan_cal as dkc

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

class App(customtkinter.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Dokkan Battle Calculator")
        

#------------------DEF GUI------------------------------------------------#
#------------------right hand side----------------------------------------#
        self.status_frame = gui.StatusFrame(self)
        self.status_frame.grid_configure(column= 2,
                                         row= 0,
                                         pady= (0,0))
        self.leader_frame1 = gui.LeaderFrame(self,
                                             values= ["1","77", "170","200"])
        self.leader_frame1.grid_configure(column=2,
                                          row=1,
                                          pady=(0,0),
                                          padx=(0,15))
        self.phase_frame1 = gui.PhaseFrame(self,
                                           text= "PHASE1 (before attack)")
        self.phase_frame1.grid_configure(column=2,
                                         row=2,
                                         pady=15,
                                         padx=15)

#------------------left hand side----------------------------------------#
        self.link_frame = gui.LinkFrame(self)
        self.link_frame.grid_configure(column=1,
                                       row=0,
                                       pady=(15,15))
        self.phase_frame2 = gui.PhaseFrame(self,
                                           text="PHASE2 (attacking)")
        self.phase_frame2.grid_configure(column=1,
                                         row=1,
                                         pady=(0,15))   
        self.super_attack_frame = gui.SuperAttackFrame(self)
        self.super_attack_frame.grid_configure(column=1,
                                               row=2,
                                               pady=(0,0),
                                               padx=(15,0))

#--------------------------middle----------------------------------------#  
        self.output_frame = gui.OutputFrame(self,
                                            text="DEF")
        self.output_frame.grid_configure(column=1,
                                         row=4,
                                         pady=15,
                                         columnspan=2)
        self.cal_button = customtkinter.CTkButton(self,
                                                  text="calculate",
                                                  command=self.calDEF)
        self.cal_button.grid_configure(column=1,
                                       row=3,
                                       columnspan=2)

#------------------LOGIC--------------------------------------------------#
        self.data_list = [dkc.Defence(stat=self.status_frame,
                                       leader=self.leader_frame1,
                                       phase1=self.phase_frame1,
                                       phase2=self.phase_frame2,
                                       link=self.link_frame,
                                       sa=self.super_attack_frame,
                                       out=self.output_frame)]
    
    def calDEF(self):
        self.data_list[0].cal()
        self.data_list[0].show()
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
