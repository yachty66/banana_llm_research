from playwright.async_api import async_playwright
import asyncio
import pandas as pd

async def init_playwright(p):  # add p as an argument
    """
    Initialize playwright
    """
    browser = await p.chromium.launch(headless=True)
    page = await browser.new_page()
    await page.goto("https://chat.lmsys.org/?arena")
    return browser, page

async def get_column_names(page):
    """
    Get the column names from the page.
    """
    for i in range(10):
        try:
            await asyncio.sleep(15)
            column_headers_elements = await page.query_selector_all('th span')
            column_headers = []
            for element in column_headers_elements:
                column_headers.append(await element.inner_text())
            return column_headers
        except Exception as e:
            print("An error occurred. Gradio probably didnt loaded:", e)
            print("Reloading the page and trying again...")
            await page.reload()
    print("Failed to get column names after 10 attempts.")

async def get_table_data(page, num_rows):
    """
    Get the table data from the page.
    """
    table_data = []
    for i in range(num_rows):
        try:
            row_elements = await page.query_selector_all(f'tr.svelte-1tclfmr:nth-child({i+1}) td span')
            row_data = []
            for element in row_elements:
                row_data.append(await element.inner_text())
            table_data.append(row_data)
        except Exception as e:
            print("An error occurred while getting table data:", e)
            print("Reloading the page and trying again...")
            await page.reload()
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
                <a href="https://chat.lmsys.org/?arena"><h1>LMSYS</h1></a>
                <div style="width: 500px; overflow-x: auto;">{html}</div>
            </div>
        </body>
        </html>
        '''
        with open('lmsys.html', 'w') as f:
            f.write(html)
        return column_headers, table_data

asyncio.run(main())
