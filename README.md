# ADS-B-Ground-Station
A repository created for my Computer Systems &amp; Networking assignment 

Project Name: ADS-B-Ground-Station
Student Name: Adelle McAteer
Student ID: 20091411

Project Proposal
When I first heard about the RaspberryPi project at the onsite day I started to think about what I
could do. I thought it would be interesting to use it to track planes flying overhead and know the
information from airline to type of plane.

Automatic Dependent Surveillance—Broadcast (ADS-B) or ADS-B is the technology that will allow
me to track flights. Aircraft are increasingly built or outfitted with ADS-B transponders. This data is
unencrypted and easily picked up by ground antennas.

While researching, I discovered FlightAware (a company who collect and publish the data of
worldwide flights on their website) have a package available for the RaspberryPi called PiAware.
I am going to use this to facilitate my assignment but hopefully build it up and use it to explore
networking and IoT in more depth.

I have already sourced the PiAware kit. So far, it has detected commercial, cargo and private
planes in the last 12 hours since setting it up. The information is available live when planes fly
overhead. There are a variety of statistics available also, but the live flight information is not
stored. I would like to tap into it more, possibly use the sense hat to light up when planes are
detected and use ThingSpeak and Twitter to publish information of flight activity

Technologies and Tools
- RaspberryPi4 with PiAware installed
- Raspberry Pi 3 Model B for data storage
- FlightAware Pro Stick Plus - FlightAware's USB SDR ADS-B Receiver with a built-in
- 1090MHz bandpass filter
- 1090MHz Desk Antenna - a 3dBi ADS-B 1090Mhz SMA Antenna with magnetic base
- FLIRC Case - aluminium case with a central cooling-core
- WiFi – to connect the RaspberyPi and data transmission
- Mobile phone for email & Twitter notification
- Python
- ThingSpeak/ThingTweet/THingHTTP
- IFTTT
- Twitter
- Firebase
- Glitch

Project Repository: https://github.com/AdelleMcateer/ADS-B-Ground-Station
