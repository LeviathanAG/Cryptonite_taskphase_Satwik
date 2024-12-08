# Forensics

## Scan surprise

Just had to open the qr code and scan it on a phone to get the flag.

![alt text](/PicoCTF/imagesforrev/flag.png)

The flag : picoCTF{p33k_@_b00_b5ce2572}


## Trivial Flag Transfer Protocol

### Thought process and approach 

I downloaded the `tftp.pcapng` from the website. I was familiar with `pcap` files but wasn't sure what `pcapng` meant so I googled it. It turns out thats its an upgrade to the `pcap` format. I worked with `pcap` files in KernelCTF so I opened it in Wireshark.

![](https://i.imgur.com/Q9EKkri.png)

There seems to be an `instructions.txt` file being transmitted but it was all in the format of data packets so I looked for a tool to recover the files. I went through the resources provided in the pdf and came across [Network Miner](https://www.netresec.com/?page=NetworkMiner). I downloaded it and tried to import the `tftp.pcapng` file but it required premium to open so I converted the `pcapng` file into a `pcap` file using `editcap -F tftp.pcapng tftp1.pcap` and opened it in Network Miner.

![](../resources/Trivial_Flag/networkminer.png)

I downloaded all the files from Netork Miner into a folder. When I opened `instructions.txt`, I found it to be encrypted. I tried to decrypt it using different ciphers in `CyberChef` and found that it was encrypted using `ROT13`. Decrypting it gave:

```
TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN
```

There was also a `plan` file which was also encrypted using `ROT13`. Decrypting it gave:

```
I USED THE PROGRAM AND HID IT WITH - DUEDILIGENCE. CHECK OUT THE PHOTOS
```

There was a `program.deb` file which I tried to install, When trying to install, I found out that it was `steghide`:

![](https://i.imgur.com/6F43Y0A.png)

I have used `steghide` in a previous CTF so I knew that it's used to hide files in images. I tried to extract the different image files I got from Network Miner, providing the password as `DUEDILIGENCE`. In the `picture3.bmp` file, I got the file `flag.txt` which contained the flag:


The flag is:

```  
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```

## Tunn3l v1s10n
We get a corrupted file `tunnel vision`.First I had to find out what type of file it was.
After trying multiple linux commands like `file`. I tried opening it up in exiftool as there was a similar problem in OASIS. after a little bit of googling on how to use exiftool I understood its a bitmap file but it had a broken header. To fix this problem, I did some reading : https://en.wikipedia.org/wiki/BMP_file_format. I tried fixing the header using the structure given in the file. according to the Wiki page, this first 4 bytes of the DIB header should dictate the size of that very header, so following the idea that this should be 40 bytes long, I replaced the size by 00 00 00 28 which showed me half the image 

and it contained a decoy flag. Now the image had some whitespace other than half the image so I tried messing with height and width parametres. When I tried changing the width, It gave me a distorted image but when I messed with the height and changed the parametres to `32 03 00 00` I got the final image and thus the flag.

![alt text](/assets/tunnel.png)

Thus the flag : `picoCTF{qu1t3_a_v13w_2020}`

## Moon Walk

Got a .wav file. tried a morse decoder (wasnt hopeful) and spectrogram analyzer but no progress. 
Looking the hints I researched about how data was transmitted during the lunar mission.

* Thus I came across an application called qsstv. 
https://en.wikipedia.org/wiki/Slow-scan_television

* I installed qsstv to investigate further.
* https://github.com/ON4QZ/QSSTV
```
apt install pkg-config g++ libfftw3-dev qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools libqt5svg5-dev libhamlib++-dev libasound2-dev libpulse-dev libopenjp2-7 libopenjp2-7-dev libv4l-dev build-essential
mkdir src/build
cd src/build
qmake ..
make -j2
sudo make install
```
Next I ran these commands after reading some documentation : https://github.com/ON4QZ/QSSTV
```
pactl load-module module-null-sink sink_name=virtual-cable
22
pavucontrol # A GUI will pop-up, go to the "Output Devices" tab to verify that you have the "Null Output" device

qsstv # The program GUI will pop-up, go to "Options" -> "Configuration" -> "Sound" and select the "PulseAudio" Audio Interface
 
Back in the pavucontrol GUI, select the "Recording" tab and specify that QSSTV should capture audio from the Null Output

```

The hint asked "What is the CMU mascot?" - the answer is "Scotty the Scottie Dog". This hinted that we should select "Scottie 1" as QSSTV's "Mode". I also had to select "Auto Slant" via trial and error.

Then I ran these commands in the terminal :

```

paplay -d virtual-cable message.wav

```
and finally I got the flag.

![alt text](/assets/moon.png)

The flag : `picoCTF{beep_boop_im_in_space}`




