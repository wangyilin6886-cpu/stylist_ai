"""Build a publishable single-file page from mockup.html.

Strips the document wrapper (the artifact host adds its own) and the local
@font-face fallbacks (the page loads the same fonts from Google Fonts).
Usage: python3 build-artifact.py OUT.html
"""
import re, sys, pathlib

src = pathlib.Path(__file__).with_name("mockup.html").read_text()
src = re.sub(r"<!DOCTYPE html>\s*|</?html[^>]*>\s*|</?head>\s*|</?body>\s*|<meta [^>]*>\s*", "", src)
src = re.sub(r"@font-face\{[^}]*Local'[^}]*\}\n", "", src)
pathlib.Path(sys.argv[1]).write_text(src)
