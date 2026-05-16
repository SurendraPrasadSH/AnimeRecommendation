import pandas as pd
import html
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def _build_model():
    df = pd.read_csv('./anime.csv')

    df['name'] = df['name'].str.lower().apply(html.unescape)
    df['genre'] = df['genre'].str.lower()
    df['episodes'] = pd.to_numeric(df['episodes'], errors='coerce')
    df['type'] = df['type'].map({
        'TV': 'series', 'OVA': 'series', 'Special': 'series',
        'ONA': 'series', 'Music': 'series', 'Movie': 'movie'
    })

    def eps_tag(row):
        if row['episodes'] == 1:    return 'movie'
        elif row['episodes'] <= 13: return 'short_series'
        elif row['episodes'] <= 26: return 'medium_series'
        else:                       return 'long_series'

    df['eps_tag'] = df.apply(eps_tag, axis=1)

    # Genre repeated 3x so TF-IDF weights it higher than episode tag
    genre_clean = df['genre'].str.replace(',', ' ')
    df['tfidf_input'] = genre_clean + ' ' + genre_clean + ' ' + genre_clean + ' ' + df['eps_tag']

    # Clean AFTER all features are built
    df = df.drop_duplicates(subset='name', keep='first')
    df = df.dropna(subset=['tfidf_input', 'name', 'genre', 'rating'])
    df = df.reset_index(drop=True)

    tf = TfidfVectorizer()
    tfidf_matrix = tf.fit_transform(df['tfidf_input'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    name_to_idx = pd.Series(df.index, index=df['name'])

    return df, tf, tfidf_matrix, cosine_sim, name_to_idx

# Built once at import time
df, tf, tfidf_matrix, cosine_sim, name_to_idx = _build_model()

def get_recommendations(query: str) -> list:
    query = query.lower().strip()
    try:
        if query in name_to_idx:
            idx = name_to_idx[query]
            if isinstance(idx, pd.Series):
                idx = idx.iloc[0]
            scores = list(enumerate(cosine_sim[idx]))
        else:
            query_vec = tf.transform([query])
            scores = list(enumerate(cosine_similarity(query_vec, tfidf_matrix)[0]))

        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        top5 = scores[1:6]
        results = []
        for i, score in top5:
            results.append({
                "name":   df.iloc[i]["name"],
                "genre":  df.iloc[i]["genre"],
                "rating": round(float(df.iloc[i]["rating"]), 2),
                "type":   df.iloc[i]["type"]
            })
        return results
    except Exception:
        return []