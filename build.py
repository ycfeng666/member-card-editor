# -*- coding: utf-8 -*-
"""把 base64 资源注入模板，生成单文件 index.html

用法：python build.py
改完 _src/index.src.html 后必须重跑，否则 index.html（线上那份）还是旧的。
注意：图片常量需要带 `data:image/xxx;base64,` 前缀；字体在 CSS 的 url() 里自己带了前缀。
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# key -> (文件路径, 前缀)
REPL = {
    '__BASE_FRONT__': (os.path.join(HERE, 'base_front.png'), 'data:image/png;base64,'),
    '__BADGE__':      (os.path.join(HERE, 'badge.png'),      'data:image/png;base64,'),
    '__AVATAR__':     (os.path.join(ROOT, 'avatar.jpg'),     'data:image/jpeg;base64,'),
    '__ARCHIVO__':    (os.path.join(ROOT, 'fonts', 'ArchivoBlack-400.ttf'), ''),
    '__MONO__':       (os.path.join(ROOT, 'fonts', 'RobotoMono-700.ttf'),   ''),
}

def b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode()

def main():
    src = os.path.join(HERE, '_src', 'index.src.html')
    s = open(src, encoding='utf-8').read()
    for key, (path, prefix) in REPL.items():
        if not os.path.exists(path):
            raise SystemExit('缺少素材: ' + path)
        s = s.replace(key, prefix + b64(path))
    out = os.path.join(HERE, 'index.html')
    open(out, 'w', encoding='utf-8').write(s)
    print('built', out, round(os.path.getsize(out) / 1024), 'KB')
    left = [k for k in REPL if k in s]
    print('未替换占位符:', left if left else '无')

if __name__ == '__main__':
    main()
