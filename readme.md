# docs-gl-offline
A fork of [docs.gl](https://github.com/BSVino/docs.gl) optimized for stable offline/local deployment — fixes MIME type issues, plain-text HTML rendering, and link-triggered file downloads for OpenGL documentation.

### Quick Start

```bash
python compile.py --local-assets
python start_offline_webserver.py
# Visit http://localhost:8000
```

License
Same as upstream docs.gl (see LICENSE). OpenGL content © Khronos Group.
