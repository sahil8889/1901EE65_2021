#Sahil Vaghasiya - 1901EE65

import os
import re
import pysrt

def regex_renamer():

	# Taking input from the user

	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")

	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))

	if(webseries_num==1):
		s="s"
		if(season_padding<10):
			s= s+ "0"
		s = s+ str(season_padding)
		s = s+ "e"
		if(episode_padding<10):
			s = s+ "0"
		s = s + str(episode_padding)
		count=0
		path= 'wrong_srt/Breaking Bad/'
		for filename in os.listdir(path):
			t=re.findall(s, filename)
			if(len(t)>0):
				count=1
				filename=re.sub('.mp4', '', filename)
				filename=re.sub('.srt', '', filename)
				filename=re.sub(' 720p.BRrip.Sujaidr', '', filename)
				filename=re.sub(' 720p.BRrip.Sujaidr', '', filename)
				if(season_padding,10):
					s1= "s0" + str(season_padding)
				else:
					s1= "s" + str(season_padding)
				if(episode_padding<10):
					s1= s1 + "e0" + str(episode_padding)
				else:
					s1+ s1 + "e" + str(episode_padding)
				s2= "- Season "+str(season_padding) + " Episode "+ str(episode_padding)
				y=re.sub(s1 ,s2, filename)
				file=pysrt.SubRipFile()
				path1='correct_srt/Breaking Bad/'+ y + '.srt'
				file.save(path1)
				path2='correct_srt/Breaking Bad/'+ y + '.MP4'
				file.save(path2)
		if(count==0):
			print('\nEnter Valid Input Corresponding Given Data\n')
		
	elif(webseries_num==2):
		s=""
		s= s+ "x"
		s =str(season_padding) + s
		if(episode_padding<10):
			s = s+ "0"
		s = s + str(episode_padding)
		count=0
		path= 'wrong_srt/Game of Thrones/'
		for filename in os.listdir(path):
			t=re.findall(s, filename)
			if(len(t)>0):
				count=1
				filename=re.sub('.mp4', '', filename)
				filename=re.sub('.srt', '', filename)
				filename=re.sub('.WEB.REPACK.MEMENTO.en', '', filename)
				if(episode_padding<10):
					s1=str(season_padding) + "x" + "0" + str(episode_padding)
				else:
					s1=str(season_padding) + "x" + str(episode_padding)
				s2= "Season "+str(season_padding) + " Episode "+ str(episode_padding)
				y=re.sub(s1 ,s2, filename)
				file=pysrt.SubRipFile()
				path1='correct_srt/Game of Thrones/'+ y + '.srt'
				file.save(path1)
				path2='correct_srt/Game of Thrones/'+ y + '.MP4'
				file.save(path2)
		if(count==0):
			print('\nEnter Valid Input Corresponding Given Data\n')
	else:
		s=""
		s= s+ "x"
		s =str(season_padding) + s
		if(episode_padding<10):
			s = s+ "0"
		s = s + str(episode_padding)
		count=0
		path= 'wrong_srt/Lucifer/'
		for filename in os.listdir(path):
			t=re.findall(s, filename)
			if(len(t)>0):
				count=1
				filename=re.sub('.mp4', '', filename)
				filename=re.sub('.srt', '', filename)
				filename=re.sub('.HDTV.CAKES.en', '', filename)
				if(episode_padding<10):
					s1=str(season_padding) + "x" + "0" + str(episode_padding)
				else:
					s1=str(season_padding) + "x" + str(episode_padding)
				s2= "Season "+str(season_padding) + " Episode "+ str(episode_padding)
				y=re.sub(s1 ,s2, filename)
				file=pysrt.SubRipFile()
				path1='correct_srt/Lucifer/'+ y + '.srt'
				file.save(path1)
				path2='correct_srt/Lucifer/'+ y + '.MP4'
				file.save(path2)
		if(count==0):
			print('\nEnter Valid Input Corresponding Given Data\n')
	

regex_renamer()