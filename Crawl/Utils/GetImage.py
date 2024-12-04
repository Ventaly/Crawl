import requests
import os
async def get_image_src_and_download(page, selector, image_name):

        iframe = page.frame_locator("#tcaptcha_iframe")
        captcha_div = iframe.locator(f'img#{selector}')
        image_src = await captcha_div.get_attribute('src')
        print(f"图片 URL: {image_src}")
        print("22222222222")
        if image_src:
            print(f"{image_name} URL: {image_src}")
            download_image(image_src, image_name)
            return image_src
        else:
            print("未能提取图片的 URL")


def download_image(url, filename):

    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"{filename} 下载完成!")
async def check_text1(page, text):
    """检查页面上是否存在指定文本"""
    elements =await page.query_selector_all(f'text="{text}"')
    print(elements)
    if elements:
        print(f"页面上存在文本为‘{text}’的元素")
        return True
    else:
        print(f"页面上不存在文本为‘{text}’的元素")
        return False

async def download_resume(page, Job_Title, Applicant_Name):
    """尝试下载简历"""
    dir_name = "E:\Email-Attachments"

    async with page.expect_download() as download_info:
        await page.locator('div.b-portfolio-wrap-gray').get_by_text('下载').nth(0).click()
    download = await download_info.value
    path = await download.path()
    file_path1 = os.path.join(dir_name, Job_Title)
    file_path = os.path.join(file_path1, f"{Applicant_Name}.pdf")

    await download.save_as(file_path)
    print(f"下载简历至 {path}")
