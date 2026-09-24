# STAIL · Personal AI Stylist — Web 设计方案 v0.1

> 对应 PPT：“STAIL” Personal AI Stylist（By Nanami & Clara）
> 可交互视觉稿：[`design/mockup.html`](./mockup.html)（直接用浏览器打开，顶部导航可切换 4 个页面）

---

## 1. 设计理念

PPT 的风格是 **复古剪贴簿 / 杂志拼贴（scrapbook collage）**：旧纸、撕边、纸胶带、半调网点、蕾丝、格子手帕，加上口红、粉饼、蝴蝶结这类贴纸元素。标题和正文都是手写体，主色是覆盆子粉 / 洋红。

Web 端延续这套语言，同时守住一条原则：**装饰归背景，内容归卡片**。

- 背景层：固定的拼贴画布（洋红笔刷条、半调粉块、书页碎片、蕾丝、格子手帕），滚动时不动，营造“贴在同一页剪贴簿上”的感觉。
- 内容层：每块信息都是一个“贴上去的纸片”（撕边粉纸、横线笔记本、方格本、拍立得、布料样片），和 PPT 各页的卡片一一对应。
- 标题永远贴在纸胶带上（PPT 每页的招牌做法）。

---

## 2. 视觉规范

### 2.1 色板（从 PPT 取色）

| Token | 色值 | 用途 |
|---|---|---|
| `--cream` | `#F1E9DC` | 页面底色 / 旧纸 |
| `--magenta` | `#C23F7E` | 笔刷色块、主按钮 |
| `--magenta-deep` | `#A8306A` | 深色笔刷块 |
| `--ink` | `#9C1F57` | **所有文字**（标题 + 正文） |
| `--pink-paper` | `#F7CFE2` | 撕边粉纸卡片 |
| `--pink-light` | `#FCE7F0` | 浅粉纸 / 方格本 |
| `--halftone` | `#E4A6C5` | 半调网点底 |
| `--tape` | `#D9C49C` | 纸胶带（标题、次按钮、导航选中态） |
| `--fabric` | `#E8386D` | 亮粉布料（选中态、强调卡片，对应 Ethical/Legal/Social 页） |
| `--plaid` | `#E0433F` | 格子手帕红线 |
| `--sticky` | `#F7EDA4` | 黄色小胶带（贴拍立得） |

文字统一用 `--ink`，放在浅色纸片上，对比度满足 WCAG AA。

### 2.2 字体

| 角色 | 字体 | 说明 |
|---|---|---|
| 标题 / 按钮 | **Caveat Brush** | 最接近 PPT 的粗手写标题 |
| 正文 / 表单 | **Caveat**（400–700） | 细手写，对应 PPT 正文 |
| 装饰书页 | **Libre Baskerville** | 背景里的旧书碎片 |

字体文件已放在本地 `design/fonts/`（Google Fonts，OFL 协议）。手写体可读性一般，所以正文字号不低于 20px。若之后需要中文界面，建议标题用「站酷快乐体」，正文用「霞鹜文楷」。

### 2.3 材质组件（PPT 元素 → Web 组件）

| PPT 元素 | Web 组件 | CSS 实现 |
|---|---|---|
| 米色纸胶带 | `.tape` 标题 / `.btn-tape` 次按钮 / `.chip` 标签 | 锯齿 `clip-path` + 噪点纹理 + 高光渐变 |
| 撕边粉纸 | `.paper` 信息卡 | 伪元素加 SVG `feTurbulence + feDisplacementMap` 做撕边，文字本身不变形 |
| 横线笔记本 | `.note` 表单 / 结果卡 | `repeating-linear-gradient` 画横线 + 红色页边线 + 打孔 |
| 粉色方格本（带线圈） | `.grid-note` | 双向网格渐变 + 顶部线圈 |
| 拍立得 | `.polaroid` 上传框 / 衣橱单品 | 白边 + 投影 + 黄色胶带 |
| 亮粉布料（锯齿剪边） | `.fabric` / 色卡 `.sw` | `conic-gradient` 遮罩做花边剪刀齿 + 织纹 |
| 半调网点 | 背景块、上传区底纹 | `radial-gradient` 点阵 |
| 蕾丝 | 背景装饰 | SVG pattern |
| 口红 / 粉饼 / 蝴蝶结 / 纽扣 / 星星 | `.sticker` 贴纸 | 白色描边 drop-shadow 做“剪贴”效果 |

