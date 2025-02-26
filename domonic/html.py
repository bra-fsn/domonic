"""
    domonic.html
    ====================================

    Generate HTML using python.

"""
from domonic.dom import (
    DOMConfig,
    Comment,
    Document,  # HTMLOptionsCollection,
    DocumentType,
    Element,
    HTMLAnchorElement,
    HTMLAreaElement,
    HTMLAudioElement,
    HTMLBaseElement,
    HTMLBaseFontElement,
    HTMLBodyElement,
    HTMLBRElement,
    HTMLButtonElement,
    HTMLCanvasElement,
    HTMLContentElement,
    HTMLDataElement,
    HTMLDataListElement,
    HTMLDialogElement,
    HTMLDivElement,
    HTMLDListElement,
    HTMLDocument,
    HTMLElement,
    HTMLEmbedElement,
    HTMLFieldSetElement,
    HTMLFormControlsCollection,
    HTMLFormElement,
    HTMLFrameSetElement,
    HTMLHeadElement,
    HTMLHeadingElement,
    HTMLHRElement,
    HTMLIFrameElement,
    HTMLImageElement,
    HTMLInputElement,
    HTMLIsIndexElement,
    HTMLKeygenElement,
    HTMLLabelElement,
    HTMLLegendElement,
    HTMLLIElement,
    HTMLLinkElement,
    HTMLMapElement,
    HTMLMediaElement,
    HTMLMetaElement,
    HTMLMeterElement,
    HTMLModElement,
    HTMLObjectElement,
    HTMLOListElement,
    HTMLOptGroupElement,
    HTMLOptionElement,
    HTMLOutputElement,
    HTMLParagraphElement,
    HTMLParamElement,
    HTMLPictureElement,
    HTMLPreElement,
    HTMLProgressElement,
    HTMLQuoteElement,
    HTMLScriptElement,
    HTMLSelectElement,
    HTMLShadowElement,
    HTMLSourceElement,
    HTMLSpanElement,
    HTMLStyleElement,
    HTMLTableCaptionElement,
    HTMLTableCellElement,
    HTMLTableColElement,
    HTMLTableDataCellElement,
    HTMLTableElement,
    HTMLTableHeaderCellElement,
    HTMLTableRowElement,
    HTMLTableSectionElement,
    HTMLTemplateElement,
    HTMLTextAreaElement,
    HTMLTimeElement,
    HTMLTitleElement,
    HTMLTrackElement,
    HTMLUListElement,
    HTMLUnknownElement,
    HTMLVideoElement,
    Node,
    Text,
)
from domonic.webapi.url import URL

html_tags = [
    "figcaption",
    "blockquote",
    "textarea",
    "progress",
    "optgroup",
    "noscript",
    "fieldset",
    "datalist",
    "colgroup",
    "summary",
    "section",
    "details",
    "command",
    "caption",
    "article",
    "address",
    "submit",
    "strong",
    "source",
    "select",
    "script",
    "output",
    "option",
    "legend",
    "keygen",
    "iframe",
    "hgroup",
    "header",
    "footer",
    "figure",
    "canvas",
    "button",
    "video",
    "track",
    "title",
    "thead",
    "tfoot",
    "tbody",
    "table",
    "style",
    "small",
    "param",
    "meter",
    "label",
    "input",
    "audio",
    "aside",
    "applet",
    "object",
    "basefont",
    "center",
    "embed",
    "isindex",
    "listing",
    "menuitem",
    "plaintext",
    "strike",
    "template",
    "picture",
    "dialog",
    "data",
    "time",
    "span",
    "samp",
    "ruby",
    "meta",
    "menu",
    "mark",
    "link",
    "html",
    "head",
    "form",
    "font",
    "code",
    "cite",
    "body",
    "base",
    "area",
    "abbr",
    "main",
    "dir",
    "wbr",
    "var",
    "sup",
    "sub",
    "nav",
    "map",
    "kbd",
    "ins",
    "img",
    "div",
    "dfn",
    "del",
    "col",
    "bdo",
    "bdi",
    "pre",
    "xmp",
    "ul",
    "tr",
    "th",
    "td",
    "rt",
    "rp",
    "ol",
    "li",
    "hr",
    "h6",
    "h5",
    "h4",
    "h3",
    "h2",
    "h1",
    "em",
    "dt",
    "dl",
    "dd",
    "br",
    "u",
    "s",
    "q",
    "p",
    "i",
    "b",
    "a",
]
# big, blink, bold, tt, var, frameset

