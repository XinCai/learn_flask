from flask import Flask, jsonify, render_template

from h2ogpte import H2OGPTE
import json

client = H2OGPTE(
    address='https://h2ogpte.genai.h2o.ai',
    api_key='sk-n0XL8rWyslMqkOlIDFYlMBG88pCm8qvgJSeQY7riFJNNR0B7',
)

# Chat with LLM
chat_session_id = client.create_chat_session_on_default_collection()
with client.connect(chat_session_id) as session:
    # Simple Question for Document Collection
    answer = session.query(
        "tell me about Choy Lee Fut in chinese",
    ).content
    # Convert answer to JSON object
    answer_json = json.dumps(answer)

    # Print the JSON object
    print(answer_json)


# # Create Collection
# collection_id = client.create_collection(
#     name="My first h2oGPTe collection",
#     description="PDF -> text -> summary",
# )

# file_path = "...path to document(s)..."
# with open(file_path.resolve(), "rb") as f:
#     upload_id = client.upload(file_path.name, f)

# # Converting the input into chunked text and embeddings...
# client.ingest_uploads(collection_id, [upload_id])

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
    return render_template('home.html', jobs=objects, answer=answer_json)


@app.route('/jobs')
def get_jobs():
    return jsonify(objects)


if __name__ == '__main__':
    app.run(debug=True)
