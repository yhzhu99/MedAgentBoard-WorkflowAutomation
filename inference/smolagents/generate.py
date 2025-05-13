import json
import os
from prompt import prompt_format
from tqdm import tqdm

from smolagents import LiteLLMModel
import os
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

from smolagents.local_python_executor import BASE_PYTHON_TOOLS
BASE_PYTHON_TOOLS["open"] = open

model = LiteLLMModel(
    model_id="deepseek/deepseek-chat",
    temperature=0.0,
    api_key="YOUR_API_KEY",
)

def generate(prompt):
    
    agent = CodeAgent(tools=[], model=model, additional_authorized_imports=["*"])
    
    agent.run(prompt)
    
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

    code_list = []
    for (i, task) in tqdm(enumerate(tasks)):
        try:
            config = get_config(task)
            
            prompt = prompt_format.format(**config)
            
            ret = generate(prompt = prompt)
            
            
        except Exception as e:
            pass
        
        
    
