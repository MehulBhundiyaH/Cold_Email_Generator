import chromadb
client = chromadb.Client()
collection = client.create_collection(name="my_collection")
collection.add(
    documents=[
        "This is the document of Mehul",
        "This document is of queen"
    ],
    ids=['id1', 'id2']
)
print("Documents added successfully!")

all_docs = collection.get()
print(all_docs)

# documents = collection.get(ids=["id1"])
# print(documents)

results = collection.query(
    query_texts=['Query is about a boy'],
    n_results=2
)
print(results)