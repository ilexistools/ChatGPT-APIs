from openai import OpenAI
import os 
from scipy.spatial.distance import cosine

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"),)

# define uma função para comparar embeddings
def compare_embeddings(embedding1, embedding2):
    return 1 - cosine(embedding1, embedding2)

# define uma função para criar embeddings 
def get_embedding(sent):
    stoplist = ['o', 'da', 'a', 'do', 'de', 'uma','e']
    tokens = [token for token in sent.lower().split(' ') if token not in stoplist]
    response = client.embeddings.create(input=tokens, model="text-embedding-ada-002")
    return response.data[0].embedding

# exemplos de frases para teste
sent1 = "O céu nublado indica a chance de mudança de temperatura e chuva"
sent2 = "O sabor do frango assado mineiro é uma delícia"
sent3 = "O céu nublado indica a possibilidade de mudança de temperatura e chuva"
sent4 = "O sabor do frango assado da minha avó é uma delícia"

# cria embeddings para cada frase
embeddings = {
    "sent1": get_embedding(sent1),
    "sent2": get_embedding(sent2),
    "sent3": get_embedding(sent3),
    "sent4": get_embedding(sent4)
}

# calcula a similaridade entre as frases
similarity_sent_1_3 = compare_embeddings(embeddings["sent1"], embeddings["sent3"])
similarity_sent_2_4= compare_embeddings(embeddings["sent2"], embeddings["sent4"])
similarity_sent_3_4 = compare_embeddings(embeddings["sent3"], embeddings["sent4"])

# imprime o resultado
print('A similaridade 1 e 3: %s' % (similarity_sent_1_3))
print('A similaridade 2 e 4: %s' % (similarity_sent_2_4))
print('A similaridade 3 e 4: %s' % (similarity_sent_3_4))
