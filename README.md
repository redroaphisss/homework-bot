# Homebot

在使用本项目前，需要配置 Claude Code API 密钥：

```bash
ANTHROPIC_BASE_URL=YOUR_API_URL
ANTHROPIC_AUTH_TOKEN=YOUR_API_KEY
ANTHROPIC_MODEL=YOUR_MODEL
```


## 开始使用

本项目使用 `uv` 进行 Python 依赖管理。

```bash
# 安装依赖
uv sync

# 运行脚本
uv run python your_script.py
```

## 依赖列表

- numpy
- pandas
- matplotlib
- PyPDF2
- openpyxl
- python-docx