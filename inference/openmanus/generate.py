import asyncio

from app.agent.manus import Manus
from app.logger import logger


import json
import os
# from prompt import prompt_format
from tqdm import tqdm

prompt_format = """
    Analyze the document in '{dataset_path}', solve the following task: 
    
    {task}
    
    Save the results in the folder '{output_dir}' 
"""


async def main(prompt):
    agent = Manus()
    try:
        logger.warning("Processing your request...")
        await agent.run(prompt)
        logger.info("Request processing completed.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")
    finally:
        # Ensure agent resources are cleaned up before exiting
        await agent.cleanup()
    

def generate(prompt):
    asyncio.run(main(prompt))
    
    return None

def get_config(task):
    task_content = task['task']
    if task['dataset'] == 'tjh':
        dataset_path = "tjh_dataset_formatted.csv"
    elif task['dataset'] == 'mimic':
        dataset_path = "mimic-iv-timeseries-note.parquet"
    
    output_dir = 'output/' + str(task['number']) + '/'
    os.makedirs(output_dir, exist_ok=True)   
     
    return {'task': task_content, 'output_dir': output_dir ,'dataset_path': dataset_path}

if __name__ == "__main__":
    with open('task100.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)

    for (i, task) in tqdm(enumerate(tasks)):
        try:
            config = get_config(task)
            
            prompt = prompt_format.format(**config)
            
            ret = generate(prompt = prompt)
            
        except Exception as e:
            pass
        


    
    
    