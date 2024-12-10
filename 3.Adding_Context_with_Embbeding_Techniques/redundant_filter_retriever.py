from langchain.embeddings.base import Embeddings
from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import BaseRetriver


class RedundantFilterRetriver(BaseRetriver):
    embeddings: Embeddings
    chroma: Chroma

    def get_relevant_documents(self, query):
        # calculate embeddings for the 'query' string
        emb = self.embeddings.embed_query(query)


        # take embeddings and feed them into that
        # max_marginal_relevance_search_by_vector
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8     # -> Control the tolerance of a very, very similary docs
        )
    
    async def aget_relevant_documents(self):