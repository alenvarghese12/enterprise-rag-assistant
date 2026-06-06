from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(docs, pdf=None):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    # Add pdf filename as metadata if provided
    if pdf:
        for chunk in chunks:
            chunk.metadata["source_pdf"] = pdf

    return chunks