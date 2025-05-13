import pandas as pd
import numpy as np
from tqdm import tqdm
import json
import re
import os
import time

from openai import OpenAI
import google.generativeai as genai

from prompt import *

DATASET = 'TJH'

def get_sample_str_tjh(df):
    """
    修改例子的获取方法：随机取3个PatientID
    """
    patients = df['PatientID'].unique()
    random_patients = np.random.choice(patients, size=3, replace=False).tolist()    # 随机选取3个PatientID
    
    example_list = []
    
    for target_id in random_patients:
        example_list.append(df[df['PatientID'] == target_id].values.tolist())   
    
    lines = []
    for example_data in example_list:
        lines.extend(example_data)
    
    colnames = df.columns.tolist()
    ret = ""
    for line in lines:   # 将每一行的数据转化为str
        line_str = ""
        for (n, d) in zip(colnames, line):
            if not bool(re.search(r'\d', d)):   # 删除缺失值（通过判断是否包含数字实现）  # tjh
                continue  
            line_str += "{}:{}, ".format(n, d)
        line_str = '[' + line_str + '],\n'
        ret += line_str
    
    ret = '[' + ret + ']'
    
    return ret

def get_sample_str_mimic(df):
    """
    随机取3个PatientID
    """
    patients = df['PatientID'].unique()
    random_patients = np.random.choice(patients, size=3, replace=False).tolist()    # 随机选取3个PatientID
    
    example_list = []
    
    for target_id in random_patients:
        example_list.append(df[df['PatientID'] == target_id].values.tolist())   # 
    
    lines = []
    for example_data in example_list:
        lines.extend(example_data)
    
    colnames = df.columns.tolist()
    ret = ""
    for line in lines:   # 将每一行的数据转化为str
        line_str = ""
        for (n, d) in zip(colnames, line):
            if n == 'Text':   # 删除Text列，防止过长
                continue 
            line_str += "{}:{}, ".format(n, d)
        line_str = '[' + line_str + '],\n'
        ret += line_str
    
    ret = '[' + ret + ']'
    
    return ret

def csv_to_prompt(df):
    """
    Reads a CSV file and converts it to a prompt format.
    """
    if DATASET == 'TJH':
        data_samples = get_sample_str_tjh(df) # tjh
    else:
        data_samples = get_sample_str_mimic(df)
    
    # prompt = prompt_format_data_wrangling.format(data_examples = data_samples)
    # prompt = prompt_format_data_querying.format(data_examples = data_samples)
    # prompt = prompt_format_data_statistics.format(data_examples = data_samples)
    # prompt = prompt_format_data_preprocessing.format(data_examples = data_samples)
    
    # prompt = prompt_format_modeling.format(data_examples = data_samples)
    # prompt = prompt_format_modeling_with_answer.format(data_examples = data_samples)
    
    # prompt = prompt_format_plotting_or_visualization_FROM_DATA.format(data_examples = data_samples)
    # prompt = prompt_format_plotting_or_visualization_MODEL_ANALYSIS.format(data_examples = data_samples)
    
    prompt = prompt_format_report.format(data_examples = data_samples)
    
    return prompt

    
def generate_question_gemini(prompt, system_prompt=None):
    
    model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')
    
    genai.configure(api_key="YOUR_API_KEY", transport="rest")
    response = model.generate_content(prompt)

    return response.text
    

if __name__ == "__main__":
    
    data_list = []
    
    # 加载数据
    if DATASET == 'TJH':
        dataframe = pd.read_csv('tjh_dataset_formatted.csv', keep_default_na=False, dtype = str)  
    else:
        dataframe = pd.read_parquet("mimic-iv-timeseries-note.parquet")  # mimic
    
    for i in tqdm(range(25)):
        try:
            # 生成prompt，随机从数据中取值  
            pt = csv_to_prompt(dataframe)
            
            # 排除生成过的任务
            pt += "\n\n    The task is not allowed to be similar in content or syntax to any of the following tasks:\n{exclusion}".format(exclusion = str([b['task'] for b in data_list]))    
            sys_pt = system_prompt
            
            block = generate_question_gemini(pt, sys_pt)    # 使用gemeni2.5 pro
            
            # 将str解析为json
            try:
                # 提取原始字符串中的JSON部分
                original_str = block
                start = original_str.find('{')
                end = original_str.rfind('}') + 1
                json_str = original_str[start:end]
                # 解析为JSON对象
                parsed_data = json.loads(json_str)
                data_list.append(parsed_data)
            except Exception as e:
                print('Error when parsing JSON:', e)
                # data_list.append(block)
                pass
            
        except Exception as e:
            print('Error when generating question:', e)
            pass
        
        # 将结果保存到JSON文件
        pth = 'output.json'
        with open(pth, 'w') as f:
            json.dump(data_list, f, indent=4, ensure_ascii=False)
        f.close()
        
        
