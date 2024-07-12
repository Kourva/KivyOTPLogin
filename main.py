#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

# Description: Kivy OTP login screen
# Author     : kozyol
# Source code: https://github.com/kozyol/KivyOTPLogin

# Importing resources from import file
from Libraries.imports import *

# Importing KV syntax files
files = ["Login", "Menu"]
for file in files:
    with open(f"Resources/{file}.kv") as kv:
        Builder.load_string(kv.read())


# Login menu screen
class LoginMenu(Screen):

    # Method to clear OTP input
    def clear_input(self, *otps, status):
        for button in otps:
            button.text = ""
            button.foreground_color = (58/255, 188/255, 248/255, 1)
        status.text = "Tap on input to change it!"
        status.color = (200/255, 200/255, 200/255, 1)

    # Method to start menu screen after successful login
    def start_menu_screen(self, *args):
        app = App.get_running_app()
        app.root.current = "Menu"
        app.root.transition.direction = 'left'

    # Method to login
    def login(self, *otps, status):
        # Get OTP code from buttons
        code = "".join(button.text for button in otps)
        
        # If code is valid, go to menu screen
        if code == "012345" and len(code) == 6:
            status.text = "Login successful"
            status.color = (0, 214/255, 0, 1)

            for index, button in enumerate(otps, start=1):
                animation = (
                    Animation(
                        foreground_color=(0, 214/255, 0, 1), 
                        duration=index/6
                    )
                )
                if index == 6:
                    animation.bind(on_complete=self.start_menu_screen)
                animation.start(button)

        # Otherwise send error and makes buttons color red
        else:
            status.text = "Invalid code"
            status.color = (214/255, 0, 0, 1)

            for index, button in enumerate(otps, start=1):
                animation = (
                    Animation(
                        foreground_color=(214/255, 0, 0, 1), 
                        duration=index/6
                    )
                )
                animation.start(button)

# Main menu screen
class MainMenu(Screen):
    # Local methods (root.xxx instead of app.xxx) and assets here
    pass


# Main class for app
class OTPLogin(App):
    # Build method
    def build(self):

        # Screen manager to have multi screens
        self.root = ScreenManager()

        # Setting Login screen and Menu screen to it
        login_screen = LoginMenu(name="Login")
        menu_screen = MainMenu(name="Menu")

        # Adding screens to screen manager
        self.root.add_widget(login_screen)
        self.root.add_widget(menu_screen)

        # Set starting screen and return screen manager
        self.root.current = "Login"
        return self.root

# Run the app
if __name__ == "__main__":
    OTPLogin().run()
