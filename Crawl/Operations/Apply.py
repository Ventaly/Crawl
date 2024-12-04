import asyncio


from  Utils.GetImage import check_text1, download_resume

async def apply(page):
    """处理申请页面的操作"""
    print(f"当前页面为{page.url}")
    contacts = await page.query_selector_all('.newApplyCardContent--IIss4')
    for contact in contacts:
        await contact.click()
        await asyncio.sleep(1)

        if await check_text1(page, '下载'):
            await download_resume(page)
        elif await check_text1(page, "向TA索要"):
            print("当前候选人未公开简历")
            await page.get_by_role("button", name="向TA索要").click()
        else:
            print("出现未知错误")

