import json
import yaml
import xmltodict
import os

def detect_format(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".json":
        return "json"
    if ext in [".yml", ".yaml"]:
        return "yaml"
    if ext == ".xml":
        return "xml"
    raise ValueError(f"Nieobsługiwany format pliku: {ext}")

def load_file(path):
    fmt = detect_format(path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            if fmt == "json":
                return json.load(f)
            if fmt == "yaml":
                return yaml.safe_load(f)
            if fmt == "xml":
                return xmltodict.parse(f.read())
    except Exception as e:
        raise ValueError(f"Błąd wczytywania pliku '{path}': {e}")

def save_file(path, data):
    fmt = detect_format(path)
    try:
        with open(path, "w", encoding="utf-8") as f:
            if fmt == "json":
                json.dump(data, f, indent=4, ensure_ascii=False)
            elif fmt == "yaml":
                yaml.dump(data, f, allow_unicode=True)
            elif fmt == "xml":
                xml_string = xmltodict.unparse(data, pretty=True)
                f.write(xml_string)
    except Exception as e:
        raise ValueError(f"Błąd zapisu pliku '{path}': {e}")