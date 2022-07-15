# AdalmPluto
![This is an image](https://softei.com/wp-content/uploads/2020/10/ADALM-Pluto-1536x1186.jpg)

transferring data from a file to adalm pluto

**Installing PlutoSDR Driver**

The terminal commands below should build and install the latest version of:

1)libiio, Analog Device’s “cross-platform” library for interfacing hardware

2)libad9361-iio, AD9361 is the specific RF chip inside the PlutoSDR

3)pyadi-iio, the Pluto’s Python API, this is our end goal, but it depends on the previous two libraries
```
*sudo apt-get install build-essential git libxml2-dev bison flex libcdk5-dev cmake python3-pip libusb-1.0-0-dev libavahi-client-dev libavahi-common-dev libaio-dev
cd ~
git clone --branch v0.23 https://github.com/analogdevicesinc/libiio.git
cd libiio
mkdir build
cd build
cmake -DPYTHON_BINDINGS=ON ..
make -j$(nproc)
sudo make install
sudo ldconfig

cd 
git clone https://github.com/analogdevicesinc/libad9361-iio.git
cd libad9361-iio
mkdir build
cd build
cmake ..
make -j$(nproc)
sudo make install

cd ~
git clone https://github.com/analogdevicesinc/pyadi-iio.git
cd pyadi-iio
pip3 install --upgrade pip
pip3 install -r requirements.txt
sudo python3 setup.py install
```

**Testing PlutoSDR Drivers**

*Open a new terminal (in your VM) and type the following commands:*
```
python3
import adi
sdr = adi.Pluto('ip:192.168.2.1') # or whatever your Pluto's IP is
sdr.sample_rate = int(2.5e6)
sdr.rx()
```
