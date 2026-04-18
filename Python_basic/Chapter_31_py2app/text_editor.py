# text_editor.py

import tkinter as tk
import tkinter.font as tk_font
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename,asksaveasfilename

# New File
def mainNewFile(event=None):
    global mainFilePath
    if mainTextEditor.get('1.0',tk.END) != '\n':
        answer=tk.messagebox.askyesnocancel("Save changes?", "Do you want to save changes?")
        if answer is True:
            mainSaveFile()
            if mainFilePath != '':
                mainTextEditor.delete('1.0', tk.END)
        elif answer is False:
            mainTextEditor.delete('1.0', tk.END)
        else:
            return
    mainWindow.title("Text Editor")
    mainFilePath=''

# Open
def mainOpenFile(event=None):
    global mainFilePath
    if mainTextEditor.get('1.0',tk.END) != '\n':
        answer=tk.messagebox.askyesnocancel("Save changes?", "Do you want to save changes?")
        if answer is True:
            mainSaveFile()
        elif answer is False:
            pass            
        else:
            return
    mainFilePath=askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if mainFilePath:
        mainTextEditor.delete('1.0', tk.END)
        with open(mainFilePath, 'r') as mainInputFile:
            mainTextEditor.insert(tk.INSERT,mainInputFile.read())
    mainWindow.title("Text Editor - "+mainFilePath)

# Save
def mainSaveFile(event=None):
    if not mainFilePath:
        mainSaveAsFile()
    else:
        with open(mainFilePath, 'w') as mainOutputFile:
            mainOutputFile.write(mainTextEditor.get('1.0',tk.END+'-1c'))
    mainWindow.title("Text Editor - "+mainFilePath)

# Save As…
def mainSaveAsFile(event=None):
    global mainFilePath
    mainFilePath=asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if mainFilePath:
        with open(mainFilePath, 'w') as mainOutputFile:
            mainOutputFile.write(mainTextEditor.get('1.0',tk.END+'-1c'))
    mainWindow.title("Text Editor - "+mainFilePath)

# Undo
def mainUndoText(event=None):
    mainTextEditor.edit_undo()

# Redo
def mainRedoText(event=None):
    mainTextEditor.edit_redo()

# Cut
def mainCutText(event=None):
    try:
        mainCopyText()
        mainTextEditor.delete("sel.first", "sel.last")
    except tk.TclError:
        pass

# Copy
def mainCopyText(event=None):
    try:
        mainTextEditor.clipboard_clear()
        mainTextEditor.clipboard_append(mainTextEditor.selection_get()) 
    except tk.TclError:
        pass

# Paste
def mainPasteText(event=None):
    try:
        mainTextEditor.insert(tk.INSERT,mainTextEditor.clipboard_get())
    except tk.TclError:
        pass

# Word count
def mainUpdateWordCount():
    mainWordCount=mainTextEditor.get('1.0','end')
    mainWordCount=mainWordCount.replace("\n", "")
    word_count=len(mainWordCount)
    mainWordCountLabel.config(text=' Words: '+str(word_count)+'    ')
    mainWindow.after(1000,mainUpdateWordCount)

# Close window
def mainCloseWindow(event=None):
    if mainTextEditor.get('1.0',tk.END) != '\n':
        answer=tk.messagebox.askyesnocancel("Save changes?", "Do you want to save changes?")
        if answer is True:
            mainSaveFile()
            mainWindow.destroy()
        elif answer is False:
            mainWindow.destroy()
        else:
            return
    else:
        mainWindow.destroy()

# Initialize file path
global mainFilePath
mainFilePath=''

# Create the main window
mainWindow=tk.Tk()
mainWindow.title("Text Editor")
mainWindow.geometry('960x500+140+130')
mainWindow.minsize(800, 300)
mainWindow.maxsize(1280, 720)
mainWindow.resizable(True, True)

# Create the main window menu
mainMenu=tk.Menu(mainWindow)
mainWindow.config(menu=mainMenu)

