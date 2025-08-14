# 图片水印

> 更新时间：2025-08-14

图片水印可以帮助您保护企业图像的版权、防止图片泄露、在出现泄露事件时进行溯源等。在使用图片水印时，您需要将图片水印SDK嵌入到业务系统或使用网页端的图片水印服务，给图片添加水印或提取其中的水印信息。本文介绍如何使用图片水印功能。

## 应用场景

- 保护企业图片版权，防止图片泄露。
- 通过嵌入明水印直接可见水印信息，快速定位泄露人员。
- 通过嵌入暗水印隐藏水印信息，结合SDK或网页端提取功能溯源泄露事件。

## 环境需求

- 操作系统：Windows / Linux / macOS
- Python 版本：3.8+ / Java 版本：1.8+
- 必要依赖：
  - requests >= 2.26.0
  - numpy >= 1.21.0
  - pandas >= 1.3.0
- 硬件需求：
  - CPU：Intel i5 或以上
  - 内存：8GB+
  - 硬盘空间：500MB 以上可用空间

---

## 安装

我们提供 Python 和 Java 的 SDK，方便用户直接集成使用。此外，我们还提供详细的 API 文档，用户可以根据文档内容开发自定义的调用接口，以满足更灵活的业务需求。

<!-- tabs:start -->

#### **Python**

```bash
pip install image-watermark-sdk
```

#### **Java**

```xml
<dependency>
  <groupId>com.example</groupId>
  <artifactId>image-watermark-sdk</artifactId>
  <version>1.0.12</version>
</dependency>
```

<!-- tabs:end -->

## 快速入门

### 添加水印

#### SDK

<!-- tabs:start -->

#### **Python**

```python
from image_watermark import Watermark

wm = Watermark(api_key="AK", api_secret="SK")
wm.embed(input_image_path="input.jpg", output_image_path="output.jpg", watermark_text="Confidential")
```

#### **Java**

```java
import com.example.watermark.Watermark;

Watermark wm = new Watermark("AK", "SK");
wm.embed("input.jpg", "output.jpg", "Confidential");
```

<!-- tabs:end -->

#### **通用 API**

**请求 URL**

`POST https://api.example.com/v1/image-watermark/embed`

**请求体（JSON 格式）**

```json
{
  "api_key": "AK",
  "api_secret": "SK",
  "input_image": "BASE64_ENCODED_IMAGE",
  "watermark_text": "Confidential"
}
```

**响应体（JSON 格式）**

```json
{
  "output_image": "BASE64_ENCODED_IMAGE"
}
```

---

### 提取暗水印

#### SDK

<!-- tabs:start -->

#### **Python**

```python
from image_watermark import Watermark

wm = Watermark(api_key="AK", api_secret="SK")
result = wm.extract("leaked.jpg")
print(result)  # 返回暗水印原文
```

#### **Java**

```java
import com.example.watermark.Watermark;

Watermark wm = new Watermark("AK", "SK");
String result = wm.extract("leaked.jpg");
System.out.println(result);
```

<!-- tabs:end -->

**提取流程**

1. 登录办公安全平台控制台。
2. 在左侧导航栏，选择**数字水印服务** > **提取服务**。
3. 创建提取任务，上传待提取文件，设置水印版本、类型及位宽。
4. 查看提取结果，获取暗水印原文。

---

## 计费说明

- 计费采用包年包月模式。

