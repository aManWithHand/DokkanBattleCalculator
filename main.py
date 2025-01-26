import customtkinter
import dokkan_cal as dk

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Dokkan Battle Calculator")
        self.geometry(f"{400}x{600}")


#button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
#button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

if __name__ == "__main__":
    app = App()
    app.mainloop()
