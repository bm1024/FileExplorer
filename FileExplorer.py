'''
Created on Apr 23, 2021
@author: Bianca Magyar
Description: Python program using tkinter that opens a filedialog to get the file path of a document selected.
Reference: GeeksForGeeks 
'''

#import components from tkinter library
from tkinter import Tk, Label, Button

#import filedialog module
from tkinter import filedialog

#function for opening the file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files", "*.txt*"),
                                                       ("all files", "*.*")))
    #dynamic window size
    window.geometry("")
    
    #change label contents
    prompt_label.configure(text="File Opened:\n" + filename)
    
    
if __name__ == "__main__":        
    
    #create root window
    window = Tk()
    window.iconbitmap("folder.ico")
        
    #set window title
    window.title("File Explorer")
    
    #set window size
    window.geometry("330x100")
    
    #set window background color
    window.config(background = "#272727")
    
    #create a file explorer label
    prompt_label = Label(window, text = "Browse files to get file path", height = 4, fg = "white", background = "#272727")
    prompt_label.grid(column=1, row=1, padx=(30,10), pady=(0,0), rowspan=2)
    
    #create browse button
    browse_button = Button(window, text = "Browse Files", command = browseFiles)
    browse_button.grid(column=2, row=1, padx=(0,40), pady=(20,5), ipadx=15)
    
    #create exit button
    exit_button = Button(window, text = "Exit", command = exit)
    exit_button.grid(column=2, row=2, padx=(0,40), pady=(0,20), ipadx=38)
    
    window.mainloop()


