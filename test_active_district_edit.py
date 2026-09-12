import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        console_logs = []
        page_errors = []
        
        page.on("console", lambda msg: console_logs.append(f"[{msg.type.upper()}] {msg.text}"))
        page.on("pageerror", lambda err: page_errors.append(str(err)))
        
        file_path = os.path.abspath("index.html")
        await page.goto(f"file:///{file_path}")
        await page.wait_for_timeout(1000)
        
        # 1. Open Cover Buku view
        await page.click(".sidebar-new .nav-item[data-view='cover-buku']")
        await page.wait_for_timeout(500)
        
        # 2. Upload dummy master cover
        dummy_b64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="
        await page.evaluate(f"""() => {{
            manualCoverImages.masterFront = '{dummy_b64}';
            districtsData.forEach(d => manualCoverImages.districtFront[d.nama.toUpperCase()] = '{dummy_b64}');
            renderCoverBukuPreview();
        }}""")
        await page.wait_for_timeout(300)
        
        # Check active district 0 (SUMUR)
        name_input_0 = await page.locator("#cover-edit-dist-name").input_value()
        katalog_input_0 = await page.locator("#cover-edit-katalog").input_value()
        rendered_name_0 = await page.locator("#cf-dist-name").text_content()
        print(f"District 0 (SUMUR): input={name_input_0}, kat={katalog_input_0}, rendered={rendered_name_0}")
        assert "SUMUR" in name_input_0
        assert "SUMUR" in rendered_name_0
        assert "1102001.3601010" in katalog_input_0
        
        # Switch to district 1 (CIMANGGU)
        await page.select_option("#cover-select-kecamatan", "1")
        await page.wait_for_timeout(200)
        name_input_1 = await page.locator("#cover-edit-dist-name").input_value()
        katalog_input_1 = await page.locator("#cover-edit-katalog").input_value()
        rendered_name_1 = await page.locator("#cf-dist-name").text_content()
        print(f"District 1 (CIMANGGU): input={name_input_1}, kat={katalog_input_1}, rendered={rendered_name_1}")
        assert "CIMANGGU" in name_input_1
        assert "CIMANGGU" in rendered_name_1
        assert "1102001.3601020" in katalog_input_1
        
        # 3. Test Editing active district values
        await page.fill("#cover-edit-dist-name", "CIMANGGU MEKAR")
        await page.wait_for_timeout(200)
        rendered_edited = await page.locator("#cf-dist-name").text_content()
        print(f"Edited name render: {rendered_edited}")
        assert "CIMANGGU MEKAR" in rendered_edited
        
        # 4. Check Magic Grab OCR Button
        ocr_btn_visible = await page.locator("#btn-run-ocr-grab").is_visible()
        print(f"Magic Grab OCR Button visible: {ocr_btn_visible}")
        assert ocr_btn_visible is True
        
        errors = [l for l in console_logs if "[ERROR]" in l]
        print(f"Total Page Errors: {len(page_errors)}")
        print(f"Total Console Errors: {len(errors)}")
        assert len(page_errors) == 0
        assert len(errors) == 0
        
        print("\n>>> ACTIVE DISTRICT BINDING & EDITING VERIFIED 100%! <<<")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
