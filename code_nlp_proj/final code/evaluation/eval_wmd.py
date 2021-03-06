import os

# Initial csv input file which consists of examples generated by different models
prediction_csv_path = 'cocon_gpt_preds_cocon_gpt_preds.csv'

# target distance file path 
target_file_path = "wmd_preds_3.tsv"

# sample sentence for WMD check
sentence_obama = 'Obama speaks to the media in Illinois'
sentence_president = 'The president greets the press in Chicago'

# Import and download stopwords from NLTK.
from nltk.corpus import stopwords
from nltk import download
download('stopwords')  # Download stopwords list.
stop_words = stopwords.words('english')

def preprocess(sentence):
    return [w for w in sentence.lower().split() if w not in stop_words]

# Preprocessing sentences before distance computation
sentence_obama = preprocess(sentence_obama)
sentence_president = preprocess(sentence_president)

# Loading word2vec model used for generating embeddings of tokens in sentence
import gensim.downloader as api
model = api.load('glove-twitter-50')

# Wrapper function for WMD computation
def find_wmd(sentence_1, sentence_2):
    sentence_1 = preprocess(sentence_1)
    sentence_2 = preprocess(sentence_2)
    distance = model.wmdistance(sentence_1, sentence_2)
    return distance

print("Sample sentence WMD distances: ", find_wmd(sentence_obama, sentence_president))

import csv
rows = []
with open(prediction_csv_path, 'r') as f1, open(target_file_path, "w") as f2:
    csvreader = csv.reader(f1)
    header = next(csvreader)
    f2.write("{}\t{}\t{}\t{}\t{}\n".format(header[0], header[8], "distance_gpt3", header[11], "distance_cocon_model"))
    for line in csvreader:
        rows.append(line)
        # line = line.split(',')
        input_sentence = line[0]
        ground_truth = line[1]
        gpt_model_1 = line[6]
        cocon_model_1 = line[9]
        gpt_model_2 = line[7]
        cocon_model_2 = line[10]
        gpt_model_3 = line[8]
        cocon_model_3 = line[11]

        dist_gpt_model_1 = find_wmd(ground_truth, gpt_model_3)
        dist_cocon_model_1 = find_wmd(ground_truth, cocon_model_3)
        
        f2.write("{}\t{}\t{}\t{}\t{}\n".format(ground_truth, gpt_model_3, dist_gpt_model_1, cocon_model_3, dist_cocon_model_1))
