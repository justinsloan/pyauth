#!/usr/bin/env python3

"""
totp.py
ʻālualua - simple one-time passcode generator

CHANGE LOG
v1 - initial release, 4 MAY 2024
TODO: prompt for secret key if missing
TODO: securely store secret key
"""

import tkinter as tk
from tkinter import ttk
import time
import pyotp

SECRET = "akkkkkkkslvkhjasfnll"


class alualua(tk.Tk):

    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('ʻālualua')
        self.resizable(0, 0)
        #self.geometry('250x80')
        self['bg'] = 'black'

        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='black',
            foreground='black')

        # label
        self.label = ttk.Label(
            self,
            text=self.get_otp(),
            font=('Digital-7', 60))

        self.label.pack(expand=True)

        # schedule an update every 1 second
        self.label.after(1000, self.update)


    def get_otp(self):
        totp = pyotp.TOTP(SECRET)
        token = totp.now()
        return f"{token[:3]} {token[3:]}" # adds a space for readability


    def update(self):
        """ update the label every 1 second """
        seconds = self._get_remaining_time()
        color = self._get_color(seconds)

        self.title('ʻālualua    (  i koe: ' + str(seconds) + '  )')
        self.label.configure(text=self.get_otp())
        self.style.configure('TLabel', foreground=color)

        # schedule another update
        self.label.after(1000, self.update)


    def _get_remaining_time(self, period=30) -> float:
        """Return remaining time of an OTP code"""
        totp = pyotp.TOTP("", interval=float(period))
        time_remaining = (totp.interval - time.time()) % totp.interval
        return int(time_remaining)


    def _get_color(self, seconds):
        """Return color of the label based on remaining time"""
        if seconds < 6:
            return'red'
        elif seconds < 11:
            return 'yellow'
        else:
            return 'green'


if __name__ == "__main__":
    app = alualua()
    app.mainloop()
