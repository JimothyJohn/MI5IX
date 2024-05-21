from typing import Optional

class Prompt:
    def __init__(
        self,
        name: str,
        profile: str,
        constraints: Optional[list] = [],
        instructions: Optional[list] = [],
        objective: Optional[str] = "",
        examples: Optional[list] = [],
    ) -> None:
        self.name = name
        self.profile = profile
        self.constraints = constraints
        self.instructions = instructions
        self.objective = objective
        self.examples = examples

    def __call__(self) -> str:
        return f"""
        {self.profile}
        {" ".join([constraint for constraint in self.constraints])}
        {" ".join([instruction for instruction in self.instructions])}
        {self.objective}
    """
