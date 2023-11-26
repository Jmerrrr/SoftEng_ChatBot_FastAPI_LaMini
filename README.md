# SoftEng_ChatBot_FastAPI_LaMini
In Vscode, open your terminal (CMD Terminal in vscode)

First Create a Virtual Environment:  
  &ensp; python -m Venv_Caps_ChatBot1_1_FastAPI_Lamini  
  &ensp; cd Venv_Caps_ChatBot1_1_FastAPI_Lamini/Scripts  
  &ensp; activate  
  &ensp; cd ..  
  &ensp; cd ..  
then run 'pip install requirements.txt' (Without the quotes)  
next clone the LLM Model:  
# Note 3GB file size, walang download bar na nakalagay, antayin nyo lang.  
  git lfs install  
  git clone https://huggingface.co/MBZUAI/LaMini-T5-738M  
Then run nyo to,  
  uvicorn testmain:app --reload  
may lalabas na ganito (Uvicorn running on http://127.0.0.1:8000)  
  ctrl + left-click nyo yung 'http://127.0.0.1:8000'  
P.S: d ko pa nilagay yung perps pdf kaya d pa sya makakasagot ng question about sa perps, basta. Pero try nyo mag prompt ng simple question about sa kung ano-ano.  
