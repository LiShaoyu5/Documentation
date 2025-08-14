> 更新时间：2025-08-14

# 能力名称

图片水印可以帮助您保护企业图像的版权、防止图片泄露、在出现泄露事件时进行溯源等。在使用图片水印时，您需要将图片水印SDK嵌入到业务系统或使用网页端的图片水印服务，给图片添加水印或提取其中的水印信息。本文介绍如何使用图片水印功能。

## 应用场景

应用场景


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

```python
pip install sdk
```

#### **Java**

```java
<dependency>
  <groupId>com.subfunctionA</groupId>
  <artifactId>subfunctionA-sdk</artifactId>
  <version>1.0.0</version>
</dependency>
```

<!-- tabs:end -->

## 快速入门

### 子功能A

子功能A的功能是给输入图片添加水印，并返回添加水印后的图片。

#### SDK

<!-- tabs:start -->

#### **Python**

```python
# 1. 引入SDK
from sdk import funcA
# 2. 调用接口
funcA(input_image_path, output_image_path, api_key)
```

#### **Java**

```java
// 1. 引入SDK
import com.subfunctionA.funcA;
// 2. 调用接口
funcA.funcA(input_image_path, output_image_path, api_key);
```

<!-- tabs:end -->

#### **通用 API**

**请求 URL**

请求URL及API_KEY取决于用户本地部署时的配置：

`POST https://api.example.com/v1/subfunctionA`

**请求头**

`Content-Type: application/json`

**请求体（JSON 格式）**

```json
{
  "api_key": "API_KEY",
  "input_image": "BASE64_ENCODED_IMAGE_STRING"
}
```

**响应体（JSON 格式）**

```json
{
  "output_image": "BASE64_ENCODED_IMAGE_STRING"
}
```

**cURL 示例**

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "api_key": "API_KEY",
    "input_image": "$(base64 input_image.jpg)"
  }' \
  https://api.example.com/v1/subfunctionA
```

---

### 子功能B

……