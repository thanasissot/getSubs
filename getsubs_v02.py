import subprocess
import os
import time
import requests
import urllib.parse

OPENSUBSAPIURL = 'https://rest.opensubtitles.org/search/'
# HEADERS = 
# one space left at the end of the string
TV_SERIES_NAME = 'House M.D. '
LANGUAGE = '/sublanguageid-ell'

def query(episode):
	""" returns encoded url for episode name ready for the body of the request
	"""
	query = ''.join(['query-',TV_SERIES_NAME, episode, LANGUAGE])
	link = urllib.parse.quote(query).lower()
	link = ''.join([OPENSUBSAPIURL, link])
	print('Link for', episode, 'acquired.')
	return link

def get_download_link(link):
	"""Returns download link of first result in the list of responses
	Or raises error if no results
	"""
	response = requests.get(
		link,
		headers = {'User-Agent' : 'thanasisnamikaze'}
		)
	try:
		dl_link = [x for x in response.json() if x['SubLanguageID'] == 'ell'][0]['SubDownloadLink']
		print('Download link acquired.')
		return dl_link
	except:
		print('Something went wrong in get_download_link()')

def download_file_and_name_sub(episode_name, dl_link):
	response = requests.get(dl_link)
	if response.status_code != 200:
		print('Error in download_file_and_name_sub()')
		return -1

	sub_name = ''.join([episode_name, '.srt'])
	open(sub_name, 'wb').write(response.content)
	print('Subtitle for', episode_name, 'successully downloaded.')


def main():
	# change directory paths
	path = '/home/thanasis/House MD Season 1, 2, 3, 4, 5, 6, 7 & 8 + Extras DVDRip TSV/Season 2'
	# /home/thanasis/House MD Season 1, 2, 3, 4, 5, 6, 7 & 8 + Extras DVDRip TSV/Season 2
	# path = input('Enter the folder\'s path: ')
	os.chdir(path)
	# episodes is a list with all episodes number and season that will be used
	# for the search query
	episodes = subprocess.run(['ls'],capture_output=True)
	episodes = episodes.stdout.decode().split('\n')

	# used for naming the subtitles
	episodesNames = [x[:len(x)-4] for x in episodes[:len(episodes)-1]]
	# used for finding the right subs to download
	episodes = [x[9:28].lower() for x in episodesNames]

	for episode, episode_name in zip(episodes, episodesNames):
		link = query(episode)
		dl_link = get_download_link(link)
		download_file_and_name_sub(episode_name, dl_link)



if __name__ == '__main__':
	main()