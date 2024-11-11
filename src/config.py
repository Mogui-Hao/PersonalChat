
import os
import json
from libraries.api.utils.LanguageFile import LanguageFile

Language: dict[str, LanguageFile] = {}
resourceFolder = "src/resource/language"
root = os.getcwd()
for item in [file for file in os.listdir(resourceFolder) if file.endswith('.json')][::-1]:
    with open(os.path.join(root, resourceFolder, item), encoding="utf-8") as f:
        Language[item.split(".")[0]] = LanguageFile(os.path.join(resourceFolder, item))

LanguageValues = list(Language.values())
CurrentLanguage: LanguageFile = LanguageValues[0]
ConfigPath = "src/config.json"
Config = {
    "style": {"theme": "auto", "language": "zh-cn"},
}

