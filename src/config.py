
import os
import json

Language: dict = {}
resourceFolder = "src/resource/language"
root = os.getcwd()
for item in [file for file in os.listdir(resourceFolder) if file.endswith('.json')][::-1]:
    with open(os.path.join(root, resourceFolder, item), encoding="utf-8") as f:
        Language[item.split(".")[0]] = json.loads(f.read())
LanguageValues = list(Language.values())
CurrentLanguage: dict = LanguageValues[0]
