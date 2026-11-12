project = "TBtoFHIR"
copyright = "2026, SPHERES OUCRU-ID"
author = "SPHERES OUCRU-ID"
release = "2.0.0"

extensions = [
    "myst_parser",
    "sphinxcontrib.mermaid",
]

myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 3
myst_fence_as_directive = ["mermaid"]

exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = f"TBtoFHIR {release} documentation"

linkcheck_ignore = [r"https://academic\.oup\.com/.*"]
linkcheck_anchors_ignore_for_url = [r"https://github\.com/.*"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
