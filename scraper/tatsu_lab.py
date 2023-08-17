from playwright.async_api import async_playwright
import pandas as pd
import asyncio

async def init_playwright(p):  
    """
    Initialize playwright with chromium browser and open a new page.
    """
    browser = await p.chromium.launch(headless=True)
    page = await browser.new_page()
    await page.goto("https://tatsu-lab.github.io/alpaca_eval/")
    return browser, page

async def get_column_names(page):
    """
    Get the column names from the page.
    """
    await asyncio.sleep(15)
    column_elements = await page.query_selector_all("tr th")
    column_names = []
    for element in column_elements:
        column_name = await element.inner_text()
        column_names.append(column_name)
    return column_names

async def get_table_data(page, num_rows):
    """
    Get the table data from the page.
    """
    table_data = []
    row_elements = await page.query_selector_all("#leaderboard tr")
    for row_element in row_elements[1:num_rows+1]:  # Skip the header row
        cell_elements = await row_element.query_selector_all("td")
        row_data = []
        for cell_element in cell_elements:
            cell_data = await cell_element.inner_text()
            row_data.append(cell_data)
        table_data.append(row_data)
    return table_data

async def main():
    """
    The main function to run the script.
    """
    async with async_playwright() as p:
        browser, page = await init_playwright(p)
        column_headers = await get_column_names(page)
        additional_columns = ['Try Playground', 'Try API', 'Cost 100 tokens/sec', 'How to setup?']
        column_headers = additional_columns + column_headers
        table_data = await get_table_data(page, 10)
        for row in table_data:
            row.insert(0, 'Coming soon...')
            row.insert(0, 'Coming soon...')
            row.insert(0, 'Coming soon...')
            row.insert(0, 'Coming soon...')
        df = pd.DataFrame(table_data, columns=column_headers)
        html = df.to_html()
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                .center-content {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    flex-direction: column;
                }}
                .dataframe {{
                    margin: auto;
                }}
            </style>
        </head>
        <body>
            <div class="center-content">
                <a href="https://tatsu-lab.github.io/alpaca_eval/"><h1>AlpacaEval Leaderboard</h1></a>
                <div style="width: 500px; overflow-x: auto;">{html}</div>
            </div>
        </body>
        </html>
        '''
        with open('tatsu_lab.html', 'w') as f:
            f.write(html)
        return column_headers, table_data

asyncio.run(main())
