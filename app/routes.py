from flask import Blueprint, render_template, abort
import markdown
import os
from pathlib import Path

main_bp = Blueprint('main', __name__)

# Obtener la ruta base de documentación
DOCS_PATH = Path(__file__).parent.parent / 'docs'
WIKI_PATH = Path(__file__).parent.parent / 'wiki'

def get_markdown_content(file_path):
    """Lee y convierte un archivo Markdown a HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return markdown.markdown(content)
    except FileNotFoundError:
        return None

@main_bp.route('/')
def index():
    """Página principal de la wiki"""
    wiki_home = WIKI_PATH / 'Home.md'
    content = get_markdown_content(wiki_home)
    return render_template('index.html', content=content, title='Inicio')

@main_bp.route('/procedimientos')
def procedimientos():
    """Sección de procedimientos de red"""
    proc_file = DOCS_PATH / 'procedimientos_red' / 'README.md'
    content = get_markdown_content(proc_file)
    if content is None:
        abort(404)
    return render_template('section.html', content=content, title='Procedimientos de Red')

@main_bp.route('/scripts')
def scripts():
    """Sección de scripts"""
    scripts_file = DOCS_PATH / 'scripts' / 'README.md'
    content = get_markdown_content(scripts_file)
    if content is None:
        abort(404)
    return render_template('section.html', content=content, title='Scripts')

@main_bp.route('/troubleshooting')
def troubleshooting():
    """Sección de troubleshooting"""
    trouble_file = DOCS_PATH / 'troubleshooting' / 'README.md'
    content = get_markdown_content(trouble_file)
    if content is None:
        abort(404)
    return render_template('section.html', content=content, title='Troubleshooting')

@main_bp.errorhandler(404)
def not_found(error):
    """Manejo de errores 404"""
    return render_template('404.html'), 404
