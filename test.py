import pandas as pd
import numpy as np

def display_table():
    df = pd.DataFrame(
       np.random.randn(10, 5),
       columns=('col %d' % i for i in range(5)))
    html = df.to_html()
    # Wrap the table in a div with scrolling
    html = f'<div style="width: 300px; height: 300px; overflow: auto;">{html}</div>'
    return html

# Save the HTML table to a file
with open('table.html', 'w') as f:
    f.write(display_table())