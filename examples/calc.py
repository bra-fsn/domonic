# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, "..")

from domonic.javascript import Math
from domonic.html import *

classless_css = link(_rel="stylesheet", _href="https://unpkg.com/marx-css/css/marx.min.css")
jquery = script(_src="https://code.jquery.com/jquery-3.5.1.min.js")

code = script(
    """
	function add(){
		$('#results').html( Number($('#a').val()) + Number($('#b').val()) )};
"""
)

calc = article(
    div(
        label("Add numbers:"),
        input(_id="a"),
        span("+"),
        input(_id="b"),
        button("Calculate", _id="calculate_button", _onclick="add();"),
        div("Result:", div(_id="results")),
    )
)

mycalc = html(head(classless_css, jquery, code), body(calc))

render(f"{mycalc}", "calc.html")

try:
    import os
    import webbrowser

    webbrowser.open("file://" + os.path.realpath(".") + "/calc.html")
except Exception as e:
    print("view calc.html in the browser")
    pass

# // TODO - serve

# from domonic.terminal import ls, touch
# import time
# ls( "| open .")
# touch( "1.hi")
# time.sleep(1)
# touch( "2.how")
# time.sleep(1)
# touch( "3.are")
# time.sleep(1)
# touch( "4.you")
