"""
An example of extending the deck options screen with raw HTML/JS.
"""

from pathlib import Path

from aqt import gui_hooks
from aqt.webview import AnkiWebView


# def setup(webview: AnkiWebView) -> None:
#     webview.eval(Path(__file__).with_name("init.js").read_text(encoding="utf8"))


INIT_SCRIPT = """
(function(){{
    const script = document.createElement('script');
    script.innerHTML = `{script}`;
    document.body.appendChild(script);
}})();"""


def setup(webview: AnkiWebView) -> None:
    script = Path(__file__).with_name("init.js").read_text(encoding="utf8")
    webview.eval(INIT_SCRIPT.format(script=script))


gui_hooks.webview_did_inject_style_into_page.append(setup)
