# docs-gl-offline
A fork of [docs.gl](https://github.com/BSVino/docs.gl) optimized for stable offline/local deployment — fixes MIME type issues, plain-text HTML rendering, and link-triggered file downloads for OpenGL documentation.

### Quick Start
```bash
git clone https://github.com/<你的用户名>/docs-gl-offline.git
cd docs-gl-offline
python compile.py --local-assets
python start_offline_fixed.py
# Visit http://localhost:8000
```
License
Same as upstream docs.gl (see LICENSE). OpenGL content © Khronos Group.

# 修改日志

1. `<a>`标签输出，index页面内的所有的输出均带有`.html`后缀。
2. 合并所有的API文档至`api_versions`文件夹下。
3. 修改了`python`本地部署服务器的方式。
4. `htdocs/api_versions`目录下，所有 HTML 页面均带有html后缀。