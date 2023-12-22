import string
import random
import sys
import random

# Palavras que o texto [N]ão [P]ode [T]erminar
NPT = ['o', 'a', 'os', 'as', 'que', 'e', 'qual', 'do', 'da', 'de', 'dos', 'das', 'nas', 'em', 'no', 'na', 'ao']

class Node(object):
  def __init__(self, word):
    self.word = word
    self.weight = 1
    self.adjacent = {}

  def increment_weight(self, word):
    self.adjacent[word] = self.adjacent.get(word, 0) + 1

  def next_word(self):
    adjacents_list = list(self.adjacent.items())
    if len(adjacents_list) == 0:
      return None
    words = [t[0] for t in adjacents_list]
    probability = [t[1] for t in adjacents_list]
    return random.choices(words, probability)[0]

class Graph(object):
  def __init__(self):
    self.vertices = {}

  def add_node(self, word):
    self.vertices[word] = Node(word)

  def is_node_in_graph(self, word):
    return word in self.vertices

  def get_node(self, word):
    return self.vertices[word]
  
  def get_or_add_node(self, word):
    if self.is_node_in_graph(word) == False:
      self.add_node(word)
    return self.get_node(word)

  def get_next_word(self, current_word):
    return self.vertices[current_word.word].next_word()


def make_graph(words):
  g = Graph()
  prev_word = None
  for word in words:
    word_node = g.get_or_add_node(word)
    if prev_word:
      prev_word.increment_weight(word_node)
    prev_word = word_node
  return g

def compose(g, words, min_size, max_size):
  composition = []
  node = g.get_node(random.choice(words))
  length = random.randint(min_size, max_size)
  for _ in range(length):
    composition.append(node.word)
    node = g.get_next_word(node)
    if node == None: break
  if composition[-1].lower() in NPT:
    composition.pop()
  composition = ' '.join(composition)
  composition += random.choices(['.', '!', '?'], [6, 3, 1])[0]
  return composition.capitalize()

def generate(words, min_size, max_size):
  g = make_graph(words)
  print(compose(g, words, min_size, max_size), '\n')

def get_text(text_path):
  with open(text_path, 'rb') as file:
    text = file.read().decode("utf-8")
  return text

def no_punctuation(text):
  return text.translate(str.maketrans('', '', string.punctuation))

def get_words_from_text(text_path):
  text = no_punctuation(get_text(text_path))
  return text.split()

def main():
  if sys.argv[0] != 'generate.py' or len(sys.argv) <= 1:
    print('Digite o local do arquivo')
    return
  text_location = sys.argv[1]
  generations = 5
  min_size = 5
  max_size = 20
  if len(sys.argv) > 2:
    generations = int(sys.argv[2])
  if len(sys.argv) > 3:
    min_size = int(sys.argv[3])
  if len(sys.argv) > 4:
    max_size = int(sys.argv[4])
  words = get_words_from_text(text_location)
  for _ in range(generations):
    generate(words, min_size, max_size)

if __name__ == '__main__':
  main()

