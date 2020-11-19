import string
with open('the_stranger.txt', 'r') as f:
    sentence_list = [sentence.split() for sentence in f.readlines()]

    


flat_list = [item for sublist in sentence_list for item in sublist]



        

wordfreq  = []
for word in flat_list:
    if word not in wordfreq:
        wordfreq.append(word)

for i in range(0, len(wordfreq)):
    print(f"Frequency of {wordfreq[i]} is: {flat_list.count(wordfreq[i])}")

story_string = ' '.join(flat_list).translate(str.maketrans('', '', string.punctuation)).lower()
punct_free_list = story_string.split()


def fun(word_list): 
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"] 
    if word_list in stop_words: 
        return False
    else: 
        return True
filtered_list = list(filter(fun, punct_free_list))

with open('fitered_story.txt', 'w') as f:
    f.write(' '.join(filtered_list))