html_attributes = [
    "accept",
    "accesskey",
    "loading",
    "action",
    "align",
    "alt",
    "async",
    "autocomplete",
    "autofocus",
    "autoplay",
    "bgcolor",
    "border",
    "charset",
    "checked",
    "cite",
    "class",
    "color",
    "cols",
    "colspan",
    "content",
    "contenteditable",
    "controls",
    "coords",
    "data",
    "datetime",
    "default",
    "defer",
    "dir",
    "dirname",
    "disabled",
    "download",
    "draggable",
    "enctype",
    "for",
    "form",
    "formaction",
    "headers",
    "height",
    "hidden",
    "high",
    "href",
    "hreflang",
    "id",
    "ismap",
    "kind",
    "label",
    "lang",
    "list",
    "loop",
    "low",
    "max",
    "maxlength",
    "media",
    "method",
    "min",
    "multiple",
    "muted",
    "name",
    "novalidate",
    "onabort",
    "onafterprint",
    "onbeforeprint",
    "onbeforeunload",
    "onblur",
    "oncanplay",
    "oncanplaythrough",
    "onchange",
    "onclick",
    "oncontextmenu",
    "oncopy",
    "oncuechange",
    "oncut",
    "ondblclick",
    "ondrag",
    "ondragend",
    "ondragenter",
    "ondragleave",
    "ondragover",
    "ondragstart",
    "ondrop",
    "ondurationchange",
    "onemptied",
    "onended",
    "onerror",
    "onfocus",
    "onhashchange",
    "oninput",
    "oninvalid",
    "onkeydown",
    "onkeypress",
    "onkeyup",
    "onload",
    "onloadeddata",
    "onloadedmetadata",
    "onloadstart",
    "onmousedown",
    "onmousemove",
    "onmouseout",
    "onmouseover",
    "onmouseup",
    "onmousewheel",
    "onoffline",
    "ononline",
    "onpagehide",
    "onpageshow",
    "onpaste",
    "onpause",
    "onplay",
    "onplaying",
    "onpopstate",
    "onprogress",
    "onratechange",
    "onreset",
    "onresize",
    "onscroll",
    "onsearch",
    "onseeked",
    "onseeking",
    "onselect",
    "onstalled",
    "onstorage",
    "onsubmit",
    "onsuspend",
    "ontimeupdate",
    "ontoggle",
    "onunload",
    "onvolumechange",
    "onwaiting",
    "onwheel",
    "open",
    "optimum",
    "pattern",
    "placeholder",
    "poster",
    "preload",
    "readonly",
    "rel",
    "required",
    "reversed",
    "rows",
    "rowspan",
    "sandbox",
    "scope",
    "selected",
    "shape",
    "size",
    "sizes",
    "span",
    "spellcheck",
    "src",
    "srcdoc",
    "srclang",
    "srcset",
    "start",
    "step",
    "style",
    "tabindex",
    "target",
    "title",
    "translate",
    "type",
    "usemap",
    "value",
    "width",
    "wrap",
    "property",
    "integrity",
    "crossorigin",
    "nonce",
    "autocapitalize",
    "enterkeyhint",
    "inputmode",
    "is",
    "itemid",
    "itemprop",
    "itemref",
    "itemscope",
    "itemtype",
    "part",
    "slot",
    "spellcheck",
    "alink",
    "nowrap",
    "vlink",
    "vspace",
    "language",
    "clear",
    "hspace",
    "xmlns",
    "about",
    "allowtransparency",
    "datatype",
    "inlist",
    "prefix",
    "resource",
    "rev",
    "typeof",
    "vocab",  # rdfa
    "playsinline",
    "autopictureinpicture",
    "buffered",
    "controlslist",
    "disableremoteplayback",  # video
]


def render(inp, outp="", to=None):  # doctype='html5')
    """write the input to string or to a file.

    Args:
        inp (obj): A domonic tag. For example div()
        outp (str): An optional output filename
        to (str): An optional output type. if 'pyml' is specified then pyml is returned instead of html.

    Returns:
        str: A HTML rendered string
    """
    if to == "pyml":
        if outp != "":
            with open(outp, "w+") as f:
                f.write(inp.__pyml__())
        return inp.__pyml__()
    # else:
    if outp != "":
        with open(outp, "w+") as f:
            f.write(str(inp))
    return str(inp)


