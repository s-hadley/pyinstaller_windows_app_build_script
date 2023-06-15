# PyInstaller Build Script

This script uses [PyInstaller](https://pypi.org/project/pyinstaller/) to build your Python project into a .exe app for Windows.

* Builds single file .exe app
* Sets app icon
* Can include image files that might not be found by PyInstaller automatically
* Can include entire Python modules (modules sometime use files that are not automatically found by PyInstaller)
* Includes app version number in app name

When I ran PyInstaller version 5.10.0 from code (```PyInstaller.__main__.run([```) I was unable to get some of 
the more obscure commands (```--collect-all```) to work. I found that those commands worked when PyInstaller was run from
the command line, hence this build script.

### Requirements
* Windows only. This script has not been tested on other OSs
* Python 3. This script was tested with Python 3.10.7
* You need to have the [PyInstaller](https://pypi.org/project/pyinstaller/) module installed.
* This repo contains a ```requirements.txt``` file. Open a command prompt, navigate to this code base and run:
```
python -m pip install -r requirements.txt
```
  * The ```requirements.txt``` file refers to a specific version of PyInstaller. Install PyInstaller independently 
(```python -m pip install PyInstaller```) if you want to use the latest version of PyInstaller

### Getting Started
Run the following command build the ```demo_app.py``` Python script provided in this repo into a Windows .exe.
```
python build_exe.py
```
    
### Tailoring the Build Script to Your Needs


* In ```build_exe.py```, adjust the PyInstaller Command Prompt command to meet your needs. Instructions are provided in the code comments.
*  
* 
* You will need to [install PyInstaller via pip](https://pypi.org/project/pyinstaller/)
* Please read the comments in the ```build_exe.py``` file, you may need to adjust the ```command_text``` based on how Python is called in your command prompt.
* Run the build script:
```
python build_exe.py
```

### Support
Got questions? Feel free to email me at:
* support@hadleytechnicalservices.com

If you need an extra hand with your coding project - I do freelance work.

### Contributing Code Updates To This Repo
Feel free to fork this repo and send me a pull request!
