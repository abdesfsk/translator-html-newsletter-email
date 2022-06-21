from tkinter import *
from deep_translator import GoogleTranslator as translator
import re
root=Tk()
#setting title
root.title("translator")
#setting window size
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
langs=['ar', 'nl', 'do', 'en', 'fr', 'de', 'it','pr', 'ru', 'es', 'sw']

#------------------Functions--------------------------------------------
def repl(x,f):
    text=f
    lang=getselectedlang()
    src=getselectedsrc()
    for t in x:
        if(len(t)>1000):
            tab=t.split(" ",500)
            for sel in tab:
                tr=translator(source=src, target=lang).translate(sel)
                text=text.replace(str(sel),str(tr))
        if(len(t)>1 and len(t)<1000):
            tr=translator(source=src, target=lang).translate(t)
            text=text.replace(str(t),str(tr))
    return text
def getselectedlang():
    selec = listlangs.get(listlangs.curselection())
    return(selec)
def getselectedsrc():
    srcs = listsrcs.get(listsrcs.curselection())
    return(srcs)
def translate():
    txt=Iutput.get('1.0', 'end-1c')
    txt=txt.replace("\n","")
    reg_str = ">(.*?)<"
    res = re.findall(reg_str, txt)
    text=repl(res,txt)
    Output.delete('1.0', 'end-1c')
    Output.insert("1.0",text)

#------------------widgests--------------------------------------------
listsrcs=Listbox(root)
listsrcs=Listbox(exportselection=0)
listsrcs["borderwidth"] = "1px"
listsrcs["fg"] = "#333333"
listsrcs["justify"] = "center"
listsrcs.place(x=480,y=60,width=113)
listsrcs.insert(END,*langs)
listlangs=Listbox(root)
listlangs=Listbox(exportselection=0)
listlangs["borderwidth"] = "1px"
listlangs["fg"] = "#333333"
listlangs["justify"] = "center"
listlangs.place(x=480,y=220,width=113)
listlangs.insert(END,*langs)
validate_bt=Button(root)
validate_bt["bg"] = "#000"
validate_bt["fg"] = "#fff"
validate_bt["justify"] = "center"
validate_bt["text"] = "Translate"
validate_bt.place(x=480,y=10,width=112,height=44)
validate_bt["command"] = translate
Iutput = Text(root, height = 5,width = 25,bg = "light cyan")
Iutput.place(x=10,y=260,width=459,height=238)
Iutput.place(x=10,y=10,width=459,height=243)
Output = Text(root, height = 5,width = 25,bg = "light cyan")
Output.place(x=10,y=260,width=459,height=238)







mainloop()