class TemplateError(IndexError):
    def __init__(self, error, message="TemplateError: "):
        """[raised when a template error occurs]

        Args:
            error ([type]): [the error]
            message (str, optional): [description]. Defaults to "Templating error: ".
        """
        self.error = error
        self.hint = ""
        print(self.error)
        if str(self.error) == "list index out of range":
            self.hint = "MISSING UNDERSCORE ON AN ATTRIBUTE"
        self.message = message + self.hint
        super().__init__(self.message)


tag = Node  # legacy support?. TODO - remove in future? 0.0.9


class closed_tag(Node):
    def __str__(self):
        if DOMConfig.RENDER_OPTIONAL_CLOSING_SLASH:
            if DOMConfig.SPACE_BEFORE_OPTIONAL_CLOSING_SLASH:
                return f"<{self.name}{self.__attributes__} />"
            else:
                return f"<{self.name}{self.__attributes__}/>"
        return f"<{self.name}{self.__attributes__}>"


html = type("html", (HTMLDocument,), {"name": "html"})
body = type("body", (HTMLBodyElement,), {"name": "body"})
head = type("head", (HTMLHeadElement,), {"name": "head"})
script = type("script", (HTMLScriptElement,), {"name": "script"})
style = type("style", (HTMLStyleElement,), {"name": "style"})
h1 = type("h1", (HTMLHeadingElement,), {"name": "h1"})
h2 = type("h2", (HTMLHeadingElement,), {"name": "h2"})
h3 = type("h3", (HTMLHeadingElement,), {"name": "h3"})
h4 = type("h4", (HTMLHeadingElement,), {"name": "h4"})
h5 = type("h5", (HTMLHeadingElement,), {"name": "h5"})
h6 = type("h6", (HTMLHeadingElement,), {"name": "h6"})
p = type("p", (HTMLParagraphElement,), {"name": "p"})

i = type("i", (Element,), {"name": "i"})  # TODO - check which?
b = type("b", (Element,), {"name": "b"})  # TODO - check which?
portal = type("portal", (Element,), {"name": "portal"})  # TODO - check which?


def Atag(self, *args, **kwargs):

    # print('Atag: ', args, kwargs)
    # Node.__init__(self, *args, **kwargs)
    # Element.__init__(self, *args, **kwargs)

    # TODO - fix BUG. this stops having no href on a tags
    if kwargs.get("_href", None) is not None:
        URL.__init__(self, url=kwargs["_href"])
    # else:
    # Node.__init__(*args, **kwargs)
    Element.__init__(self, *args, **kwargs)
    # Node.__init__(self, *args, **kwargs)
    # URL.__init__(self, *args, **kwargs)


def __update__(
    self, *args, **kwargs
):  # TODO - you removed this but where the unit test that you wrote it for in the first place?
    # print('__update__: ', args, kwargs)
    # URL.__update__(self)
    # TODO - fix BUG. this stops having no href on a tags
    if self.getattr("_href", None) is not None:
        self.kwargs["_href"] = self.href
    # Node.__init__(self, *args, **kwargs)
    # URL.__init__(self, *args, **kwargs)
    # self.__init__(*args, **kwargs)
    Element.__init__(self, *args, **kwargs)
    URL.__init__(self, *args, **kwargs)


a = type("a", (Element, URL), {"name": "a", "__init__": Atag})  # , "__update__": __update__})
ul = type("ul", (HTMLUListElement,), {"name": "ul"})
ol = type("ol", (HTMLOListElement,), {"name": "ol"})
li = type("li", (HTMLLIElement,), {"name": "li"})
div = type("div", (HTMLDivElement,), {"name": "div"})

strong = type("strong", (Element,), {"name": "strong"})  # TODO - check
blockquote = type("blockquote", (Element,), {"name": "blockquote"})  # TODO - check
table = type("table", (HTMLTableElement,), {"name": "table"})
tr = type("tr", (Element,), {"name": "tr"})
td = type("td", (Element,), {"name": "td"})
# form = type('form', (Element,), {'name': 'form'})


