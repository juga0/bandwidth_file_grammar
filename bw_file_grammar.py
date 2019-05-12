#!/usr/bin/env python3
from lark import Lark

grammar_key = r"""
    keyvalue: KEY "=" VALUE
    headerline: keyvalue NL
    timestampline: INT NL
    header: timestampline [headerline*]
    relayline: keyvalue [(SP keyvalue)*] NL
    relaylines: relayline+
    bandwidthfile: header [TERMINATOR] [relaylines]

    INT: ("0".."9")+
    CR : /\r/
    LF : /\n/
    NL: (CR? LF)+
    SP : " "
    KEY : (KEYWORDCHAR | "_")+
    KEYWORD: KEYWORDCHAR+
    KEYWORDCHAR: "a".."z" | "A".."Z" | "-" | "0".."9"
    VALUE: ARGUMENTCHAR+
    ARGUMENTCHAR: "a".."z" | "A".."Z" | "-" | "0".."9"
    TERMINATOR: "=====" | "===="
"""

grammar_keyword = r"""
    keyvalue: KEYWORD "=" VALUE
    headerline: keyvalue NL
    timestampline: INT NL
    header: timestampline [headerline*]
    relayline: keyvalue [(SP keyvalue)*] NL
    relaylines: relayline+
    bandwidthfile: header [TERMINATOR] [relaylines]

    INT: ("0".."9")+
    CR : /\r/
    LF : /\n/
    NL: (CR? LF)+
    SP : " "
    KEY : (KEYWORDCHAR | "_")+
    KEYWORD: KEYWORDCHAR+
    KEYWORDCHAR: "a".."z" | "A".."Z" | "-" | "0".."9"
    VALUE: ARGUMENTCHAR+
    ARGUMENTCHAR: "a".."z" | "A".."Z" | "-" | "0".."9"
    TERMINATOR: "=====" | "===="
"""

def main():
    # Using KEY
    bw_file_parser = Lark(grammar_key, start='bandwidthfile')

    text = '92849238\nbw=1 node_id=A\n'
    print(bw_file_parser.parse(text).pretty())

    # Using KEYWORD
    bw_file_parser = Lark(grammar_keyword, start='bandwidthfile')

    text = '92849238\nbw=1 node_id=A\n'
    print(bw_file_parser.parse(text).pretty())

if __name__ == '__main__':
    main()
