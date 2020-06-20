from wordcloud import  WordCloud
import matplotlib.pyplot as plt
text = "I am Tushar Dimri "
wordcloud = WordCloud(max_font_size = 40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation= "bilinear")
plt.axis("off")
plt.show()