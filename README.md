# 専科生ヲタ芸同好会 · 会员证编辑器

在线自制会员证：上传头像、改 Name / Band Name / 编号，实时预览，一键导出 300dpi PNG。

- 卡面尺寸 85.6 × 54.0 mm（CR80），导出 3033 × 1914 px 并写入 300 dpi
- 版式取自 `会员证.psd`（RiNG 会员证），品牌位替换为同好会字标
- 字体：Noto Sans SC（子集 GB2312 + JIS X 0208）、Archivo Black、Roboto Mono

本地打开 `index.html` 即可；`_src/index.src.html` 是模板，改动后用构建脚本注入 base64 资源。
