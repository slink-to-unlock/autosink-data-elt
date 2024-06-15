# 数据提取-加载-转换

[🇬🇧](README.md) | [🇰🇷](README.kr.md) | [🇨🇳](README.zh-CN.md)

解析数据湖中的值并将其加载到内存中，然后可以运行数据标记器。将完成标记的数据存储到特征存储中。autosink-data-elt包括用于读取和写入数据湖中存储的json文件的实用程序类和定义的数据类型。当从树莓派提取的数据存储在数据湖中时，将数据加载并进行标记，以转换为特征存储中的形式，因此将其命名为ELT。

## 功能

- [ ] 解析数据湖中的值并将其加载到内存中，然后将数据标记器整理为易于读取的形式。
- [ ] 调用标记器。
- [ ] 将完成标记的数据存储到特征存储中。

# 环境

环境基于 MacOS、Linux。

## `Makefile`

`Makefile`具有以下功能。

### `make lint`

- 若要使用`.vscode`设置，请安装`pylint`扩展。
- 使用linter的默认设置覆盖`pyproject.toml`文件中指定的选项来lint代码。

### `make format`

- 格式化程序使用google的`yapf`。
- 使用`pyproject.toml`文件中指定的选项覆盖`yapf`格式化程序的默认设置来格式化代码。
- 若要使用`.vscode`设置，请安装`yapf`扩展。

### `make test`

- 测试使用`unittest`。
- 支持`test_*.py`和`*_test.py`模式。
- 测试文件必须连接到包含测试的位置，并且必须有`__init__.py`。

### `make publish`

- 请按以下格式编写`~/.pypirc`文件。
   