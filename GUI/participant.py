
import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
    def show(self):
        self.lift()
    
    def hide(self):
        self.hide()

class Login_Page(Page):
   
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Login page")
       label.pack(side="top", fill="none", expand=False)
       
       email_label = tk.Label(self, text = "Enter your Email")
       email_label.pack(side="top", fill="x",expand=False)
       email_entry = tk.Entry(self,width=10)
       email_entry.pack(side="top", fill="none", expand=False) 
       
       password_label = tk.Label(self,text= "Enter your password")
       password_label.pack(side="top", fill="x",expand=False)
       password_entry = tk.Entry(self, width=10)
       password_entry.pack(side="top", fill="none", expand=False)  
       
       buttonframe = tk.Frame(self)
       buttonframe.pack(side="top", fill="x", expand=False)
       login_button = tk.Button(buttonframe, text="Login", command=Login_Page.verifyLogin)
       login_button.pack(side="top", fill="none",expand=False) 
       
    #    home_page_button = tk.Button(buttonframe, text="Home Page", command=self.hide())
    #    home_page_button.pack(side="top", fill="none",expand=False)
   def verifyLogin():
      ## to-do : verify login
      print("Verifiquei")
 
       
class Register_Page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Register Page")
        label.pack(side="top", fill="both", expand=False)
        
        name_label = tk.Label(self, text = "Enter your first name")
        name_label.pack(side="top", fill="x",expand=False)
        name_entry = tk.Entry(self,width=10)
        name_entry.pack(side="top", fill="none", expand=False)
        
        surname_label = tk.Label(self,text= "Enter your surname")
        surname_label.pack(side="top", fill="x",expand=False)
        surname_entry = tk.Entry(self, width=10)
        surname_entry.pack(side="top", fill="none", expand=False)
        
        email_label = tk.Label(self, text = "Enter your Email")
        email_label.pack(side="top", fill="x",expand=False)
        email_entry = tk.Entry(self,width=10)
        email_entry.pack(side="top", fill="none", expand=False) 
        
        password_label = tk.Label(self,text= "Set your password")
        password_label.pack(side="top", fill="x",expand=False)
        password_entry = tk.Entry(self, width=10)
        password_entry.pack(side="top", fill="none", expand=False)  
        
        buttonframe = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        login_button = tk.Button(buttonframe, text="Register", command=Register_Page.insertUser)
        login_button.pack(side="top", fill="none",expand=False) 
        
       
   
    def insertUser():
      ## to do: CRUD
      
      print("Registrei")

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Login_Page(self)
        p2 = Register_Page(self)
      

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="bottom", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       

        b1 = tk.Button(buttonframe, text="Login Page", command=p1.show)
        b2 = tk.Button(buttonframe, text="Register Page", command=p2.show)
      

        b1.pack(side="bottom")
        b2.pack(side="bottom")

        ##p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Auction App")
    ##label = tk.Label(root, text="Auctions App")
    root.wm_geometry("400x400")
    root.mainloop()