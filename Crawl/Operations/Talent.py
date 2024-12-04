import asyncio


from  Utils.GetImage import check_text1, download_resume

async def Talent_Search(page):
    """处理推荐页面的操作"""
    print(f"当前页面为{page.url}")
    # 选择过滤条件 page.locator
    await page.get_by_text('不限职位').click()

    job_item = page.locator('div.job-info')
    job_item_count = await job_item.count()
    # for index in range(job_item_count):

    await job_item.nth(0).click()
    job_item = page.locator('div.select-condition')
    job_item_count = await job_item.count()
    for index in range(1, job_item_count):
        await page.locator('div.select-condition').nth(index).click()
    await page.locator('div.jobs-handle').get_by_text('确定').click()
    await page.locator('div.searchInputBox--R_eer').get_by_text('搜索', exact=True).click()

    await page.locator('span.ant-lpt-select-selection-item').get_by_text('沟通状态').click()
    await  page.locator('div.rc-virtual-list').get_by_text('隐藏我和同事已沟通').click()
    await  page.locator('label.ant-lpt-checkbox-wrapper').get_by_text('隐藏已查看').click()
    await asyncio.sleep(2)
    # 获取所有 .newResumeItem--ppozw 匹配的 div
    # communicate_buttons = page.locator('div.resumeCard--uwSqc')
    communicate_buttons = page.locator(
        'button.ant-lpt-btn.ant-lpt-btn-primary.ant-lpt-teno-btn.ant-lpt-teno-btn-secondary')
    # 获取匹配的数量communicate_buttons
    count = await communicate_buttons.count()

    # 遍历所有 div
    click_GT = 0
    for index in range(count - 1, -1, -1):
        # 获取当前 div
        div = communicate_buttons.nth(index)

        # 在当前 div 内定位按钮
        # button = div.locator('span.btnContainer--NUXPG')
        if await check_text1(page, "立即沟通"):
            # # 检查按钮是否存在并可见
            # if await button.is_visible():
            # 点击按钮
            await div.get_by_text("立即沟通").click()

            await asyncio.sleep(1)
            # 定位目标元素
            close_button1 = page.locator('span.ant-im-modal-close-x span[aria-label="close"]')
            close_button2 = page.locator(
                'button.ant-lpt-modal-close span.ant-lpt-modal-close-x button span[aria-label="close"]')
            # 检查是否存在且可见
            if await close_button1.is_visible():
                # await close_button1.nth(index).click()
                await close_button1.click()
                print("沟通更多候选人页面关闭")
                # 检查元素是否存在并可见
            if await close_button2.is_visible():
                await close_button2.click()
                print("付费按钮关闭")
                break
            click_GT = click_GT + 1
            if click_GT >= 3:
                print(f"已点击 {click_GT} 个按钮，退出循环。")
                break
