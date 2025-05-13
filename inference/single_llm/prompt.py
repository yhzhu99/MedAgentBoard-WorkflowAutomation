prompt_format = """
    You have been given a task and a dataset, and you need to write a code to solve the given task.
    
    The columns names of the dataset are as follows:
    {colnames}
    
    The task is as follows:
    {task}
    
    You need to provide the response strictly according to the following requirements:
    
    1. Only return the code itself, without any explanation or comments;
    2. Use Python syntax;
    3. Ensure that the code can run directly.
    4. Assume the path of the dataset is "{dataset_path}". 
    5. The code needs to save the running results to "{save_path}".
"""

system_prompt_format = """
    You are a helpful assistant.
"""