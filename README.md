# smallTouchScreen
 Small GUI for Raspberry Pi

# WaveShare LCD
https://www.waveshare.com/wiki/3.5inch_RPi_LCD_(A)

# Development & Troubleshooting
## Touchscreen X-Y Input Backwards
```
sudo nano /usr/share/X11/xorg.conf.d/99-calibration.conf
```
Change SwapAxes from 1 to 0
Then reboot

## PyQt
sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools

If you see
```
qt.qpa.screen: QXcbConnection: Could not connect to display                                                                                                                                                                                 Could not connect to any X display.
```

Fix it with
```
export DISPLAY=:0.0