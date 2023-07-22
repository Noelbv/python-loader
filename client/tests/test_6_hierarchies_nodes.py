import pytest
from click.testing import CliRunner
from cli import cli

def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()
    return content

def test_cli():
    runner = CliRunner()
    # Reset DB and add some tagsets
    runner.invoke(cli, ['reset'], input="y\n")
    runner.invoke(cli, ['add', 'tagset', 'Location'])          # Alphanumerical
    runner.invoke(cli, ['add', 'tagset', 'TimeStamp', '2'])    # Timestamp format YYYY-MM-dd hh:mm:ss
    runner.invoke(cli, ['add', 'tagset', 'Time', '3'])         # Time format hh:mm:ss  
    runner.invoke(cli, ['add', 'tagset', 'Date', '4'])         # Date format YYYY-MM-dd
    runner.invoke(cli, ['add', 'tagset', 'Resolution', '5'])   # Numerical
    # Add some tags
    runner.invoke(cli, ['add', 'tag', '1', '1', 'Iceland'])     # ID : 1
    runner.invoke(cli, ['add', 'tag', '1', '1', 'Reykjavik'])   # ID : 2
    runner.invoke(cli, ['add', 'tag', '1', '1', '101'])         # ID : 3
    runner.invoke(cli, ['add', 'tag', '1', '1', 'Iceland'])     # ID : 4
    runner.invoke(cli, ['add', 'tag', '1', '1', 'Hella'])       # ID : 5
    runner.invoke(cli, ['add', 'tag', '1', '1', 'Norway'])      # ID : 6
    runner.invoke(cli, ['add', 'tag', '1', '1', 'Oslo'])        # ID : 7

    # Add the medias
    runner.invoke(cli, ['add', 'media', './testfiles'])

    # Test 'getters' with empty table
    result = runner.invoke(cli, ['get', 'hierarchies'])
    assert result.output.strip() == ""

    result = runner.invoke(cli, ['get', 'hierarchy', '1'])
    assert result.output.strip() == "{'Error': 'could not retrieve hierarchy with the given id'}"

    result = runner.invoke(cli, ['get', 'node', '1'])
    assert result.output.strip() == "{'Error': 'could not find node with given ID'}"

    result = runner.invoke(cli, ['get', 'child-nodes', '1'])
    assert result.output.strip() == ""

    result = runner.invoke(cli, ['get', 'nodes-of-hierarchy', '1'])
    assert result.output.strip() == ""


    # Add hierarchies
    result = runner.invoke(cli, ['add', 'hierarchy', 'Geography', '1'])
    assert result.output.strip() == """id: 1
name: "Geography"
tagsetId: 1"""

    result = runner.invoke(cli, ['add', 'hierarchy', '"Days of week"', '4'])
    assert result.output.strip() == """id: 2
name: \"Days of week\"
tagsetId: 4"""

    # Add nodes
    result = runner.invoke(cli, ['add', 'node', '1', '1'])
    assert result.output.strip() == """id: 1
name: "Geography"
tagsetId: 1"""

if __name__ == '__main__':
    test_cli()
