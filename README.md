# Keyword-Extractor-with-Closeness-Centrality

Closeness Centrality is a measure of centrality of individual nodes within a network. This metric explains the role/importance of a node acting as the "middleman" allowing transfer of information between other nodes. Higher closeness centrality = more nodes have to go through this node to reach other nodes. 

# Experiment

Closeness centrality to be applied on vectors of words to see if keywords can be extracted. Brute force is used as this is a small experiment.

# Results

Quite accurate but not very scalable!

## Results from short story on Ali Baba and Forty Thieves

A quick peep on the top of keywords returned:

```
[   ('baba', 0.09611829944547136),
    ('ali', 0.09484106305367379),
    ('gold', 0.03565830721003135),
    ('wife', 0.020097173144876326),
    ('cassim', 0.017294626312538603),
    ('words', 0.016629357211384713),
    ('said', 0.01604726006260195),
    ('rich', 0.015273581738838537),
    ('see', 0.014914365320003276),
    ('door', 0.014876573483733857),
    ('sesame', 0.01447085950544645),
    ('rock', 0.013497478493028774),
    ('shut', 0.012645035781282569),
```

# Improvements
Names should be tokenised together and most importantly, scalability should be improved. 
