"""Assemble qg/index.html + qg/etat.js en un seul fichier autonome (qg/apercu/qg-allure.html),
lisible sur n'importe quel appareil sans passer par claude.ai."""
from pathlib import Path
d = Path(__file__).parent
html = (d / "index.html").read_text(encoding="utf-8")
etat = (d / "etat.js").read_text(encoding="utf-8")
html = html.replace('<script src="etat.js"></script>', "<script>\n" + etat + "\n</script>")
out = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<style>[hidden]{display:none!important}body{margin:0}</style>\n</head>\n<body>\n' + html + '\n</body>\n</html>\n')
(d / "apercu").mkdir(exist_ok=True)
(d / "apercu" / "qg-allure.html").write_text(out, encoding="utf-8")
print("ok", len(out))
