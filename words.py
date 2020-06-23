from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
	story_words = []
	for words in story:
		linewords = list(words.decode().split( ))
		for line in linewords:
			story_words.append(line)
	r = " ".join(story_words)
	print(r)
