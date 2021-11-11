#P2 More ffmpeg
import subprocess

ans=True
while ans:
    print("""
    1.Create a script which can cut N seconds the BBB video. 
    2.Create a script which will extract the YUV histogram from the previous BBB video you’ve done and create a new video with both images at the same time.
    3.Create a script which can resize the BBB video into 4 differents video outputs (doesn’t need to be at the same time)
        a) 720p
        b) 480p
        c) 360x240
        d) 160x120
    4.Create a script which can change the audio into mono output and in a different audio codec
        a)Change to mono audio
        b)Change to mp3
    5.Exit/Quit --> Press enter
    """)
    ans= input("What would you like to do? ")
    #Exercise 1
    if ans=="1":
        ans4 = input("How many seconds do you want from the video: ")
        sec  = "00:00:" + ans4
        subprocess.call(['ffmpeg','-ss', '00:00:00', '-i', 'bbb.mp4', '-to', sec , '-c', 'copy', 'output.mp4'])

    #Exercise 2
    elif ans=="2":
        subprocess.call(['ffplay', 'bbb.mp4', '-vf', 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay'])

    #Exercise 3
    elif ans=="3":
        ans2 = input("Choose video size a, b, c or d: ")
        if ans2 == "a":
            subprocess.call(['ffmpeg', '-i', 'output.mp4', '-s', '1280x720', '-c:a','copy', '1280x720.mp4'])
        elif ans2 == "b":
            subprocess.call(['ffmpeg', '-i', 'output.mp4', '-s', '640×480', '-c:a', 'copy', '640×480.mp4'])
        elif ans2 == "c":
            subprocess.call(['ffmpeg', '-i', 'output.mp4', '-s', '360x240', '-c:a', 'copy', '360x240.mp4'])
        elif ans2 == "d":
            subprocess.call(['ffmpeg', '-i', 'output.mp4', '-s', '160x120', '-c:a', 'copy', '160x120.mp4'])
        else:
            print("Enter a valid command")

    #Exercise 4
    elif ans=="4":
        ans3 = input("Choose a) mono auido b) Encode in different audio codec: ")
        if ans3 == "a":
            subprocess.call(['ffmpeg', '-i', 'output.mp4', '-ac', '1', 'mono.mp4'])
        elif ans3 == "b":
            subprocess.call(['ffmpeg', '-i', 'output.mp4', '-acodec', 'aac', '-vcodec', 'copy', 'audio_aac.mp4'])
        else:
            print("Please enter a valid command")

    else:
        print("Please enter a valid command")
        