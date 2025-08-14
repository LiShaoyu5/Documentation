from scrapegraphai.graphs import SmartScraperGraph

# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "api_key": "",
        "model": "deepseek-chat",
        "base_url": "https://api.deepseek.com/v1",
        # "model_provider": "deepseek",
    },
    "verbose": True,
    "headless": False,
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="""
            提取该页面的文档内容，要求如下：
            1. 以Markdown格式返回，不必强求还原网页格式，但必须保证是工整的多级文档。
            2. 只返回文档正文内容，不需要侧边栏和顶部导航栏，及其它无关的页面内容。
            3. 去除文档中全部有关“阿里”、“阿里云”的字样。去除文档中所有超链接。
            """,
    source="https://help.aliyun.com/zh/dsc/data-security-center/user-guide/data-de-identification",
    config=graph_config,
)

result = smart_scraper_graph.run()

with open("../tools/data-de-identification.md", "w", encoding="utf-8") as f:
    f.write(result["content"])
