import json
from tqdm import tqdm
import os

from openai import OpenAI

from prompt import system_prompt_format, prompt_format

client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key="YOUR_API_KEY",
)

def generate(prompt, system_prompt):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
        )
        result = response.choices[0].message.content
        # 清理代码格式（去除可能的代码块标记）
        code = result.replace("```python", "").replace("```", "").strip()
        return {"code": code, "error": None}
    except Exception as e:
        return {"code": None, "error": str(e)}
  
def get_config(task):
    task_content = task['task']
    if task['dataset'] == 'tjh':
        dataset_path = "tjh_dataset_formatted.csv"
        colnames = "['PatientID', 'RecordTime', 'AdmissionTime', 'DischargeTime', 'Outcome', 'LOS', 'Sex', 'Age', 'Hypersensitive cardiac troponinI', 'hemoglobin', 'Serum chloride', 'Prothrombin time', 'procalcitonin', 'eosinophils(%)', 'Interleukin 2 receptor', 'Alkaline phosphatase', 'albumin', 'basophil(%)', 'Interleukin 10', 'Total bilirubin', 'Platelet count', 'monocytes(%)', 'antithrombin', 'Interleukin 8', 'indirect bilirubin', 'Red blood cell distribution width ', 'neutrophils(%)', 'total protein', 'Quantification of Treponema pallidum antibodies', 'Prothrombin activity', 'HBsAg', 'mean corpuscular volume', 'hematocrit', 'White blood cell count', 'Tumor necrosis factorα', 'mean corpuscular hemoglobin concentration', 'fibrinogen', 'Interleukin 1β', 'Urea', 'lymphocyte count', 'PH value', 'Red blood cell count', 'Eosinophil count', 'Corrected calcium', 'Serum potassium', 'glucose', 'neutrophils count', 'Direct bilirubin', 'Mean platelet volume', 'ferritin', 'RBC distribution width SD', 'Thrombin time', '(%)lymphocyte', 'HCV antibody quantification', 'D-D dimer', 'Total cholesterol', 'aspartate aminotransferase', 'Uric acid', 'HCO3-', 'calcium', 'Amino-terminal brain natriuretic peptide precursor(NT-proBNP)', 'Lactate dehydrogenase', 'platelet large cell ratio ', 'Interleukin 6', 'Fibrin degradation products', 'monocytes count', 'PLT distribution width', 'globulin', 'γ-glutamyl transpeptidase', 'International standard ratio', 'basophil count(#)', 'mean corpuscular hemoglobin ', 'Activation of partial thromboplastin time', 'Hypersensitive c-reactive protein', 'HIV antibody quantification', 'serum sodium', 'thrombocytocrit', 'ESR', 'glutamic-pyruvic transaminase', 'eGFR', 'creatinine']"
    elif task['dataset'] == 'mimic':
        dataset_path = "mimic-iv-timeseries-note.parquet"
        colnames = "['RecordID', 'PatientID', 'RecordTime', 'AdmissionID', 'Outcome', 'LOS', 'Readmission', 'Text', 'Age', 'Sex', 'Capillary refill rate', 'Diastolic blood pressure', 'Fraction inspired oxygen', 'Glascow coma scale eye opening', 'Glascow coma scale motor response', 'Glascow coma scale total', 'Glascow coma scale verbal response', 'Glucose', 'Heart Rate', 'Height', 'Mean blood pressure', 'Oxygen saturation', 'Respiratory rate', 'Systolic blood pressure', 'Temperature', 'Weight', 'pH']"
    save_path = "/home/kisara/RESEARCH/MedAgentBoard/MedAgentBoard/single_llm_2/output/{}/".format(str(task['number']))
    os.makedirs(save_path, exist_ok=True)
    
    return {'task': task_content, 'colnames': colnames ,'dataset_path': dataset_path, 'save_path': save_path}

with open('task100.json', 'r', encoding='utf-8') as f:
    tasks = json.load(f)

code_list = []
for (i, task) in tqdm(enumerate(tasks)):
    
    config = get_config(task)
    
    prompt = prompt_format.format(**config)
    
    ret = generate(prompt = prompt, system_prompt=system_prompt_format)
    
    code_list.append({
        "task": task['task'],
        "task_type": task['task_type'],
        "dataset": task['dataset'],
        "metadata": task['metadata'],
        "ID": task['ID'],
        
        "code": ret['code'],
        "error": ret['error']
    })
    
    with open('code.json', 'w', encoding='utf-8') as f:
        json.dump(code_list, f, ensure_ascii=False, indent=4)
    
    
    