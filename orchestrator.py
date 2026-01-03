class Orchestrator:
    """
    Central orchestrator responsible for coordinating
    task-based execution of autonomous agents.
    """

    def __init__(self):
        self.context = {}

    def dispatch(self, agent, task: dict):
        """
        Sends a task to an agent and stores the result.
        """
        result = agent.run(task)
        return result
