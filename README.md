# 🧠 ModelForge Fusion Suite v16

> “If Stable Diffusion had a command center... this would be it.”

The **ModelForge Fusion Suite** is a no-compromise, all-in-one extension for Stable Diffusion WebUI (AUTOMATIC1111) — built to **merge models**, **stack LoRAs**, **run parallel workflows**, and now... **self-heal with embedded AI**.

![banner](assets/banner.png)

## ⚙️ What It Does

| Core System                      | Function                                                                 |
|----------------------------------|--------------------------------------------------------------------------|
| 🔀 Model Merger                  | Combine `.ckpt`, `.safetensors`, `.pt` models with live weight controls |
| 🎼 LoRA Composer + Splitter      | Blend or deconstruct LoRAs — experiment like a pro                      |
| 🧠 Dual-Stream Trainer           | Train face + body separately, merge weights on completion               |
| ⚡ Parallel Merge Engine         | Multi-threaded batch merging (max out your CPU)                         |
| 🎛 10x Workflow Manager          | Build and test up to 10 prompt+model pipelines side-by-side             |
| 🖼 Real-Time txt2img Generation  | Full image generation via WebUI API — per workflow                      |
| 📊 Output Grid Comparison        | Preview all 10 results instantly in a unified panel                     |
| 🤖 AI Error Auto-Fixer           | Monitors for crashes, auto-heals problems (missing deps, model fails)   |
| 🌐 Webhook + Fix History         | Sends reports and logs every automated fix attempt                      |

## 🧩 Addon Modules Included

- ✅ LoRA Stacker
- ✅ Smart Merge Visualizer
- ✅ Prompt Relay Engine
- ✅ AutoTagger (stub)
- ✅ Workflow Optimizer
- ✅ Web Dashboard (stub)

## 📦 Install Instructions

```bash
git clone https://github.com/YOUR_USERNAME/ModelForgeFusionSuite.git
mv ModelForgeFusionSuite stable-diffusion-webui/extensions/
```

## 🛡️ Requirements

- Python 3.10
- torch >= 2.1.x
- AUTOMATIC1111 WebUI
- API enabled on http://127.0.0.1:7860

## 📂 Structure

ModelForgeFusionSuite/
├── core/
├── outputs/
│   └── workflow_compare/
├── assets/
│   └── banner.png
├── fix_history.log
├── README.md

## 📡 Webhook Reporting

```json
{
  "error": "AttributeError: 'NoneType' object has no attribute 'cond_stage_model'",
  "fix_result": "✅ Model reloaded.",
  "timestamp": "2025-05-12T16:30:00"
}
```

---

MIT License — Use. Fork. Fuse. Evolve.
