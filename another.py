# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd 

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create a plot
# plt.plot(x, y)


# plt.plot(x, y, label="Line")
# plt.legend()


# # Show the plot
# sizes = [15, 30, 45, 10]
# labels = ['A', 'B', 'C', 'D']

# plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.title("Pie Chart")
# plt.show()



# data = np.random.randn(1000)  # Generate random data
# plt.hist(data, bins=10, color='red')
# plt.title("Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }

# df = pd.DataFrame(data)
# print(df)


# data = [['Alice', 25, 'New York'], ['Bob', 30, 'Los Angeles'], ['Charlie', 35, 'Chicago']]
# columns = ['Name', 'Age', 'City']

# df = pd.DataFrame(data, columns=columns)
# print(df)

# df['Age'].plot(kind='hist')
# plt.show()

from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# Load the pre-trained RAG tokenizer, retriever, and generator
tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", tokenizer=tokenizer)
model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq")

# Encode the input query
input_query = "Who is the president of the United States?"
input_ids = tokenizer(input_query, return_tensors="pt").input_ids

# Use the retriever to get relevant documents
retrieved_docs = retriever(input_ids)

# Generate a response based on the retrieved documents
outputs = model.generate(input_ids, context_input_ids=retrieved_docs["context_input_ids"], context_attention_mask=retrieved_docs["context_attention_mask"])

# Decode and print the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
