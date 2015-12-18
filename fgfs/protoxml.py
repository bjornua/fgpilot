from xml.etree import ElementTree

from pprint import pprint


def fileLineIter(inputFile,
                 inputNewline="\n",
                 outputNewline=None,
                 readSize=8192):

    if outputNewline is None:
        outputNewline = inputNewline

    partialLine = ''
    while True:
        charsJustRead = inputFile.read(readSize)
        if not charsJustRead:
            break

        partialLine += charsJustRead
        lines = partialLine.split(inputNewline)
        partialLine = lines.pop()

        for line in lines:
            yield line + outputNewline

    if partialLine:
        yield partialLine


def parseXML(xml):
    tr = ElementTree.fromstring(xml)

    o = tr.find('generic').find('output')

    var_separator = o.find('var_separator').text
    if var_separator == 'newline':
        var_separator = '\n'

    line_separator = o.find('line_separator').text
    if line_separator == 'newline':
        line_separator = '\n'

    labels = (c.find('node').text for c in o.findall('chunk'))

    labels = list(labels)

    return (line_separator, var_separator, labels)


def parse_value(a):
    if a[0] == '-':
        b = a[1:]
    else:
        b = a

    if b.isdigit():
        return int(a)

    pieces = b.split(".")
    if len(pieces) == 2 and all(p.isdigit() for p in pieces):
        return float(a)

    return a

def parse_input_stream(stream, line_separator, var_separator, labels):
    s = fileLineIter(inputFile=stream, inputNewline=line_separator, readSize=1)

    for line in s:
        columns = line.split(var_separator)

        columns = (parse_value(v) for v in columns)

        yield dict(zip(labels, columns))


def make_reader(protoFile, stream):
    line_separator, var_separator, labels = parseXML(open(protoFile, 'r').read())

    parser = parse_input_stream(stream, line_separator, var_separator, labels)

    for x in parser:
        yield x