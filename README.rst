**********************************************************************************************************
Thư viện chuyển đổi văn bản thành giọng nói cho ngôn ngữ lập trình Python hoạt động ở chế độ Offline
(tts_offline). 
**********************************************************************************************************

- Tương thích với Python 2 và 3
- Tốc độ đáp ứng nhanh hơn thư viện của Google


Cài đặt
************
::

	câu lệnh: pip install tts_offline


> If you get installation errors , make sure you first upgrade your wheel version using :  
`pip install --upgrade wheel`

**Đối với Linux :**
#####################################

+ Nếu sử dụng thư viện này trên hệ điều hành Linux gặp lỗi âm thanh thì hãy cài đặt   : 
espeak , ffmpeg và libespeak1 như sau: 

::

	sudo apt update && sudo apt install espeak ffmpeg libespeak1


Sử dụng :
************
::

	import pyttsx3
	engine = pyttsx3.init()
	engine.say("I will speak this text")
	engine.runAndWait()
	
	
**Thay đổi giọng đọc, Tốc độ đọc và âm lượng đọc :**

::

	import pyttsx3
	engine = pyttsx3.init() # object creation

	""" Tốc độ đọc"""
	rate = engine.getProperty('rate')   # getting details of current speaking rate
	print (rate)                        #printing current voice rate
	engine.setProperty('rate', 125)     # setting up new voice rate


	"""Âm lượng đọc"""
	volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
	print (volume)                          #printing current volume level
	engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

	"""Giọng đọc"""
	voices = engine.getProperty('voices')       #getting details of current voice
	#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
	engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

	engine.say("Hello World!")
	engine.say('My current speaking rate is ' + str(rate))
	engine.runAndWait()
	engine.stop()

	"""Saving Voice to a file"""
	# On linux make sure that 'espeak' and 'ffmpeg' are installed
	engine.save_to_file('Hello World', 'test.mp3')
	engine.runAndWait()


**Tài liệu tham khảo**
#####################################

https://pyttsx3.readthedocs.io/en/latest/


Thư viện cần thiết:
*********************
* sapi5
* nsss
* espeak



Liên kết:
**************

* PyPI (https://pypi.python.org)
* GitHub (https://github.com/nateshmbhat/pyttsx3)
* Full Documentation (https://pyttsx3.readthedocs.org)
