# Some tips -

# use if not os.path.isfile(f) to check if it is file or folder and take necessary action
# if f.endswith(".txt"), take necessary action


# FMS = File Management System

# global path
import os
from tkinter import *
from tkinter import filedialog


class FMS () :
    global path
    path = os.getcwd ()
    filenames = os.listdir (path)

    def pc_path () :
        print (path)

    def chg_path (dp) :
        # This function allows the user to change default path (os.getcwd())
        path = dp
        print ("The new path is : ", end=" ")
        print (path)

    def name_files ()  -> object:
        filenames = os.listdir (path)
        print ("The file names are : ")
        print ()
        for f in filenames :
            print (f)

    def op () :
        root = Tk()

        def openprogram () :
            prog = filedialog.askopenfilename ()
            os.system ('"%s"' % prog)

        bt = Button (root, text="Open", command=openprogram).pack ()
        root.mainloop ()

    def del_st (type) :  # del_sf = delete specific file
        path = os.getcwd ()
        filenames = os.listdir (path)
        print ("This program removed : ")
        for f in filenames :
            if (f.endswith (type)) :
                os.remove (f)
                print (f)


FMS.name_files ()




