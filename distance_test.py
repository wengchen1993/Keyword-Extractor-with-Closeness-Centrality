import re
import pprint
import string
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

# Initialize stemmer and lemmatizer
stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()
pp = pprint.PrettyPrinter(indent=4)

# Load stopwords list
with open('stopWords.txt') as sw:
    swList = [line.rstrip() for line in sw]
sw.close()

swList = ' '.join(swList)

# Load alibaba story texts
with open('alibaba.txt') as ab:
    baba = [line.rstrip() for line in ab]
ab.close()


# Other sample stories, retrieved from Grenfell tower news and short description on Haruki Murakami's book
'''
story = 'Police have said they are considering manslaughter charges in relation to the deadly Grenfell Tower blaze as they revealed that the insulation and cladding tiles at the building failed safety tests. \
Det Supt Fiona McCormack, who is overseeing the investigation, said on Friday that officers had established the initial cause of the fire was a fridge-freezer and that it was not started deliberately. \
She said they were trying to get to the bottom of why the fire grew so quickly and tests had pointed towards the cladding using aluminium composite tiles and the insulation behind it. Investigators will now seek to establish whether the use of these materials was illegal. \
McCormack said: “Preliminary tests show the insulation samples collected from Grenfell Tower combusted soon after the tests started. The initial test on the cladding tiles also failed the safety tests.” \
She added that the insulation proved “more flammable than the cladding”. McCormack said police would investigate how the tiles were installed. \
“We will identify and investigate any criminal offence and, of course, given the deaths of so many people, we are considering manslaughter, as well as criminal offences and breaches of legislation and regulations,” she said. \
McCormack said documents and materials had been seized from a number of organisations but no one had been questioned yet as it was too early in the investigation.'

story = 'Haruki Murakami needs little introduction: a literary sensation abroad as much as in his native Japan, he has won multiple international awards for his novels such as Norwegian Wood and 1Q84. In a 2004 interview with The Paris Review, Murakami remarked that one of the best things about writing books “is that you can dream while you are awake”. The dreamlike quality of the stories in Men Without Women is undoubtedly one of its chief attractions. Murakami’s womenless men live in perpetual daydreams, a state of mind often prompted by a loss of some kind. In one story, for example, an ageing plastic surgeon grows obsessed with a younger, idealised woman whose perfection causes him to fade, quite literally, into nothingness. Murakami’s latest is a hypnotising study of male loneliness.'
'''

story = ' '.join(list(filter(None, baba)))

# Remove everything except alphabets and numbers, convert to lowercase and split
trim_story = re.sub(r"[^A-Za-z0-9]+|\bs\b", " ", story).lower().split()

# Stemming can be added here
ori_str = list(filter(None, [ts if ts not in swList else '' for ts in trim_story]))

# Unique tokens list
uni_str = set(ori_str)

# Get nearest distance between two words in a corpus
def get_distance(words, word1, word2):
    ans = len(words)
    curr_word, curr_index = None, 0
    for index, word in enumerate(words):
        if word != word1 and word != word2: continue
        if curr_word and word != curr_word:
            ans = min(ans, index - curr_index)
        curr_word, curr_index = word, index
    return ans

res = {}
n = len(uni_str)
print("=============================")
print("Number of original words : {}".format(len(ori_str)))
print("Number of unique token: {}".format(n))
print("=============================")

for elem1 in uni_str:
    temp = []
    for elem2 in ori_str:
        if elem1 != elem2:
            temp.append(get_distance(ori_str, elem1, elem2))
        else:
            temp.append(0)
    res[elem1] = 1 / ( sum(temp) / (n - 1) )

res = sorted(res.items(), key = lambda x:x[1], reverse=True)
nn = int(n/3)
pp.pprint(res[:nn])
