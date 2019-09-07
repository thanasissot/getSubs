import subprocess
import os
import pyautogui
import time


def main():
	# change directory paths
	pyautogui.FAILSAFE = True
	# path = '/home/thanasis/House MD Season 1, 2, 3, 4, 5, 6, 7 & 8 + Extras DVDRip TSV/Season 2'
	# /home/thanasis/House MD Season 1, 2, 3, 4, 5, 6, 7 & 8 + Extras DVDRip TSV/Season 2
	path = input('Enter the folder\'s path: ')
	os.chdir(path)
	print("""\nMake sure there is not other type of file in that folder except video type files\nAlso make sure vlc is the default application\n""")
	run = input('Do you want to continue? (Y/N)\n')

	if run.lower().startswith('y'):
		# get all the name os the files in a list
		alist = subprocess.run(['ls'],capture_output=True)
		alist = alist.stdout.decode().split('\n')
		alist = alist[:len(alist)-1]

		# run only the first file to capture coordinates
		print('\nWe will now run a trial to capture the coordinates of the proper buttons.')
		print('The first file on the folder will now run.')
		print('After that you will have 3 seconds to place the mouse pointer in the exact location specified.\n')
		print('It make take you up to 2-3 tries to get the correct coordinates')
		print('Also try not to have any other windows open cause the VLsub menu can appear anywhere\n')
		run2 = input('Are you ready to continue? (Y/N)\n')

		if run2.lower().startswith('y'):
			coords = []
			subprocess.run(['xdg-open', alist[0]])
			time.sleep(1)
			buttons = ('View (and click it after Done)', 'VLsub (and click it after Done)', 'Search by hash', 
					  'Point the first item on the subtitles list', 
					  'Download Selection', 
					  'X(close button, top corner)')

			for button in buttons:
				print('Point at', button)
				time.sleep(2.1)
				mousePos = pyautogui.position()
				print('Done')
				coords.append((mousePos.x, mousePos.y))
				time.sleep(1.1)


			print('Closing the current file...')
			time.sleep(2)
			pyautogui.click(coords[-1][0], coords[-1][1])


			print(coords)

			for avi in alist:
				# run avi
				subprocess.run(['xdg-open', avi])
				# time.sleep(1)
				for pos in coords:
					time.sleep(1.3)
					x, y = pos
					pyautogui.click(x, y)


if __name__ == '__main__':
	main()