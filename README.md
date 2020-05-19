# Using a virtual environment with Sublime Text3 in Linux

# Sublime Text 3:
https://www.sublimetext.com/3
or
sudo snap install sublime-text

# Install Virtual Environment
>python3 -m venv venv

## Activate of virtual environment:
>source venv/bin/activate

## Deactivate
>deactivate

# Install qrcode:
pip install qrcode['pil']


# Set Build
Tolls --> Build System --> New Build System ...
<pre><code>
{
    "shell_cmd": "/path/to/virtual/enviroment/venv/bin/python3 -u \"$file\"",
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
}
</pre></code>

# Python Code for testing:
<pre><code>
import qrcode

img = qrcode.make("www.mps.co.at")
img.save("mps.png")
print("Done")
</pre></code>

# Change Build Settings:
cd ~/.config/sublime-text-3/Packages/User/filename
