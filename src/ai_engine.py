# section 2: ai_engine.py
# Person 2 can explain this section

import os
from typing import Optional

try:
    from google import genai
except ImportError:
    genai = None

class AIEngine:
    def __init__(self, api_key: Optional[str] = None):
        """
        Initializes the AI connection using Gemini.
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is missing. Please set it as an environment variable.")
        
        if genai is None:
            raise ImportError("google-genai package is not installed. Run: pip install google-genai")

        self.client = genai.Client(api_key=self.api_key)
        self.model_name = "gemini-2.5-flash"  # Using efficient flash model

    def generate_review(self, diff_text: str) -> str:
        """
        Constructs the prompt and sends the diff to Gemini for review.
        """
        system_instruction = (
            "You are an expert Principal Software Engineer acting as a rigorous PR reviewer. "
            "You are reviewing the provided git diff. "
            "You MUST categorize your feedback into 3 exact sections: "
            "\n1. [Code Quality]: Readability, maintainability, syntax.\n"
            "\n2. [Security]: Vulnerabilities, poor practices, edge case handling.\n"
            "\n3. [Codebase Integration]: Architectural fit, impact on existing code.\n"
            "If a section has no issues, simply say 'No major issues found.'\n"
            "Provide insightful, concise, and actionable bullet points."
        )

        prompt = f"Please review the following Pull Request diff:\n\n```diff\n{diff_text}\n```"

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.4,
            ),
        )
        
        if not response.text:
            raise Exception("AI model returned an empty empty response.")
            
        return response.text
