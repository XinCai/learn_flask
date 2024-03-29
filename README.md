# Project Name

A brief description of your Flask project.

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Use Global API Keys](#use-global-api-keys)
  - [Usage](#usage)
  - [Features](#features)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.


## Use Global API Keys
```
from h2ogpte import H2OGPTE

client = H2OGPTE(
    address='https://h2ogpte.genai.h2o.ai',
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
    f.write('There were 55 paper clips shipped, 22 to Scranton and 33 to Filmer.')
    
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
documents = client.list_documents_in_collection(collection_id, offset=0, limit=99)
for doc in documents:
    summary = client.summarize_document(
        document_id=doc.id,
        timeout=60,
    )
    print(summary.content)
```

update package requirments file via command
```
pip freeze > requirements.txt 
```


## Usage

1. Set up the necessary environment variables.
2. Run the Flask application using `python app.py`.
3. Access the application in your browser at `http://localhost:5000`.

## Features

- Feature 1: Description of feature 1.
- Feature 2: Description of feature 2.
- ...

## Contributing

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).