def build_context(chunks):

    context = ""

    for chunk in chunks:

        context += chunk.page_content

        context += "\n\n"

    return context