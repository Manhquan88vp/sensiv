from os import system'
system('pip install rich')
system('clear')
import rich
from time import sleep
from rich.progress import track

for step in track(range(27)):
	sleep(1)
	step


for i in range(0,10):
	print(i)
	sleep(1)
	
system("rm -rf storage/shared/Android/obb/com.dts.freefireth")

