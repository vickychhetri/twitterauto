#Program to login and send message to lover or hater all day
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import sqlite3


#Design Page
class Window(Frame):
    def __init__(self,master=None):
        with open("userrecord.csv") as file_name:
            self.array = np.loadtxt(file_name, delimiter=",",  dtype='str')
        Frame.__init__(self,master)
        self.master=master
        self.configure(bg="black")
        self.pack(fill=BOTH,expand=1,ipadx="16",ipady="16")
        self.backcolor="black"
        self.fgcolor="green"
    
        text=Label(self,text="Software is designed and developed by www.vickychhetri.com . ",font=("Times New Roman",19),bg=self.backcolor,fg="green")
        text.place(x=70,y=350)
        text=Label(self,text="Twitter Handler Auto. ",font=("Times New Roman",19),bg=self.backcolor,fg="green")
        text.place(x=150,y=50)
        self.startButton=Button(self,text="Start Processing",command=self.startProgram,width="80",font=("Times New Roman",10),height="10",bg="green",fg="white")
        self.startButton.place(x=160,y=150)
    #Function to ADD message in random list
    def addItemInList(self):
        self.lb.insert('end', self.messageItem.get())
    def startProgram(self):
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
                username=driver.find_element(By.CSS_SELECTOR, value=".r-30o5oe")
                username.clear()
                username.send_keys( self.user)
                login = driver.find_element(By.CSS_SELECTOR, value="div.css-18t94o4:nth-child(6) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)").click()
                time.sleep(10)
                username2=driver.find_element(By.CSS_SELECTOR, value=".r-30o5oe")
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
                            print("No Need to like")
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
                time.sleep(5)
                logoutclick = driver.find_element(By.CSS_SELECTOR, value="div.css-18t94o4:nth-child(1)").click()
            
        except:
            tkinter.messagebox.showerror('Software','Something went wrong, close the application and try again.')

#Initializa tkinter
root= Tk()
app=Window(root)

#SET TITLE
root.wm_title("Software")
root.geometry("900x400")
root.resizable(False,False)
#Show WIindow
root.call('wm','iconphoto',root._w,PhotoImage(file='icon.png'))
root.mainloop()