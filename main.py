import tkinter as tk
from tkinter import*
from tkinter import messagebox as mes
from PIL import ImageTk, Image
import time
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.resizable(width=False,height=False)
   
        self.title("Test version 0.0.1")
        self.iconbitmap('python.ico')
        self.clock_label = tk.Label(self, text="", font=("Arial", 20))
        self.clock_label.place(x=900, y=10, width=200, height=40)

        # Start the clock
        self.update_clock()
        self.muqova()
        self.kirit()
        self.tugma()
        self.lis()
    def update_clock(self):
        # Get the current time
        current_time = time.strftime("%H:%M:%S")

        # Update the clock label
        self.clock_label.configure(text=current_time)

        # Schedule the next update after 1 second
        self.after(1000, self.update_clock)
    def muqova(self):
        self.xis=tk.Label(self,text="0",font=("Arial",15))
        self.xis.place(x=10,y=330,width=300,height=40)
        tk.Label(self,text="Parking",font=("Arial",20)).place(x=300,y=0,width=400,height=40)
        tk.Label(self,text="Model",font=("Arial",15)).place(x=10,y=50,width=60,height=40)
        tk.Label(self,text="State number",font=("Arial",15)).place(x=10,y=130,width=120,height=40)
        tk.Label(self,text="duration of stay (h)",font=("Arial",15)).place(x=10,y=210,width=170,height=40)
        tk.Label(self,text="Cost",font=("Arial",15)).place(x=10,y=290,width=100,height=40)
        tk.Label(self,text="List",font=("Arial",17)).place(x=700,y=110,width=100,height=40)
    def kirit(self):
        self.entry1 = tk.Entry(self, font=("Arial", 13),bd=3)
        self.entry1.place(x=10, y=90, width=150, height=30)
        self.entry2 = tk.Entry(self, font=("Arial", 13),bd=3)
        self.entry2.place(x=10, y=170, width=150, height=30)
        self.entry3 = tk.Entry(self, font=("Arial", 13),bd=3)
        self.entry3.place(x=10, y=250, width=150, height=30)
    def tugma(self):
        button = tk.Button(self, text="Save", font=("Arial", 17), bd=7, highlightbackground="red", command=self.saqla)
        button.place(x=10, y=370, width=100, height=40)
        button.bind("<Enter>", self.on_enter) 
        button.bind("<Leave>", self.on_leave)

    def saqla(self):
        model = self.entry1.get()
        davlat = self.entry2.get()
        muddat = self.entry3.get()
        dav=davlat.replace(" ","")
        try:
            if type(int(muddat))==type(1):
                self.xis['text']=f"{1000*int(muddat)} $"
                if model == "" or davlat == "" or muddat == "":
                    mes.showerror("Error", "Information not fully entered!")
                else:
                    if 10>len(dav)>1:
                        if not(dav.isalpha()) and not(dav.isdigit()):
                            
                            lis1 = self.children['!listbox']
                            lis1.insert("end", f"{model} {davlat}".upper())
                            self.entry1.delete(0, 'end')
                            self.entry2.delete(0, 'end')
                            self.entry3.delete(0, 'end')
                            data = lis1.get("0", "end")
                            data2=lis1.get("0","end")              
                            for value in set(data):                       
                                if data.count(value) > 2:
                                    self.xis['text']="Just free"
                                    bon=True
                                    mes.showinfo(title="  BONUS",message="Since this is the 3rd time this car has used our service, we will give you a bonus of 1 free day")
                                    for i in range(data.count(value)):
                                        lis1.delete(lis1.get(0, "end").index(value))
                        else:
                            mes.showerror("Error","State must be number, number and letters")
                    else:
                        mes.showerror("Error","The country number was entered incorrectly")
            else:
                mes.showinfo(title="ERROR",message="Enter the term in the number!")
        except ValueError:
            if model == "" or davlat == "" or muddat == "":
                mes.showerror("Error", "Incomplete data entry!")
            else:
                mes.showinfo(title="ERROR",message="Enter the term in the number!")        
    def on_enter(self, event):
        event.widget.config(bg="cyan")
    def on_leave(self, event):
        event.widget.config(bg="SystemButtonFace")
    def lis(self):
        self.lis1 = tk.Listbox(self,font=("Arial",15),bd=5)
        self.lis1.place(x=450, y=150, width=700, height=500)
        self.lis1.bind('<<ListboxSelect>>', self.info)
    def info(self, event):
        global data
        w = event.widget
        try:
            idx = int(w.curselection()[0])
            value = w.get(idx)
            data = self.lis1.get("0", "end")
            mes.askyesno(title="Info", message=f"{value} {data.count(value)}  times added time {time.ctime()}")
        except IndexError as e:
            pass
if __name__ == "__main__":
    app = App()
    app.mainloop()