mainMenuFile=tk.Menu(mainMenu,tearoff=0)
mainMenu.add_cascade(label='File',menu=mainMenuFile)
menu=mainMenuFile.add_command(label='New File',command=mainNewFile)
menu=mainMenuFile.add_command(label='Open…',command=mainOpenFile)
menu=mainMenuFile.add_command(label='Save',command=mainSaveFile)
menu=mainMenuFile.add_command(label='Save As…',command=mainSaveAsFile)

mainMenuEdit=tk.Menu(mainMenu,tearoff=0)
mainMenu.add_cascade(label='Edit',menu=mainMenuEdit)
mainMenuEdit.add_command(label='Undo',command=mainUndoText)
mainMenuEdit.add_command(label='Redo',command=mainRedoText)
mainMenuEdit.add_command(label='Cut',command=mainCutText)
mainMenuEdit.add_command(label='Copy',command=mainCopyText)
mainMenuEdit.add_command(label='Paste',command=mainPasteText)

# Create the shortcut key framework and shortcut keys, word count label for the main window
mainShortcutKeyFrame=tk.Frame(mainWindow)
mainShortcutKeyFrame.pack(side='top', fill='x')

mainShortcutKeyNew=tk.Button(mainShortcutKeyFrame,text="New File", width=5)
mainShortcutKeyNew.pack(side='left')
mainShortcutKeyNew.bind('<Button-1>',mainNewFile)

mainShortcutKeyNew=tk.Button(mainShortcutKeyFrame,text="Open…", width=5)
mainShortcutKeyNew.pack(side='left')
mainShortcutKeyNew.bind('<Button-1>',mainOpenFile)

mainShortcutKeySave=tk.Button(mainShortcutKeyFrame,text="Save", width=5)
mainShortcutKeySave.pack(side='left')
mainShortcutKeySave.bind('<Button-1>',mainSaveFile)

mainShortcutKeySaveAs=tk.Button(mainShortcutKeyFrame,text="Save As…", width=5)
mainShortcutKeySaveAs.pack(side='left')
mainShortcutKeySaveAs.bind('<Button-1>',mainSaveAsFile)

mainShortcutKeyUndo=tk.Button(mainShortcutKeyFrame,text="Undo", width=5)
mainShortcutKeyUndo.pack(side='left')
mainShortcutKeyUndo.bind('<Button-1>',mainUndoText)

mainShortcutKeyRedo=tk.Button(mainShortcutKeyFrame,text="Redo", width=5)
mainShortcutKeyRedo.pack(side='left')
mainShortcutKeyRedo.bind('<Button-1>',mainRedoText)

mainShortcutKeyCut=tk.Button(mainShortcutKeyFrame,text="Cut", width=5)
mainShortcutKeyCut.pack(side='left')
mainShortcutKeyCut.bind('<Button-1>',mainCutText)

mainShortcutKeyCopy=tk.Button(mainShortcutKeyFrame,text="Copy", width=5)
mainShortcutKeyCopy.pack(side='left')
mainShortcutKeyCopy.bind('<Button-1>',mainCopyText)

mainShortcutKeyPaste=tk.Button(mainShortcutKeyFrame,text="Paste", width=5)
mainShortcutKeyPaste.pack(side='left')
mainShortcutKeyPaste.bind('<Button-1>',mainPasteText)

mainWordCountLabel=tk.Label(mainShortcutKeyFrame,text=' Words: 0    ')
mainWordCountLabel.pack(side='right')

# Create the text editing area
mainTextEditor=ScrolledText(mainWindow,undo=True)
mainTextEditor.config(font=tk_font.Font(size=15))
mainTextEditor.pack(side='bottom',expand=True,fill='both')

# Activate word count statistics
mainWindow.after(1000,mainUpdateWordCount)

# Activate check for saved updates when closing the window
mainWindow.protocol("WM_DELETE_WINDOW",mainCloseWindow)

mainWindow.mainloop()