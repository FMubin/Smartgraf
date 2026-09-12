import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        console_messages = []
        page.on("console", lambda msg: console_messages.append(f"{msg.type.upper()}: {msg.text}"))
        page.on("pageerror", lambda err: print(f"PAGE ERROR:\n{err}"))
        
        file_path = os.path.abspath("index.html")
        await page.goto(f"file:///{file_path}")
        await page.wait_for_timeout(2000)
        
        print("Clicking generate-massal menu...")
        try:
            await page.click(".nav-item[data-view='generate-massal']", timeout=3000)
            await page.wait_for_timeout(1000)
        except Exception as e:
            print("Failed to click generate-massal:", e)
            
        print("Clicking ekspor-cetak menu...")
        try:
            await page.click(".nav-item[data-view='ekspor-cetak']", timeout=3000)
            await page.wait_for_timeout(1000)
        except Exception as e:
            print("Failed to click ekspor-cetak:", e)
            
        print("\n--- Console Messages ---")
        for msg in console_messages:
            print(msg)
        print("------------------------")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
