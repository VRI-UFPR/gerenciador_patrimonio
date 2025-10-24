# This file is part of the Gerenciador Patrimonio
# Copyright (c) 2025 VRI
# 
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# =============================================================================
#  Header
# =============================================================================

import jinja2
from flask import Flask, request
from flask_cors import CORS

g_app = Flask(__name__)
g_cors = CORS(g_app)

g_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./templates'),
    autoescape=True  # Ativa escape automático para segurança
)

# =============================================================================
#  Paginas HTML
# =============================================================================

@g_app.route('/', methods=["GET"])
def get_index():
    '''
        Descricao da funcao
    '''
    global g_env

    # renderiza o template mapa com os dados
    template = g_env.get_template('index.html')
    return template.render()

# =============================================================================
#  Main
# =============================================================================

if __name__ == '__main__':
    g_app.run(debug=True)