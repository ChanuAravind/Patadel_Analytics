from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import string
import zipfile
from spacy.lang.en.stop_words import STOP_WORDS

app = Flask(__name__)

with zipfile.ZipFile('cleaned_df.zip', 'r') as z:
    with z.open('cleaned_df.csv') as f:
        cleaned_df = pd.read_csv(f)

df = pd.DataFrame(columns=['patent_number', 'title', 'abstract', 'claims', 'description'])
df['patent_number'] = cleaned_df.patent_number
df['title'] = cleaned_df.english_titles
df['abstract'] = cleaned_df.modified_abstract
df['claims'] = cleaned_df.english_claims
df['description'] = cleaned_df.english_description
df['family_members'] = cleaned_df.english_family_members

nlp = spacy.load('en_core_web_sm', disable=["tagger", "ner"])
nlp.add_pipe('sentencizer')

def pre_processor(sentence):
    mytokens = sentence.split(' ')
    mytokens = [word.lower() for word in mytokens if word not in STOP_WORDS and word not in string.punctuation]
    return mytokens

df["processed_abstract"] = df["abstract"].apply(pre_processor)
df["processed_claims"] = df["claims"].apply(pre_processor)
df["processed_description"] = df["description"].apply(pre_processor)
df['family_members'] = df['family_members'].apply(pre_processor)

df['processed_text'] = df['processed_abstract'] + df['processed_claims'] + df['processed_description'] + df[
    'family_members']
documents = [' '.join(tokens) for tokens in df["processed_text"]]

# vectorizer = TfidfVectorizer(min_df=0.01, max_df=0.95, ngram_range=(1, 2))
vectorizer = TfidfVectorizer()
text_tfidf_matrix = vectorizer.fit_transform(documents)

@app.route('/search', methods=['GET'])
def search():
    user_query = request.args.get('query', '')

    query_tokens = pre_processor(user_query)
    query = ' '.join(query_tokens)
    query_vector = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vector, text_tfidf_matrix).flatten()
    results = list(zip(df['patent_number'], df['title'], cosine_similarities))
    results.sort(key=lambda x: x[2], reverse=True)
    # top_results = results[:10]
    top_results = [(x[0], x[1]) for x in results[:10]]
    return jsonify(top_results)

@app.route('/')
def home():
    welcome_message = 'Welcome to Patent Search!'
    search_link = 'Head to <a href="/search?query=microprocessor">Query URL</a>'

    return f'<h1>{welcome_message}</h1><p>{search_link}</p>'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
