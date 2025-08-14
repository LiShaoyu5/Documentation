# 数据脱敏

> 更新时间：2025-08-14

数据脱敏能力支持静态脱敏和动态脱敏，帮助您保护敏感数据，防止泄露或违规使用。在使用数据脱敏时，您可以通过SDK或控制台任务配置完成静态或动态的数据脱敏处理。本文档介绍如何使用数据脱敏功能。

## 应用场景

- 将敏感数据与第三方共享时，保护隐私字段不被泄露。
- 在分析、统计或展示数据时，屏蔽部分敏感信息。
- 在需要回源解密的场景中安全加密存储数据。

## 环境需求

- 操作系统：Windows / Linux / macOS
- Python 版本：3.8+ / Java 版本：1.8+
- 必要依赖：
  - requests >= 2.26.0
  - pandas >= 1.3.0
- 硬件需求：
  - CPU：Intel i5 或以上
  - 内存：8GB+
  - 硬盘空间：500MB 以上可用空间

---

## 安装

我们提供 Python 和 Java 的 SDK，方便用户直接集成使用。此外，还提供详细的 API 文档供自定义调用。

<!-- tabs:start -->

#### **Python**

```bash
pip install data-deidentification-sdk
```

#### **Java**

```xml
<dependency>
  <groupId>com.example</groupId>
  <artifactId>data-deidentification-sdk</artifactId>
  <version>1.0.0</version>
</dependency>
```

<!-- tabs:end -->

## 快速入门

### 静态脱敏

静态脱敏通过创建脱敏任务，指定目标数据资产，并依据脱敏规则匹配目标敏感字段，采用脱敏算法（如遮盖、加密、替换等）处理指定字段，并将结果保存到目标位置。

#### SDK

<!-- tabs:start -->

#### **Python**

```python
from data_deid import StaticMasking

config = {
  "method": "hash",
  "key": "123456",
  "fields": ["name", "age"]
}

masker = StaticMasking(api_key="AK", config=config)
masker(input_path="input.csv", output_path="output.csv")
```

#### **Java**

```java
import com.example.deid.StaticMasking;

StaticMasking masker = new StaticMasking("AK", "123456", "hash", "name,age");
masker.mask("input.csv", "output.csv");
```

<!-- tabs:end -->

#### **通用 API**

`POST https://api.example.com/v1/data-mask/static`

**请求体**

```json
{
  "api_key": "AK",
  "api_secret": "SK",
  "task_id": "TASK_ID"
}
```

---

### 动态脱敏

动态脱敏通过调用 `ExecDatamask` 接口，对 JSON 格式数据中指定字段进行数据脱敏处理。

#### SDK

<!-- tabs:start -->

#### **Python**

```python
from data_deid import DynamicMasking
```

#### **Java**

```java
import com.example.deid.DynamicMasking;
```

<!-- tabs:end -->

---

## 脱敏算法示例

提供多种脱敏算法，包括：哈希脱敏、遮盖脱敏、替换脱敏、变换脱敏、加密脱敏和洗牌脱敏：

- 哈希脱敏：将敏感字段值进行哈希处理，生成摘要，再替换原始值。
- 遮盖脱敏：将敏感字段值进行遮盖，只保留字段长度，但不显示具体内容。
- 替换脱敏：将敏感字段值替换为固定字符，如 *。
- 变换脱敏：将敏感字段值进行随机替换，但保留字段长度。
- 加密脱敏：将敏感字段值进行加密处理，再替换原始值。
- 洗牌脱敏：将敏感字段值进行洗牌处理，再替换原始值。

---

## 计费说明

- 计费采用包年包月模式。

