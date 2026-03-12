# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
word_counts = {}

for i in range(n):
    word = input()
    
    word_counts[word] = word_counts.get(word,0) + 1
    
print(len(word_counts))
    
print(*(word_counts.values()))
