#Program to login and send message to lover or hater all day
from attr import validate
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import tkinter.messagebox
from tkinter import *
# from PIL import Image, ImageTk
import numpy as np
import pandas as pd
import sqlite3
import threading
from tkinter import messagebox

#Design Page
class Window(Frame):
    def __init__(self,master=None):
        with open("userrecord.csv") as file_name:
            self.array = np.loadtxt(file_name, delimiter=",",  dtype='str')
        Frame.__init__(self,master)
        self.master=master
        self.configure(bg="white")
        self.pack(fill=BOTH,expand=1,ipadx="16",ipady="16")
        self.backcolor="white"
        self.fgcolor="black"
        text=Label(self,text=f"No. of Users to load: {len(self.array)}",font=("sans-serif",10),bg=self.backcolor,fg="black")
        text.place(x=250,y=250)
        text=Label(self,text="Software under www.vickychhetri.com . ",font=("sans-serif",10),bg=self.backcolor,fg="black")
        text.place(x=70,y=350)
        text=Label(self,text="Genius",font=("sans-serif",50),bg="white",fg="brown")
        text.place(x=300,y=20)
        self.text2=Label(self,text="$>",font=("sans-serif",9),bg="white",fg="red")
        self.text2.place(x=30,y=70)
        
        self.startButton=Button(self,text="Click Here to Restore Payload and Initiate Program",command=threading.Thread(target=self.startProgram).start,width="50",font=("sans-serif",15),height="2",bg="red",fg="white")
        # self.sep=Separator(self,orient='horizontal')
        # self.sep.place(x=0,y=150)
        self.startButton.place(x=160,y=150)
    #Function to ADD message in random list
    def addItemInList(self):
        self.lb.insert('end', self.messageItem.get())
    def startProgram(self):
        self.startButton['text']="Program Initiated"
        try:
            for each in self.array:
                self.user = each[0] 
                self.password = each[1]  
                self.unv=each[2]
                self.to = each[3]
                # options = FirefoxOptions()
                # options.add_argument("--headless")
                # driver = webdriver.Firefox(options=options)
                driver = webdriver.Firefox()
                driver.get("https://twitter.com/i/flow/login")
                #login
                time.sleep(5)
                # DROP MESSAGE
                self.text2['text']=f"Email:{each[0]}  with \n\n username {each[2]} loaded."
                time.sleep(1)
                username=driver.find_element(By.CSS_SELECTOR, value=".r-30o5oe")
                username.clear()
                username.send_keys( self.user)
                login = driver.find_element(By.CSS_SELECTOR, value="div.css-18t94o4:nth-child(6) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)").click()
                time.sleep(10)
                username2=driver.find_element(By.CSS_SELECTOR, value=".r-30o5oe")
                 if(username2):
                    username2.clear()
                    username2.send_keys(self.unv)
                    login2 = driver.find_element(By.CSS_SELECTOR, value=".r-19yznuf > div:nth-child(1)").click()
                    time.sleep(5)  
                password=driver.find_element(By.CSS_SELECTOR, value=".r-homxoj")
                password.clear()
                password.send_keys( self.password)
                login3 = driver.find_element(By.CSS_SELECTOR, value="span.css-bfa6kz:nth-child(1) > span:nth-child(1)").click()
                time.sleep(10) 
                searchbox=driver.find_element(By.CSS_SELECTOR, value=".r-30o5oe")
                searchbox.clear()
                searchbox.send_keys(self.to)
                time.sleep(5) 
                userfindandclcik = driver.find_element(By.CSS_SELECTOR, value="#typeaheadDropdown-1 > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)").click()
                time.sleep(5)
            

                SCROLL_PAUSE_TIME = 3
                last_height = 100
                
                newlast=0
                tempo_last=last_height
                for x in range(1,13):
                    try:
                        poststring=f"section.css-1dbjc4n:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child({x}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3)"
                        print(f"working inside try {x}")
                        postclick = driver.find_element(By.CSS_SELECTOR, value=poststring).click()
                        time.sleep(5) 
                        print(driver.current_url)
                        # Start Data check
                        conn = sqlite3.connect('tweet.db')
                        cursor = conn.execute(f"SELECT * from TwitterPOS where USER='{self.user}' AND POSTURL='{driver.current_url}'")

                        n = cursor.fetchall()
                        
                        if (len(n)>0):
                            self.text2['text']=f"Already Liked and retweeted \n Message: {n}"
                            time.sleep(1)
                        else: 
                            likeClick = driver.find_element(By.CSS_SELECTOR, value="div.r-1h0z5md:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
                            time.sleep(1) 
                            retweet = driver.find_element(By.CSS_SELECTOR, value="div.r-1h0z5md:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
                            time.sleep(1) 
                            retweetReclick = driver.find_element(By.CSS_SELECTOR, value="div.r-z2wwpe:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
                            time.sleep(1)
                            # Comment is not working till now , need to wrok in future 10/-6/2-22 recorded
                            # comment=driver.find_element(By.CSS_SELECTOR, value=".DraftEditor-editorContainer")
                            # comment.clear()
                            # comment.send_keys("nice")
                            # time.sleep(1)
                            # reply = driver.find_element(By.CSS_SELECTOR, value="div.r-42olwf:nth-child(2)").click()
                            conn = sqlite3.connect('tweet.db')
                            conn.execute(f"INSERT INTO TwitterPOS (USER,POSTURL) \
                                VALUES ('{self.user}','{driver.current_url}' )")
                            conn.commit()
                            self.text2['text']=f"like and retweet completed: \n like & retweet {self.user} {driver.current_url}"
                            time.sleep(1)
                        driver.back()
                        driver.execute_script(f"window.scrollTo(0, {x*100});")

                        time.sleep(5) 
                        driver.execute_script(f"window.scrollTo(0, {newlast});") 
                    except:
                        print(f"catch expection : {x}")
                        if x==3:
                            x=11
                        continue
                    finally:
                        conn.close()
                driver.get("https://twitter.com/logout")
                self.text2['text']=f"logout {self.user}"
                time.sleep(5)
                logoutclick = driver.find_element(By.CSS_SELECTOR, value="div.css-18t94o4:nth-child(1)").click()
            
        except:
            tkinter.messagebox.showerror('Software','Something went wrong, close the application and try again.')
#function to generate report from sql
def generateReport():
    db_file="tweet.db"
    conn = sqlite3.connect(db_file, isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM TwitterPOS", conn)
    db_df.to_csv('database.csv', index=False)
#function to do nothing
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
#function to show about message
def about():
   info=''' Software is develop by the Vicky Chhetri. To Know More About, kindly visit vickychhetri.com or email at admin@vickychhetri.com
   '''
   messagebox.showinfo('information', info)
#function to show help message
def help():
   info='''Email: admin@vickychhetri.com or Visit www.github.com/vickychhetri


   1.) Mozila Browser to crawl, login and to do tasks.
   2.) userrecords csv file as a payload.
   
   www.vickychhetri.com
   '''
   messagebox.showinfo('Help', info)
#Initializa tkinter
root= Tk()
app=Window(root)

#SET TITLE
root.wm_title("Works in Aryana Lab.")
root.geometry("900x400")
root.resizable(False,False)
#Show WIindow
root.call('wm','iconphoto',root._w,PhotoImage(file='icon.png'))
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Show Report", command=generateReport)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Report", menu=filemenu)
 
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help ", command=help)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


root.mainloop()
