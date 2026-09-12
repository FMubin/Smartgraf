import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        file_path = os.path.abspath("index.html")
        await page.goto(f"file:///{file_path}")
        await page.wait_for_timeout(2000)
        
        # Test while in Generate Massal tab (view-editor is hidden)
        await page.click(".nav-item[data-view='generate-massal']")
        await page.wait_for_timeout(500)
        
        result = await page.evaluate("""async () => {
            const report = [];
            const viewEditor = document.getElementById("view-editor");
            
            // Apply offscreen rendering
            const wasActive = viewEditor.classList.contains("active");
            const origStyle = {
                display: viewEditor.style.display,
                position: viewEditor.style.position,
                left: viewEditor.style.left,
                top: viewEditor.style.top,
                visibility: viewEditor.style.visibility,
                opacity: viewEditor.style.opacity,
                zIndex: viewEditor.style.zIndex
            };
            
            viewEditor.style.display = "flex";
            viewEditor.style.position = "fixed";
            viewEditor.style.left = "-9999px";
            viewEditor.style.top = "0";
            viewEditor.style.visibility = "visible";
            viewEditor.style.opacity = "1";
            viewEditor.style.zIndex = "-9999";
            
            const element = document.getElementById("infographic-element");
            
            for (let b = 1; b <= 7; b++) {
                activeBab = b;
                updatePreview();
                await new Promise(r => setTimeout(r, 100));
                
                try {
                    const canvas = await html2canvas(element, { scale: 1.5, logging: false });
                    report.push({ bab: b, success: true, width: canvas.width, height: canvas.height });
                } catch (err) {
                    report.push({ bab: b, success: false, error: err.toString() });
                }
            }
            
            // Restore
            viewEditor.style.display = origStyle.display;
            viewEditor.style.position = origStyle.position;
            viewEditor.style.left = origStyle.left;
            viewEditor.style.top = origStyle.top;
            viewEditor.style.visibility = origStyle.visibility;
            viewEditor.style.opacity = origStyle.opacity;
            viewEditor.style.zIndex = origStyle.zIndex;
            
            return report;
        }""")
        
        print("=== RENDERING RESULTS FOR ALL 7 BABS ===")
        all_ok = True
        for r in result:
            print(r)
            if not r.get("success"):
                all_ok = False
                
        print("ALL BABS PASSED:", all_ok)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
