from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import re
import pickle
from janome.tokenizer import Tokenizer

with open('anime_title.pickle', mode='rb') as f:
    anime_titles = pickle.load(f)


anime_index = {}
tagged_documents = []
for i, line in enumerate(anime_titles):
    anime_index[''.join(line)] = i
    tagged_documents.append(TaggedDocument(line, [i]))

model = Doc2Vec(documents=tagged_documents,
                vector_size=100,
                min_count=5,
                window=2,
                epochs=30,
                dm=0)

model.save('model/anime_title.model')

# print(anime_title[0])
# print(model.docvecs[0])
# print(model.docvecs[0].shape)

# print(model.docvecs.most_similar(0))

# print(anime_titles[10])
# print(anime_titles[anime_index[''.join(anime_titles[10])]])
# print(anime_index[''.join(anime_titles[10])])
# print("--------------------------")
# for p in model.docvecs.most_similar(anime_index['ボールルームへようこそ']):
#     print(anime_titles[p[0]])
