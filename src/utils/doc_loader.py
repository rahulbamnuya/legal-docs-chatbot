def load_document(text: str) -> dict:
    """
    Load and validate document text
    """
    if not text or not text.strip():
        raise ValueError("Document text cannot be empty")

    return {
        "content": text.strip(),
        "length": len(text.strip())
    }
