from flask import Flask
from pathlib import Path

root_path = Path(__file__).parent.parent
template_path = root_path / 'resources/templates'
static_dir = root_path / 'resources/static'

app=Flask(__name__, template_folder=template_path,
          static_folder=static_dir, static_url_path='/static')