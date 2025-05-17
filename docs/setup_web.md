# Web‑Only Contribution Guide

> **Goal:** Enable anyone with just a browser (Windows 11, macOS, Linux, Chromebook) to contribute code, docs, CAD, or tests to **IonStar** without local installs or command‑line tools.

---

## 1. Fork & Clone in the Browser
1. Open the repo page and click **Fork** (top‑right).  
2. Inside your fork, press **.** (period) to launch **github.dev** (VS Code in the browser).  

## 2. Create / Edit Files
- Use the left sidebar to add folders: **Right‑click → New Folder**.  
- Add or edit files: **Right‑click → New File** or click any file to open the editor.  
- Auto‑save keeps drafts until you commit.

## 3. Commit Changes
1. Hit **Ctrl+Shift+G** (or click the Source Control icon).  
2. Type a clear commit message (one line).  
3. Click **Commit**.  
4. Click **… → Push** to send commits back to your fork.

## 4. Open a Pull Request
1. Return to the GitHub web UI.  
2. Click **Compare & Pull Request**.  
3. Fill in PR title + description.  
4. Submit. Maintainers review and merge.

## 5. CAD & PCB
- Upload `.step`, `.stl`, or KiCad files directly.  
- Preview 3D models in the browser using GitHub’s built‑in viewer.

## 6. Testing in the Cloud
- Small Python tests run via **GitHub Actions** (coming soon).  
- Hardware‑in‑loop sims triggered on PRs using public CI services.  

---

### Quick Tips
| Action | Shortcut |
|--------|----------|
| Open command palette | <kbd>F1</kbd> |
| Save file | <kbd>Ctrl+S</kbd> |
| Terminal (for Codespaces) | <kbd>Ctrl+`</kbd> |

---

**You’re ready—no local environment, no problem. Contribute anywhere, anytime.**
