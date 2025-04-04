import tkinter  # Import standard module

window = tkinter.Tk()
c = tkinter.Canvas(window, width=200, height=200)  # Specify a size for the canvas
c.pack()

'''
Draw a neutral face
'''
# # Function to draw a neutral face
# def render_neutral_face():
#     # Draw face
#     c.create_oval(50, 50, 120, 120)  
#     # Draw eyes
#     c.create_oval(60, 60, 80, 80)  
#     c.create_oval(90, 60, 110, 80)  
#     # Draw pupils
#     c.create_oval(65, 65, 75, 75, fill="black")  
#     c.create_oval(95, 65, 105, 75, fill="black")  
#     # Draw mouth
#     c.create_line(70, 110, 100, 110)  

# # Call the function to draw the face
# render_neutral_face()

# window.mainloop()  # Start the Tkinter event loop

'''
Draw a smiley face
'''

# def render_smile_face():
#     # draw face
#     c.create_oval(50, 50, 120, 120)
#     # draw eyes
#     c.create_oval(60, 60, 80, 80)
#     c.create_oval(90, 60, 110, 80)
#     # draw pupils
#     c.create_oval(65, 65, 75, 75, fill="black")
#     c.create_oval(95, 65, 105, 75, fill="black")
#     # draw smiley mouth
#     # c.create_arc(60, 110, 110, 80, start=0, extent=-180)
#     c.create_arc(60, 110, 110, 80, start=0, extent=-180, style = "arc")

# render_smile_face()
# window.mainloop()

'''
Draw a sad face
'''
# def sad_face():
# # Draw face
#     c.create_oval(50, 50, 150, 150, outline="black", width=2)
#     # Draw eyes
#     c.create_oval(70, 80, 90, 100, outline="black", width=2)  # Left eye
#     c.create_oval(110, 80, 130, 100, outline="black", width=2)  # Right eye
#     # Draw pupils
#     c.create_oval(78, 88, 82, 92, fill="black")  # Left pupil
#     c.create_oval(118, 88, 122, 92, fill="black")  # Right pupil
#     # Draw angry eyebrows (tilted downward)
#     c.create_line(65, 75, 95, 65, width=3)  # Left eyebrow
#     c.create_line(105, 65, 135, 75, width=3)  # Right eyebrow
#     # Draw angry mouth (frown)
#     c.create_arc(80, 120, 120, 140, start=0, extent=180, style="arc", width=2)

# sad_face()
# window.mainloop()


# def angry_face():
#     # Draw face
#     c.create_oval(50, 50, 150, 150, outline="black", width=2)

#     # Draw eyes
#     c.create_oval(70, 80, 90, 100, outline="black", width=2)  # Left eye
#     c.create_oval(110, 80, 130, 100, outline="black", width=2)  # Right eye

#     # Draw pupils
#     c.create_oval(78, 88, 82, 92, fill="black")  # Left pupil
#     c.create_oval(118, 88, 122, 92, fill="black")  # Right pupil

#     # Draw **angry eyebrows** (tilted inward like a V)
#     c.create_line(65, 70, 90, 75, width=3)  # Left eyebrow (angling downwards to center)
#     c.create_line(110, 75, 135, 70, width=3)  # Right eyebrow (angling downwards to center)

#     # Draw **angry mouth** (sharp, downturned curve)
#     c.create_line(80, 130, 100, 120, 120, 130, smooth=True, width=3)
    


# angry_face()

# window.mainloop()



