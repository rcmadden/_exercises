# Data Parser
## Write a Dataset Class
Stanford IMDB Movie Reviews data set: dataSentences.txt
[x]Skip first line (header: sentence, sentence number)

[x]Skip line numbers (first character on each line)
Only about 20,000 distinct words
## Write a Dataset Class
[x]All our code should be contained in its own class

[x]Constructor takes filename as input

[x]Need variables for the following: n_ sentences, vocab (all the distinct words), _words, all the sentences

[x]Dict. To map each word to a unique integer index

[x]Function to read file - sentences as [strings] (lowercase)

[x]Function to compile vocabulary of unique words to a list (return vocab, n_ words)

[x]Function to get word frequencies as a dictionary of key for word number of occurances as value