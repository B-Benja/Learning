 """ 
 example of a python code, that can run as module or script
 fetches words from URL and prints them; one word per line
 """ 

import sys
from urllib.request import urlopen


def fetch_words(url):
    """ receive a list of words from a URL 
    
    Args: the URL of a txt document
    
    Returns: stringt with the words from the document
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    """ Print one item per line    """
    for item in items:
        print(word)

def main(url):
    """ print each word from a txt document / from a URL
    
    Args: URL """
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1])