import matplotlib.pyplot as plt

languages = ['hee', 'hoho', 'C++', 'Js', 'css']
popularity = [30, 25, 88, 69, 10]

plt.pie(popularity, labels=languages)
plt.title("Popularity of Programming Languages")

plt.show()
