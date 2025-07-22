from deepeval.synthesizer import Synthesizer
from deepeval.synthesizer.config import ContextConstructionConfig
from typing import List, Optional, Any


def generate_goldens_from_documents(
        document_paths: str,
        model: Any,
        embedder: Optional[Any] = None,
        chunk_size: int = 100,
        chunk_overlap: int = 10, ):
    synthesizer = Synthesizer(model=model)

    goldens = synthesizer.generate_goldens_from_docs(
        document_paths=[document_paths],
        context_construction_config=ContextConstructionConfig(embedder=embedder,
                                                              critic_model=model,
                                                              chunk_size=chunk_size,
                                                              chunk_overlap=chunk_overlap)
    )
    return goldens
