from pyppeteer import launch
import asyncio
async def main(pdd1):
    try:
        browser = await launch({
            "headless":False,
            "dumpio":True,
            "args":[
                "--no-sandbox",
                "--window-size=500,500",
                "--disable-infobars",
                "--log-level=3",
                "--enable-extensions",
            ]
        })
        page = await browser.newPage()

        await page.setUserAgent(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.1.3904.97 Safari/537.36")
        await asyncio.wait_for(page.goto(
            'http://www.baidu.com',
            {"timeout": 1000 * 5}), timeout=5.0)
        page_1 = (await browser.pages())[1]
    except Exception as e:
        print("???",e)
        await browser.close()
        return None
    await browser.close()

if __name__ == '__main__':
    print("start")
    url_list = [1]
    loop = asyncio.get_event_loop()
    tasks = [(main(url)) for url in url_list]
    loop.run_until_complete(asyncio.wait(tasks))
