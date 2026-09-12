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
        
        await page.add_init_script("window.alert = () => {};")
        
        file_path = os.path.abspath("index.html")
        await page.goto(f"file:///{file_path}")
        await page.wait_for_timeout(2000)
        
        # Mock districtsData to 2 items to run the export test quickly
        await page.evaluate("districtsData = districtsData.slice(0, 2);")
        
        # Click Generate Massal tab
        await page.click(".nav-item[data-view='generate-massal']")
        await page.wait_for_timeout(1000)
        
        print("Clicking mass generate button...")
        btn = page.locator("#btn-export-all-mass-tab")
        await btn.click()
        
        # Verify overlay is shown
        overlay_visible = await page.locator("#rendering-overlay").is_visible()
        print(f"Is rendering overlay visible right after click: {overlay_visible}")
        
        # Wait up to 10 seconds for completion by polling the overlay visibility
        for i in range(10):
            await page.wait_for_timeout(1000)
            overlay_visible = await page.locator("#rendering-overlay").is_visible()
            if not overlay_visible:
                break
                
        print(f"Is rendering overlay visible after polling: {overlay_visible}")
        
        print("\n--- Console Logs during export ---")
        for msg in console_messages:
            print(msg)
        print("---------------------------------")
        
        if not overlay_visible:
            print("SUCCESS: Rendering overlay displayed and dismissed correctly!")
        else:
            print("FAIL: Rendering overlay stuck on screen.")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