> **素材建议**：mockup 里的贴纸是临时手绘 SVG。正式版建议从 Canva 原稿导出透明 PNG/WebP（口红、粉饼、蝴蝶结、草莓、墨镜、纽扣、帽子、鞋子、蕾丝、书页、格子手帕），还原度会高很多。

### 2.4 动效

- 页面切换：纸片轻微下落并回正（0.45s）。
- 按钮 / 标签悬停：像被手指按住，微微旋转并上浮。
- 卡片保持 ±1–2° 的随机倾斜，模拟手贴的感觉。
- 遵守 `prefers-reduced-motion`，用户开启后关闭全部动画。

---

## 3. 信息架构（对应 PPT「Low Fidelity Prototype」页）

```
Welcome ──► Sign up / Log in ──► Dashboard（上传）──► Analysis Results ──► Wardrobe Styler
                                     ▲                                        │
                                     └──────────── 添加衣物 ◄──────────────────┘
```

| 页面 | PPT 对应内容 | 主要模块 |
|---|---|---|
| **1. Welcome** | 封面 + Introduction + Welcome Page | 纸胶带大标题「“STAIL” Personal AI Stylist」、By Nanami & Clara、3 张功能卡（Color / Body Type / Wardrobe）、注册 / 登录笔记本卡 |
| **2. Dashboard（Upload）** | Dashboard | 3 个拍立得上传框（自拍 / 全身照 / 衣物）、**隐私同意卡**（来自 Ethical/Legal 页：用户同意、安全存储、GDPR & PDP）；勾选同意后才能点「Analyse me」 |
| **3. Analysis Results** | Analysis Results | 色彩季型 + 布料色卡（推荐色 / 避免色）、置信度条与「重新拍照」提示（来自 Limitations：准确度依赖照片质量）、体型卡 + 剪影、穿搭建议方格本 |
| **4. Wardrobe Styler** | Wardrobe Styler | 场合标签（Casual / Work / Date / Party / Travel）、我的衣橱（拍立得网格 + 添加）、AI 生成的 3 套搭配（每套附“为什么适合你”）、收藏 ♡ |

响应式：≥900px 为多栏拼贴布局；手机端改为单列，背景书页碎片隐藏，导航压缩为两行。已在 390px 宽度下验证，没有横向滚动。

---

## 4. 技术方案建议（待确认）

| 层 | 建议 | 理由 |
|---|---|---|
| 前端 | **Next.js（React）+ CSS Modules** | 材质组件直接用 mockup 里的 CSS 封装成 `<Tape>`、`<TornPaper>`、`<Polaroid>`、`<Notebook>`、`<Fabric>`、`<Sticker>` |
| 后端 / AI | **Python FastAPI** | 对应 PPT 的三个 AI 模块：Computer Vision（人脸 / 人体关键点、衣物识别）→ Classification（色彩季型、体型）→ Recommendation Engine（搭配生成） |
| 快速原型的替代方案 | 用多模态 LLM API 直接分析照片，输出 JSON | 不用自己训练模型，先把完整流程跑通 |
| 存储 | 用户照片加密存储，可一键删除 | 对应 Legal 页的承诺 |

---

## 5. 下一步

1. 确认视觉方向（对照 `mockup.html`）。
2. 确认技术栈，以及 AI 部分是做真实模型还是先用 LLM API 原型。
3. 从 Canva 导出贴纸素材。
4. 搭建项目骨架 → 组件库 → 4 个页面 → 接入 AI。

---

## 6. 快速演示版（demo v0.2）

`mockup.html` 发布为 Artifact 后，会通过 Artifact 的 `sample` 能力调用 Claude，照片分析是真实的。不需要后端，也不需要 API key，费用由打开页面的人的 Claude 账号承担，第一次调用时会先征求同意。

| 功能 | AI 可用时 | AI 不可用时（本地打开 / 未授权） |
|---|---|---|
| 自拍 → 色彩季型、推荐色和避免色、置信度 | Claude 读图后返回 JSON | 显示示例结果 |
| 全身照 → 体型和穿搭建议 | 同上 | 示例 |
| 衣物照 → 名称、类别、颜色 | 批量识别，生成缩略图放进衣橱 | 使用示例衣橱 |
| 场合 → 3 套搭配和理由 | 只用衣橱里已有的单品 | 本地随机组合 |

- 衣橱缩略图和分析结果只保存在当前浏览器（localStorage），点页脚的 “Reset demo” 可以清空。
- 更新线上版本：`python3 design/build-artifact.py <输出路径>`，然后发布到同一个链接。
