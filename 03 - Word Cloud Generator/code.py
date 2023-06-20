from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the input text file
with open('input.txt', 'r') as file:
    text = file.read()

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400).generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(16, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('')
plt.show()

#Interpolation variations to use: nearest, bilinear, bicubic, lanczos, gaussian