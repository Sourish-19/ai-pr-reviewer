# section 3: analyzer.py
# Person 3 can explain this section

import re
from typing import Dict

class ReviewAnalyzer:
    def __init__(self):
        """
        Initializes the analyzer responsible for structuring the AI output.
        """
        pass

    def parse_ai_response(self, raw_text: str) -> Dict[str, str]:
        """
        Takes the unstructured string response from the AI and chunks it 
        into our 3 agreed-upon categories.
        """
        # A simple parser identifying the sections based on the prompt instructions.
        parsed_data = {
            "Code Quality": "No report.",
            "Security": "No report.",
            "Codebase Integration": "No report.",
            "Raw": raw_text # Store the raw text just in case parsing fails
        }
        
        # We try to extract content between the headers using Regex or basic string splitting.
        # This regex looks for [Category]: followed by whatever content until the next category or EOF.
        quality_match = re.search(r"\[Code Quality\]:?(.*?)(?=\[Security\]|\[Codebase Integration\]|\Z)", raw_text, re.DOTALL | re.IGNORECASE)
        security_match = re.search(r"\[Security\]:?(.*?)(?=\[Code Quality\]|\[Codebase Integration\]|\Z)", raw_text, re.DOTALL | re.IGNORECASE)
        integration_match = re.search(r"\[Codebase Integration\]:?(.*?)(?=\[Code Quality\]|\[Security\]|\Z)", raw_text, re.DOTALL | re.IGNORECASE)

        if quality_match:
            parsed_data["Code Quality"] = quality_match.group(1).strip()
        if security_match:
            parsed_data["Security"] = security_match.group(1).strip()
        if integration_match:
            parsed_data["Codebase Integration"] = integration_match.group(1).strip()

        return parsed_data
