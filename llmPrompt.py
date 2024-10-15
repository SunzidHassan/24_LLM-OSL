def llmPrompt(delimiter, chemical, chmThr):

    task = f"""
    Select the best action for a mobile robot to move towards an odor/plume/vapor emiting object.
    You will select the action by analyzing given robot egocentric visual frame and odor concentration data.
    You will be given:
    - A list of actions to select from
    - Hints to select the actions
    - Instructions of how to respond to user.
    All of these inputs are delimited by {delimiter}.
    """

    actionInstructions = """
    Action 1: Move forward. (Action_id = 1).
    Action 2: Move right. (Action_id = 2).
    Action 3: Move left. (Action_id = 3).
    Action 4: Follow high odor. (Action_id = 4).
    Action 5: Find odor emiting object. (Action_id = 5).
    """

    hints = """
    Hint 1: If there is an odor/plume/vapor emiting object in the image, select actions from (1-3) to approach the object. If the odor/plume/vapor emiting object is in the center of the image, select Move forward (Action_id = 1); if it's in the right half of the image, select Move right (Action_id = 2); if it's in the left half of the image, select Move left (Action_id = 3).
    Hint 2: If there is no odor/plume/vapor emiting object in the image, then check the 'odor_concentration' and 'odor_concentration_threshold' values. If the 'odor_concentration' value is greater than the 'odor_concentration_threshold' value, then select action `Follow high odor` (Action_id = 4). Otherwise, select action 'Find odor emiting object' (Action_id = 5)."""


    # output with reasoning
    reasoningOutputInstructions = f"""
    Your response should use the following format:
    <reasoning>
    <reasoning>
    <repeat until you have a decision>
    Selected Action:{delimiter} <only output one `Action_id` as a int number>
    Make sure to include {delimiter} to separate every step."""

    # or output without reasoning
    behaviorOutputInstructions = f"""
    Response to user:{delimiter} <Respond with the corresponding numerical value of the `Action_id` (1, 2, 3, 4, or 5) without any additional text or punctuation.>
    """

    robotPrompt_hints1_reasoning1 = f"""
    {delimiter} Task:
    {task}
    {delimiter} Available Actions:
    {actionInstructions}
    {delimiter} Hints:
    {hints}
    {delimiter} Output Instructions:
    {reasoningOutputInstructions}
    {delimiter} "odor_concentration" Value:
    {chemical}
    {delimiter} "odor_concentration_threshold" Value:
    {chmThr}
    """

    return robotPrompt_hints1_reasoning1