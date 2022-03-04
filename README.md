The code runs automated mobile testing on android emulator on Meraki android app.
Tools used :
1) Appium Server(Windows) v1.22.2
2) Appium inspector 
3) Android Emulator

Requirements to run this automation 
- Appium Server and Android emulator should be running in order to run this automation

Instructions to run 
1) Install python3
2) Setup python virtual environment 
3) git clone `git@github.com:sksehdev/meraki_android_automation.git`
4) cd `meraki_android_automation`
5) run `pip install -r requirements.txt` inside virtual environment
6) Add the API key in test_meraki.py(line 13) and arguments (desired_caps)to run the tests
4) Once the libraries are installed , run `pytest tests/ -s -v`
5) The tests will start executing 

Tests: 
There are 12 tests in total 

There is also sample report in this repo called report.html from the run 






