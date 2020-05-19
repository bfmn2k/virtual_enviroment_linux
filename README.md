# Sublime Text 3:
https://www.sublimetext.com/3
or
sudo snap install sublime-text



# Install Virtual Enviroment
>python3 -m venv venv


## Activate of virtual environment:
>source venv/bin/activate

## Deactivate
>deactivate

# Install qrcode:
pip install qrcode['pil']


# Set Build
Tolls --> Build System --> New Build System ...
{
    "shell_cmd": "/path/to/virtual/enviroment/venv/bin/python3 -u \"$file\"",
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
}


# Python Code for testing:
import qrcode

img = qrcode.make("www.cmps.co.at")
img.save("mps.png")
print("Done")


# Change Build Settings:
cd ~/.config/sublime-text-3/Packages/User/<filename>
