from jinja2 import Template

html_templates = {
    'remove': Template('<td class="remove">&nbsp;{{ old }}</td>'),
    'insert': Template('<td class="insert">&nbsp;{{ new }}</td>'),
    'match': Template('<td class="match">&nbsp;{{ new }}</td>'),
    'alter': Template('<td class="alter">&nbsp;{{ new }}</td>'),
    'document': Template("""<!doctype html>
<html>
    <style>
    td { min-width: 40px; }
    .remove { background: #FFAEAE; }
    .insert { background: #B0E57C; }
    .alter { background: #FFF0AA; }
    </style>
    <table>
    {% for row in rows %}
        <tr>
        {% for col in row %}
            {{ col }}
        {% endfor %}
        </tr>
    {% endfor %}
    </table>
</html>"""),
}

def html(diffs, templates=html_templates):
    "Render diffs as HTML."

    rows = []

    for row_edit, row_details in diffs:

        cols = []

        for edit, (old, new) in row_details:
            cols.append(templates[edit].render(old=old, new=new))

        rows.append(cols)

    return templates['document'].render(rows=rows)
