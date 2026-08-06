import json, os, glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, 'data')


def build():
    index_path = os.path.join(DATA_DIR, 'index.json')
    with open(index_path, encoding='utf-8') as f:
        index = json.load(f)

    data = {}
    for entry in index:
        fp = os.path.join(DATA_DIR, entry['file'])
        with open(fp, encoding='utf-8') as f:
            data[entry['id']] = json.load(f)
        entry['count'] = len(data[entry['id']]['questions'])

    out = os.path.join(DATA_DIR, 'bundle.js')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('window.QUIZ_INDEX = ')
        json.dump(index, f, ensure_ascii=False)
        f.write(';\nwindow.QUIZ_DATA = ')
        json.dump(data, f, ensure_ascii=False)
        f.write(';\n')
    print(f'Da tao {out} voi {len(index)} bo de.')


if __name__ == '__main__':
    build()
