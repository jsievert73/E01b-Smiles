#!/usr/bin/env python3
#imports the required components to run our program
import utils, open_color, arcade
#makes sure we have the right version of utils imported
utils.check_version((3,7))
#sets the variables for screen width and height.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#Titles the screen
SCREEN_TITLE = "Smiley Face Example"
#creates our class to run this program
class Faces(arcade.Window):
    """ Our custom Window Class"""
    #initalizes the aspect of the program that will track our mouse.
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True)
        #creates the starting position for our smiley face by setting our default
        #variables to the middle of our screen
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        #sets the background to white. 
        arcade.set_background_color(open_color.white)
    #starts a function defining what should be drawn by the program, which will be
    #called whenever the mouse is moved
    def on_draw(self):
        """ Draw the face """
        #begins the rendering of our picture
        arcade.start_render()
        #centers the coordinates on our mouse or default coordinates
        face_x,face_y = (self.x,self.y)
        #from this we adjust the relative spacing of everything, like we did in main3.py
        smile_x,smile_y = (face_x + 0,face_y - 10)
        eye1_x,eye1_y = (face_x - 25,face_y + 40) 
        eye2_x,eye2_y = (face_x + 25,face_y + 40)
        catch1_x,catch1_y = (face_x - 22,face_y + 50) 
        catch2_x,catch2_y = (face_x + 28,face_y + 50) 
        #now that the variables are set, we will actually draw the picture
        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)
        arcade.draw_ellipse_filled(eye1_x,eye1_y,30,45,open_color.black)
        arcade.draw_ellipse_filled(eye2_x,eye2_y,30,45,open_color.black)
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)

    #a function that will be called whenever the mouse is moved within the screen
    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        #sets our centering variables to the current mouse position.
        self.x = x
        self.y = y


#runs the class faces(), which tracks the movement and draws the smiley, within the window
window = Faces()
#runs the arcade which is needed for our picture to be visible
arcade.run()