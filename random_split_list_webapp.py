# Please check out the HTML file instead at index.thml

from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

def split_list_into_groups(incl, m):
    random.shuffle(incl)
    n = len(incl)
    group_sizes = [n // m + (1 if i < n % m else 0) for i in range(m)]
    groups = []
    start = 0
    for size in group_sizes:
        groups.append(incl[start:start + size])
        start += size
    for group in groups:
        group.sort()
    return groups

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        incl = list(map(int, filter(None, request.form['numbers'].strip().split(','))))
        m = int(request.form['groups'])
        groups = split_list_into_groups(incl, m)
        return render_template_string(template, groups=groups, enumerate=enumerate)
    return render_template_string(template)

template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>List Splitter Randomizer</title>
    <script>
      function copyToClipboard(groupId) {
        var copyText = document.getElementById(groupId);
        var textArea = document.createElement("textarea");
        textArea.value = copyText.innerText;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand("Copy");
        textArea.remove();
        alert("Copied to clipboard");
      }
    </script>
  </head>
  <body>
    <h1>List Splitter Randomizer</h1>
    <form method="post">
      <label for="numbers">Enter numbers (comma-separated):</label><br>
      <input type="text" id="numbers" name="numbers" required><br>
      <label for="groups">Enter number of groups:</label><br>
      <input type="number" id="groups" name="groups" required><br><br>
      <input type="submit" value="Submit">
    </form>
    {% if groups %}
      <h2>Result</h2>
      {% for i, group in enumerate(groups) %}
        <div>
          <h3>Group {{ i+1 }}</h3>
          <ul id="group-{{ i+1 }}">
            {% for item in group %}
              <li>{{ item }}</li>
            {% endfor %}
          </ul>
          <button onclick="copyToClipboard('group-{{ i+1 }}')">Copy to Clipboard</button>
        </div>
      {% endfor %}
    {% endif %}
  </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)