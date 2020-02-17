# Python Watermark

## Dev Setup macOS

```sh
vv
```

## Create Binaries

```sh
python setup.py py2app
sudo pyinstaller source/watermark.py -n Watermark --windowed --noconfirm --clean --onefile --icon=assets/Icon.icns
sudo pyinstaller --noconfirm ./Watermark.spec

```


<a href="https://www.vecteezy.com/"> Vectors by Vecteezy</a>


## Issues

on macOs Window not focused:
- argv_emulation=True,
- -psn File Handle

py2app -> Cannot bundle
pyinstaller -> Cannot use argv

