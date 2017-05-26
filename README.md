## Requirements
- Python 3

## Installation
```
# Install latest version of OpenCV 3 with Python 3 bindings
brew install opencv3 --without-python --with-python3 --c++11 --with-contrib
brew link --force opencv3

# Create virtual environment
py -m venv venv

# Add opencv3 to path in virtual environment
echo /usr/local/opt/opencv3/lib/python3.6/site-packages >> venv/lib/python3.6/site-packages/opencv3.pth

# Activate virtual environment
source venv/bin/activate

# Install Python dependencies in our virtual environment
pip3 install -r requirements.txt
```


