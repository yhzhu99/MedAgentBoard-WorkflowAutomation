system_prompt = """
    You are a data scientist.
"""

# 一、数据

# 数据整理
prompt_format_data_wrangling = """
    You have been given a CSV format dataset, and you need to provide a task based on the the dataset.
    
    The dataset examples are as follows:
    {data_examples}
    
    You need to provide the response strictly according to the following requirements:
    
    1. The task requires testing the ability of data wrangling;
    2. Please return your response in JSON format, similar to the following:
    {{
        'task': '...',
    }}
"""

# 数据查询
prompt_format_data_querying = """
    You have been given a CSV format dataset, and you need to provide a task based on the the dataset.
    
    The dataset examples are as follows:
    {data_examples}
    
    You need to provide the response strictly according to the following requirements:
    
    1. The task requires testing the ability of data querying;
    2. Please return your response in JSON format, similar to the following:
    {{
        'task': '...',
    }}
"""

# 数据统计
prompt_format_data_statistics = """
    You have been given a CSV format dataset, and you need to provide a task based on the the dataset.
    
    The dataset examples are as follows:
    {data_examples}
    
    You need to provide the response strictly according to the following requirements:
    
    1. The task requires testing the ability of data statistics;
    2. Please return your response in JSON format, similar to the following:
    {{
        'task': '...',
    }}
"""

# 数据预处理
prompt_format_data_preprocessing = """
    You have been given a CSV format dataset, and you need to provide a task based on the the dataset.
    
    The dataset examples are as follows:
    {data_examples}
    
    You need to provide the response strictly according to the following requirements:
    
    1. The task requires testing the ability of data preprocessing;
    2. Please return your response in JSON format, similar to the following:
    {{
        'task': '...',
    }}
"""

# 建模分析
prompt_format_modeling = """
    You have been given a CSV format dataset, and you need to provide a task based on the the dataset.
    
    The dataset examples are as follows:
    {data_examples}
    
    You need to provide the response strictly according to the following requirements:
    
    1. The task requires testing the ability of modeling;
    2. Please return your response in JSON format, similar to the following:
    {{
        'task': '...',
    }}
"""

# 画图分析
prompt_format_plotting_or_visualization_FROM_DATA = """
    You have been given a CSV format dataset, and you need to provide a task based on the the dataset.
    
    The dataset examples are as follows:
    {data_examples}
    
    You need to provide the response strictly according to the following requirements:
    
    1. The task requires testing the ability of plotting or visualization. The task requires presenting a modeling problem first, and then proposing a plotting or visualization problem based on it;
    2. Please return your response in JSON format, similar to the following:
    {{
        'task': '...',
    }}
"""

prompt_format_plotting_or_visualization_MODEL_ANALYSIS = """
    You have been given a CSV format dataset, and you need to provide a task based on the the dataset.
    
    The dataset examples are as follows:
    {data_examples}
    
    You need to provide the response strictly according to the following requirements:
    
    1. The task requires testing the ability of modeling and plotting and visualization. Propose a modeling problem and request plotting or visualization based on the running results, such as performance comparison or feature importance or other analysis;
    2. Please return your response in JSON format, similar to the following:
    {{
        'task': '...',
    }}
"""

# 生成报告
prompt_format_report = """
    You have been given a CSV format dataset, and you need to provide a task based on the the dataset.
    
    The dataset examples are as follows:
    {data_examples}
    
    You need to provide the response strictly according to the following requirements:
    
    1. The task requires testing the ability to generate report; the task is to investigate a valuable problem and request the generation of a corresponding report;
    2. Please return your response in JSON format, similar to the following:
    {{
        'task': '...',
    }}
"""
