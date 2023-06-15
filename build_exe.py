##########################################################
#*** PyInstaller Build Script ****
##########################################################

# Imports
import subprocess
import default_settings
import os
import shutil

#*** Construct app name ***
app_version_no_dots = str(default_settings.APP_VERSION).replace('.','_')
app_name_no_spaces = str(default_settings.APP_NAME).replace(' ','_')
app_name = app_name_no_spaces+'_v'+app_version_no_dots

##########################################################
#*** PyInstaller Build Command ****
##########################################################

# Replace 'python' with the command you use to start Python in your command prompt. Normally it's 'python', so you
# might not have to change it.
# Replace 'demo_app.py' with the name of the Python script you want to turn into a .exe Windows app
command_text = 'python -m PyInstaller demo_app.py '

# Instructs PyInstaller to produce a single file .exe app. Do not change this command.
command_text +='--onefile '

# Sets file name of .exe app
command_text += '--name '+str(app_name)+' '

# Are you using any Python modules in your app that contain additional resources (files, executables, etc.) that are not
# being automatically added to the built .exe app by PyInstaller?
# If so, replace 'magicdaq' with the name of the module you need to include.
# You can repeat this command as many times as is needed to include all special modules.

#command_text += '--collect-all magicdaq '

# Are you using any additional files (image files, icons, etc.) in your app that are not being automatically added to
# the built .exe app by PyInstaller?
# If so, you can use this command to specify the files that should be bundled with the .exe app
# Replace 'image_1.png' with the name of your file
command_text += '--add-data "image_1.png;." '
command_text += '--add-data "image_2.png;." '
# IMPORTANT: remember to include your app icon as shown below
command_text += '--add-data "simple_hts_app_icon.ico;." '

# Sets the app icon for the .exe app file created
# Change 'simple_hts_app_icon.ico' to the file name of icon you would like to use
command_text += '--icon simple_hts_app_icon.ico '

# Instructs PyInstaller to save the newly created .exe app file in a new folder called 'executable'
command_text += '--distpath ./executable '

# The .exe built will be saved at this path
output_folder_path = './executable'

##########################################################
#*** Build the App ****
##########################################################

print('*** Building App into .exe *** ')
print(' ')

#*** Delete previous .exe if it exists ***
# We must delete the previously built app, or PyInstaller sometimes refuses to re-build the app from scratch
# (preforms some sort of diff function - which sometimes misses things)

if os.path.exists(output_folder_path):
    try:
        shutil.rmtree(output_folder_path)
        print('Good: deleted previous built /executable folder.')
        print(' ')
    except Exception as exception_text:
        print('ERROR: unable to delete previously built /executable folder.')
        print('Error text: '+str(exception_text))
        print(' ')

#*** Run PyInstaller ***
print('PyInstaller Command Being Run: ')
print(command_text)
print('')
print('IMPORTANT: check that the Python call in the above command is correct for your system!')
print('If it is not, modify the build_exe.py file to correct it!')
print('')

# print out in real time
process = subprocess.Popen(command_text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
for line in iter(process.stdout.readline, ''):
    print(line.strip())

process.stdout.close()
process.wait()

print('')
print('App build complete.')
print('EXE Name: '+str(app_name)+'.exe')
print('')
print('*** Build Script Complete ***')