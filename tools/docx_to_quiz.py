import docx, json, re, sys, os
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_bundle

CIRCLE_MAP = {'①': 'A', '②': 'B', '③': 'C', '④': 'D'}


def iter_block_items(doc):
    for child in doc.element.body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, doc)
        elif child.tag == qn('w:tbl'):
            yield Table(child, doc)


def table_to_text(table):
    lines = []
    for row in table.rows:
        cells = [c.text.strip() for c in row.cells]
        cells = [c for c in cells if c]
        if cells:
            lines.append(' | '.join(cells))
    return '\n'.join(lines)


def extract(path):
    d = docx.Document(path)
    questions = []
    cur = None
    pending_lines = []
    range_end = None

    def flush():
        nonlocal cur
        if cur:
            questions.append(cur)
            cur = None

    def start_question(num):
        nonlocal cur, pending_lines
        flush()
        cur = {'num': num, 'raw_lines': [], '_bold_option_text': None, 'correct': None}
        if pending_lines:
            cur['raw_lines'].extend(pending_lines)
        if range_end is not None and num >= range_end:
            pending_lines = []

    for block in iter_block_items(d):
        if isinstance(block, Table):
            text = table_to_text(block)
            if not text.strip():
                continue
            if cur is not None:
                cur['raw_lines'].append(text)
            else:
                pending_lines.append(text)
            continue

        p = block
        text = p.text
        if not text.strip():
            continue
        bold_texts = [r.text for r in p.runs if r.bold]

        mrange = re.match(r'^\[(\d{1,3})-(\d{1,3})\]', text)
        if mrange:
            flush()
            pending_lines = []
            range_end = int(mrange.group(2))
            continue
        if re.match(r'^\[(\d{1,3})번\]\s*$', text):
            continue
        mm2 = re.match(r'^\[(\d{1,3})번\s*\(([^)]*)\)\]', text)
        if mm2:
            start_question(int(mm2.group(1)))
            continue

        m = re.match(r'^(\d{1,3})\.\s*(.*)', text, re.S)
        if m and (bold_texts and re.match(r'^\d{1,3}\.$', bold_texts[0])):
            start_question(int(m.group(1)))
            rest = m.group(2)
            if rest.strip():
                cur['raw_lines'].append(rest)
            for bt in bold_texts[1:]:
                if any(c in bt for c in CIRCLE_MAP):
                    cur['_bold_option_text'] = bt
            continue

        if cur is None:
            pending_lines.append(text)
            continue

        cur['raw_lines'].append(text)
        if any(c in text for c in CIRCLE_MAP):
            for bt in bold_texts:
                if any(c in bt for c in CIRCLE_MAP):
                    cur['_bold_option_text'] = bt

    flush()

    def split_options(line):
        parts = re.split(r'(①|②|③|④)', line)
        opts = []
        i = 1
        while i < len(parts):
            marker = parts[i]
            val = parts[i + 1] if i + 1 < len(parts) else ''
            opts.append((marker, val.strip()))
            i += 2
        return opts

    for q in questions:
        stem_lines = []
        opts = []
        for line in q['raw_lines']:
            positions = [line.find(c) for c in CIRCLE_MAP if c in line]
            if not positions:
                stem_lines.append(line)
            else:
                idx = min(positions)
                before = line[:idx].strip()
                if before:
                    stem_lines.append(before)
                opts.extend(split_options(line[idx:]))
        q['stem'] = '\n'.join(stem_lines).strip()
        q['options'] = [{'label': CIRCLE_MAP[m], 'text': v} for m, v in opts]
        bold_opt = q.pop('_bold_option_text', None)
        q['correct_source'] = 'docx'
        if bold_opt:
            for m, v in split_options(bold_opt):
                q['correct'] = CIRCLE_MAP[m]
        if q['correct'] is None:
            q['correct_source'] = None
        del q['raw_lines']

    tables = []
    for t in d.tables:
        tables.append([[c.text for c in row.cells] for row in t.rows])

    return questions, tables


def main():
    if len(sys.argv) < 4:
        print('Usage: python docx_to_quiz.py <input.docx> <output.json> "<Quiz title>"')
        sys.exit(1)
    src, out, title = sys.argv[1], sys.argv[2], sys.argv[3]
    questions, tables = extract(src)
    unmarked = [q['num'] for q in questions if q['correct'] is None]
    data = {'title': title, 'source': os.path.basename(src), 'questions': questions, 'tables': tables}
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'{len(questions)} cau hoi -> {out}')
    if unmarked:
        print(f'CANH BAO: {len(unmarked)} cau khong co dap an duoc danh dau (bold) trong file goc: {unmarked}')
        print('Mo file JSON va dien truong "correct" (A/B/C/D) cho cac cau nay, hoac sua tren app.')

    data_dir = os.path.dirname(os.path.abspath(out))
    index_path = os.path.join(data_dir, 'index.json')
    quiz_id = os.path.splitext(os.path.basename(out))[0]
    index = []
    if os.path.exists(index_path):
        with open(index_path, encoding='utf-8') as f:
            index = json.load(f)
    index = [e for e in index if e['id'] != quiz_id]
    index.append({'id': quiz_id, 'file': os.path.basename(out), 'title': title})
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    build_bundle.build()


if __name__ == '__main__':
    main()
