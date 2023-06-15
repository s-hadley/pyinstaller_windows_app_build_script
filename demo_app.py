##########################################################
#*** Demo App ****
##########################################################

# This code creates a small tkinter app that displays two images
# It's included in this repo as an example, so that the build_exe.py script has something to build into an exe
# This code was created by ChatGPT; I then modified it for our purposes

import tkinter as tk
import default_settings
import resource


#*** Construct App Name ***
app_name = str(default_settings.APP_NAME+' v'+default_settings.APP_VERSION)

#*** Tkinter App ***
# Create the main tkinter window
window = tk.Tk()
window.title(app_name)

# Set app icon
window.iconbitmap(resource.get_path("simple_hts_app_icon.ico"))

# Load the first image
image_1 = tk.PhotoImage(file=resource.get_path("image_1.png"))

# Load the second image
image_2 = tk.PhotoImage(file=resource.get_path("image_2.png"))

# Create the first image label
label_1 = tk.Label(window, image=image_1)
label_1.pack(side=tk.LEFT, padx=10, pady=10)

# Create the second image label
label_2 = tk.Label(window, image=image_2)
label_2.pack(side=tk.RIGHT, padx=10, pady=10)

# Start the tkinter event loop
window.mainloop()

