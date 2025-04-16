from playwright.sync_api import sync_playwright
import time

def screenshot_tradingview(pair="BTCUSDT", output_path="chart.png"):
    url = f"https://www.tradingview.com/chart/?symbol=BINANCE:{pair}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        page.goto(url)
        time.sleep(10)  # attendre le chargement complet

        try:
            page.locator('text=Maybe later').click(timeout=3000)
        except:
            pass

        page.screenshot(path=output_path)
        print(f"✅ Screenshot enregistré sous : {output_path}")

        browser.close()

screenshot_tradingview()