class form(Element):
    def __init__(self, *args, **kwargs):
        new_kwargs = {}
        for k, v in kwargs.items():
            if k[0] != "_":
                # print("WARNING: kwarg '{}' should begin with an underscore".format(k))
                new_kwargs[f"_{k}"] = v
            else:
                new_kwargs[k] = v
        kwargs = new_kwargs

        self.name = "form"
        Node.__init__(self, *args, **kwargs)
        Element.__init__(self, *args, **kwargs)

    @property
    def elements(self):
        kids = []
        for child in self.children:
            if isinstance(child, (button, fieldset, input, object, output, select, textarea)):
                kids.append(child)
        return kids


label = type("label", (Element,), {"name": "label"})
# label.__doc__ = '''
#                 .. highlight:: python
#                 .. code-block:: python

#                     # used to label form elements. i.e.
#                     label(_for=None, _text=None, **kwargs)
#                     # <label for=""></label>
#                 '''

submit = type("submit", (Element,), {"name": "submit"})
title = type("title", (HTMLTitleElement,), {"name": "title"})
noscript = type("noscript", (Element,), {"name": "noscript"})
section = type("section", (Element,), {"name": "section"})
nav = type("nav", (Element,), {"name": "nav"})
article = type("article", (Element,), {"name": "article"})
aside = type("aside", (Element,), {"name": "aside"})
hgroup = type("hgroup", (Element,), {"name": "hgroup"})
address = type("address", (Element,), {"name": "address"})
pre = HTMLPreElement  # type("pre", (Element,), {"name": "pre"})
dl = type("dl", (Element,), {"name": "dl"})
dt = type("dt", (Element,), {"name": "dt"})
dd = type("dd", (Element,), {"name": "dd"})
figure = type("figure", (Element,), {"name": "figure"})
figcaption = type("figcaption", (Element,), {"name": "figcaption"})
em = type("em", (Element,), {"name": "em"})
small = type("small", (Element,), {"name": "small"})
s = type("s", (Element,), {"name": "s"})
cite = type("cite", (Element,), {"name": "cite"})
q = type("q", (Element,), {"name": "q"})
dfn = type("dfn", (Element,), {"name": "dfn"})
abbr = type("abbr", (Element,), {"name": "abbr"})
code = type("code", (Element,), {"name": "code"})
var = type("var", (Element,), {"name": "var"})
samp = type("samp", (Element,), {"name": "samp"})
kbd = type("kbd", (Element,), {"name": "kbd"})
sub = type("sub", (Element,), {"name": "sub"})
sup = type("sup", (Element,), {"name": "sup"})
u = type("u", (Element,), {"name": "u"})
mark = type("mark", (Element,), {"name": "mark"})
ruby = type("ruby", (Element,), {"name": "ruby"})
rt = type("rt", (Element,), {"name": "rt"})
rp = type("rp", (Element,), {"name": "rp"})
bdi = type("bdi", (Element,), {"name": "bdi"})
bdo = type("bdo", (Element,), {"name": "bdo"})
span = type("span", (HTMLSpanElement,), {"name": "span"})
ins = type("ins", (Element,), {"name": "ins"})
iframe = type("iframe", (Element,), {"name": "iframe"})
video = type("video", (HTMLVideoElement,), {"name": "video"})
audio = type("audio", (HTMLAudioElement,), {"name": "audio"})
canvas = type("canvas", (HTMLCanvasElement,), {"name": "canvas"})
caption = type("caption", (Element,), {"name": "caption"})
colgroup = type("colgroup", (Element,), {"name": "colgroup"})
tbody = type("tbody", (Element,), {"name": "tbody"})
thead = type("thead", (Element,), {"name": "thead"})
tfoot = type("tfoot", (Element,), {"name": "tfoot"})
th = type("th", (Element,), {"name": "th"})
fieldset = type("fieldset", (HTMLFieldSetElement,), {"name": "fieldset"})  # type("fieldset", (Element,), {"name": "fieldset"})
legend = type("legend", (Element,), {"name": "legend"})
button = type("button", (HTMLButtonElement,), {"name": "button"})  # type("button", (Element,), {"name": "button"})
select = type("select", (HTMLSelectElement,), {"name": "select"})  # type("select", (Element,), {"name": "select"})
datalist = type("datalist", (HTMLDataListElement,), {"name": "datalist"})
optgroup = type("optgroup", (HTMLOptGroupElement,), {"name": "optgroup"})
option = type("option", (HTMLOptionElement,), {"name": "option"})
textarea = type("textarea", (HTMLTextAreaElement,), {"name": "textarea"})
output = type("output", (HTMLOutputElement,), {"name": "output"})
progress = type("progress", (HTMLProgressElement,), {"name": "progress"})
meter = type("meter", (HTMLMeterElement,), {"name": "meter"})
details = type("details", (Element,), {"name": "details"})
summary = type("summary", (Element,), {"name": "summary"})
menu = type("menu", (Element,), {"name": "menu"})
menuitem = type("menuitem", (Element,), {"name": "menuitem"})  # dead but may be used
font = type("font", (Element,), {"name": "font"})
header = type("header", (Element,), {"name": "header"})
footer = type("footer", (Element,), {"name": "footer"})
# map_ = type('map_', (tag,), {'name': 'map_'})
# object_ = type('object_', (tag,), {'name': 'object_'})
# del_ = type('del_', (tag,), {'name': 'del_'})

