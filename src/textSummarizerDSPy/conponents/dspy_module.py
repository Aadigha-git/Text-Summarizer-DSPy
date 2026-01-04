import dspy

class GenerateSummary(dspy.Signature):
    """
    You are an expert summarization system.

    Produce a faithful, concise summary that:
    - Preserves key facts and decisions
    - Avoids hallucinations or new information
    - Uses clear, neutral language
    - Is appropriate for the specified audience and format

    Do NOT copy sentences verbatim unless necessary.
    """

    # Inputs
    article = dspy.InputField(
        desc="The full dialogue, article, or transcript to be summarized"
    )

    audience = dspy.InputField(
        desc="Target audience (e.g., general, executive, technical, student)",
        default="technical"
    )

    max_words = dspy.InputField(
        desc="Maximum number of words for the summary",
        default=120
    )

    # Outputs (structured, not just one blob of text)
    summary = dspy.OutputField(
        desc="The final concise summary, within the word limit"
    )

    key_points = dspy.OutputField(
        desc="3–5 bullet-point highlights capturing the most important information"
    )

    confidence = dspy.OutputField(
        desc="A number from 0 to 1 indicating confidence that the summary is faithful to the source"
    )
