# -*- coding: utf-8 -*-
import os
import sys
import tkinter as tk
import configparser
from tkinter import messagebox
from watermarker.marker import watermark_text


form = {}
fieldset = {}
config = configparser.ConfigParser(allow_no_value=True)
config_file = os.path.join(os.path.dirname(sys.argv[0]), 'settings.ini')


def load_settings(set_gui_form=False):

    config.read(config_file)

    form['text'] = config.get('WATERMARK', 'Text', fallback='Hello World')
    form['position'] = config.get('WATERMARK', 'Position', fallback='tl')

    if set_gui_form:
        fieldset['text'] = tk.StringVar(value=form['text'])
        fieldset['position'] = tk.StringVar(value=form['position'])


def save_settings():

    try:
        config.add_section('WATERMARK')
    except configparser.DuplicateSectionError:
        pass

    config.set('WATERMARK', 'Text', fieldset['text'].get())
    config.set('WATERMARK', 'Position', fieldset['position'].get())

    with open(config_file, 'w') as configfile:
        config.write(configfile)


def makewindow(root):

    window_width = 450
    window_height = 280

    root.minsize(window_width, window_height)
    root.title("Watermarker Einstellungen")

    x_cordinate = int((root.winfo_screenwidth() / 2) - (window_width / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (window_height / 2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


def makeform(root):

    form_frame = tk.Frame(root)
    form_frame.pack(side=tk.TOP, fill='x', padx=15, pady=15)

    label = tk.Label(form_frame, text="Text")
    label.pack(anchor='w')

    entry_text = tk.Entry(form_frame, textvariable=fieldset['text'])
    entry_text.pack(anchor='w', fill='x', pady=(5, 15))

    label = tk.Label(form_frame, text="Position")
    label.pack(anchor='w')

    tk.Radiobutton(form_frame, text="Oben links", variable=fieldset['position'], value="tl", tristatevalue=0).pack(anchor='w')
    tk.Radiobutton(form_frame, text="Oben rechts", variable=fieldset['position'], value="tr", tristatevalue=0).pack(anchor='w')
    tk.Radiobutton(form_frame, text="Unten links", variable=fieldset['position'], value="bl", tristatevalue=0).pack(anchor='w')
    tk.Radiobutton(form_frame, text="Unten rechts", variable=fieldset['position'], value="br", tristatevalue=0).pack(anchor='w')

    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side=tk.BOTTOM, fill='x')

    button_quit = tk.Button(bottom_frame, text='Speichern', command=save_settings, default='active')
    button_quit.pack(side=tk.RIGHT, padx=(0, 15), pady=15)

    button_cancel = tk.Button(bottom_frame, text='Beenden', command=root.quit)
    button_cancel.pack(side=tk.RIGHT, padx=5)

    label = tk.Label(bottom_frame, text="© 2020 Bastian Probian", font=("Helvetica", 10), fg='gray')
    label.pack(anchor='w', padx=(15, 0), pady=(18, 0))


if __name__ == '__main__':

    # Display Programm Options
    if len(sys.argv) == 1:
        root = tk.Tk()
        load_settings(set_gui_form=True)

        makewindow(root)
        makeform(root)

        root.call('wm', 'attributes', '.', '-topmost', True)
        root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)
        root.mainloop()

    # Add Watermark
    else:

        load_settings()
        files = set(sys.argv[1:])
        messagebox.showinfo('File', files)
        messagebox.showinfo('File', sys.argv)

        for file in files:
            # messagebox.showinfo('File', file)
            print("asd")
            file = '/Users/contmp/Desktop/IMG_0203.jpeg'
            watermark_text(file, '%s_watermarked.png' % file, text=form['text'])
            print("fer")
