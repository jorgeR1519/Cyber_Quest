"""Retira el generador anterior y conserva los conversores de documento reutilizables."""
import ast
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[1]
archivo = RAIZ/"herramientas"/"preparar_entrega.py"
fuente = archivo.read_text(encoding="utf-8")
arbol = ast.parse(fuente)
funciones = [ast.get_source_segment(fuente,nodo) for nodo in arbol.body
             if isinstance(nodo,ast.FunctionDef) and nodo.name in ("bloques","formato","render","crear_docx")]
encabezado = '''"""Conversores de documentos y entrada del generador de la aventura 2D."""
from pathlib import Path
import sys
import html
import re
from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape
RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / "documentacion" / "primera_entrega"
sys.path.insert(0,str(RAIZ))
from temas import TEMAS

'''
nuevo = encabezado+'\n\n'.join(funciones)+"\n\nif __name__ == '__main__':\n    from entrega_aventura import main\n    main()\n"
nuevo = nuevo.replace("CyberQuest: Defensa Digital","CyberQuest: Los guardianes del escudo")
archivo.write_text(nuevo,encoding="utf-8")
(RAIZ/"herramientas"/"mockups_entrega.py").write_text('"""Compatibilidad con los mockups vigentes de aventura 2D."""\nfrom mockups_aventura import mockup\n',encoding="utf-8")
print("Generador anterior retirado; conversores reutilizables conservados.")
