---
name: compile-latex
description: Compile a LaTeX pdf with XeLaTeX. Use when compiling homework.
argument-hint: "[filename without .tex extension]"
allowed-tools: ["Read", "Bash", "Glob"]
---

# Compile LaTeX 

## Steps
1. **compile**
  - `xelatex -output-directory=outputs yourfile.tex`
  - Take a look at `templates` folder before output the final homework `[filename].tex` file

2. **Check for warnings:**
   - Grep output for `Overfull \\hbox` warnings
   - Grep for `undefined citations` or `Label(s) may have changed`
   - Report any issues found

3. **Open the PDF** for visual verification:
   ```bash
   open Slides/$ARGUMENTS.pdf          # macOS
   # xdg-open Slides/$ARGUMENTS.pdf    # Linux
   ```

4. **Report results:**
   - Compilation success/failure
   - Number of overfull hbox warnings
   - Any undefined citations
   - PDF page count

## Important
- **Always use XeLaTeX**, never pdflatex