# time = HTMLTimeElement  # type('time', (tag,), {'name': 'time'})
data = type("data", (HTMLDataElement,), {"name": "data"})
samp = type("samp", (Element,), {"name": "samp"})

base = type("base", (HTMLBaseElement,), {"name": "base"})
link = type("link", (closed_tag, HTMLLinkElement), {"name": "link"})  # HTMLLinkElement TODO - closed tags
meta = type("meta", (closed_tag, HTMLMetaElement), {"name": "meta"})  # HTMLMetaElement TODO - closed tags
hr = type("hr", (closed_tag, HTMLHRElement), {"name": "hr"})
br = type("br", (closed_tag, HTMLBRElement,), {"name": "br"})
wbr = type("wbr", (closed_tag, Element), {"name": "wbr"})
img = type("img", (closed_tag, HTMLImageElement), {"name": "img"})  # HTMLImageElement TODO - closed tags
param = type("param", (closed_tag, HTMLParamElement), {"name": "param"})  # HTMLParamElement
source = type("source", (closed_tag, HTMLSourceElement), {"name": "source"})  # HTMLSourceElement
track = type("track", (closed_tag, HTMLTrackElement), {"name": "track"})  # HTMLTrackElement
area = type("area", (HTMLAreaElement,), {"name": "area"})
col = type("col", (closed_tag, HTMLTableColElement), {"name": "col"})  # HTMLTableColElement
input = type("input", (closed_tag, HTMLInputElement), {"name": "input"})  # HTMLInputElement  # TODO - closed tags
keygen = type("keygen", (closed_tag, HTMLKeygenElement), {"name": "keygen"})  # HTMLKeygenElement
command = type("command", (closed_tag, Element), {"name": "command"})

main = type("main", (Element,), {"name": "main"})

# obsolete
applet = type("applet", (Element,), {"name": "applet"})
# object = type('object', (Element,), {'name': 'object'})
basefont = type("basefont", (Element,), {"name": "basefont"})
center = type("center", (Element,), {"name": "center"})
# dir = type('dir', (Element,), {'name': 'dir'})
embed = type("embed", (HTMLEmbedElement,), {"name": "embed"})
isindex = type("isindex", (Element,), {"name": "isindex"})
listing = type("listing", (Element,), {"name": "listing"})
plaintext = type("plaintext", (Element,), {"name": "plaintext"})
s = type("s", (Element,), {"name": "s"})
u = type("u", (Element,), {"name": "u"})
strike = type("strike", (Element,), {"name": "strike"})
xmp = type("xmp", (Element,), {"name": "xmp"})

template = type("template", (Element,), {"name": "template"})

picture = type("picture", (HTMLPictureElement,), {"name": "picture"})
dialog = type("dialog", (HTMLDialogElement,), {"name": "dialog"})


# legacy.
doctype = type("doctype", (DocumentType,), {"name": "doctype"})
comment = type("comment", (Comment,), {"name": "comment"})


def create_element(name="custom_tag", *args, **kwargs):
    """
    A method for creating custom tags

    tag name needs to be set due to custom tags with hyphens can't be classnames.
    i.e. hypenated tags <some-custom-tag></some-custom-tag>
    """
    # checks if already exists
    if name in html_tags:
        return globals()[name](*args, **kwargs)

    # NOTE: we care calling it custom_tag because it can't have hyphens
    custom_tag = type("custom_tag", (Element,), {"name": name})
    new_tag = custom_tag(*args, **kwargs)
    new_tag.name = name
    return new_tag
