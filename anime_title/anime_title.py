from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pickle

with open('anime_title.pickle', mode='rb') as f:
    anime_titles = pickle.load(f)

anime_index = {}
for i, line in enumerate(anime_titles):
    anime_index[''.join(line)] = i

model = Doc2Vec.load('model/anime_title.model')

for p in model.docvecs.most_similar(anime_index['魔法科高校の劣等生']):
    print(anime_titles[p[0]])
