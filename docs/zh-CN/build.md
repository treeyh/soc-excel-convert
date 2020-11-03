```bash
# 打包：
python setup.py sdist bdist_wheel

# 安装twine工具
python -m pip install --user --upgrade twine

# 上传包
twine upload dist/*
```