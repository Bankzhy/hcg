# HCG Evaluation Dataset

This directory contains the source-code files used in the HCG developer
evaluation. The samples were selected from the CodeSearchNet dataset and
prepared as short, standalone inputs for interactive code-graph analysis.

## Structure

- `developer_01` to `developer_10`: one folder for each evaluator
- 60 source files in each evaluator folder
- 20 Java, 20 Python, and 20 JavaScript files per evaluator
- 600 assignments in total

Some samples intentionally appear in two evaluator folders for cross-review.
The overlap mapping is withheld from evaluators.

## Use with HCG

1. Download this repository as a ZIP file and extract it.
2. In HCG, open the **Files** tab and select **Import Folder**.
3. Select only the `developer_XX` folder assigned to you.
4. Use the 60 imported files for the evaluation.

Do not rename, edit, or delete the original files during the evaluation. If a
task requires making code incomplete, restore the code before continuing.

## Source

The code samples are derived from
[CodeSearchNet](https://github.com/github/CodeSearchNet). Refer to the upstream
dataset and original repositories for source-specific licensing information.
