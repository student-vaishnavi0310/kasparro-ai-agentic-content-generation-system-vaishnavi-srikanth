class BaseAgent:
    """
    Base class for all agents in the system.
    Defines a common agent contract.
    """

    def __init__(self, name: str):
        self.name = name

    def run(self, task: dict):
        """
        Every agent must implement this method.
        Agents respond only to tasks.
        """
        raise NotImplementedError(
            f"Agent '{self.name}' must implement run(task)"
        )
