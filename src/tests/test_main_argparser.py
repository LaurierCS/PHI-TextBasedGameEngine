from main import parser

def test_parser_validate():
    args = ['game', '--validate']
    result = parser.parse_args(args)
    assert result.game == 'game'
    assert result.validate is True
    assert result.binary is False
    assert result.compile is None

def test_parser_binary():
    args = ['game', '--binary']
    result = parser.parse_args(args)
    assert result.game == 'game'
    assert result.validate is False
    assert result.binary is True
    assert result.compile is None

def test_parser_compile():
    args = ['game', '--compile', 'filename']
    result = parser.parse_args(args)
    assert result.game == 'game'
    assert result.validate is False
    assert result.binary is False
    assert result.compile is 'filename'

