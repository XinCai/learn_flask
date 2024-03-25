from flask import Flask, render_template

from h2ogpte import H2OGPTE

client = H2OGPTE(
    address='https://h2ogpte.internal-genai.dedicated.h2o.ai',
    api_key='sk-n0XL8rWyslMqkOlIDFYlMBG88pCm8qvgJSeQY7riFJNNR0B7',
)

# Create a new collection
collection_id = client.create_collection(
    name='Contracts',
    description='Paper clip supply contracts',
)

# Create documents
# Note: Done for demonstration purposes only (not usually needed)
with open('dunder_mifflin.txt', 'w') as f:
    f.write('There were 55 paper clips shipped, '
            '22 to Scranton and 33 to Filmer.')
    
with open('initech.txt', 'w') as f:
    f.write('David Brent did not sign any contract with Initech.')
    
# Upload documents
# Many file types are supported: text/image/audio documents and archives
with open('dunder_mifflin.txt', 'rb') as f:
    dunder_mifflin = client.upload('Dunder Mifflin.txt', f)
    
with open('initech.txt', 'rb') as f:
    initech = client.upload('IniTech.txt', f)

# Ingest documents (Creates previews, chunks and embeddings)
client.ingest_uploads(collection_id, [dunder_mifflin, initech])

# Create a chat session
chat_session_id = client.create_chat_session(collection_id)

# Query the collection
with client.connect(chat_session_id) as session:
    reply = session.query(
        'How many paper clips were shipped to Scranton?',
        timeout=60,
    )
    print(reply.content)

    reply = session.query(
        'Did David Brent co-sign the contract with Initech?',
        timeout=60,
    )
    print(reply.content)

# Summarize each document
documents = client.list_documents_in_collection(
    collection_id, offset=0, limit=99
)
for doc in documents:
    summary = client.summarize_document(
        document_id=doc.id,
        timeout=60,
    )
    print(summary.content)


app = Flask(__name__)


objects = [
    {'id': 1,
     'title': 'Software Engineer',
     'location': 'San Francisco',
     'salary': 100000
     },
    {'id': 2,
     'title': 'Data Analyst',
     'location': 'New York',
     'salary': 90000
     },
    {'id': 3,
     'title': 'Product Manager',
     'location': 'Seattle',
     'salary': 110000
     }
]


# Add an additional blank line here
@app.route('/')
def hello():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
