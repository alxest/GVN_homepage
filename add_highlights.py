import argparse

def interpret_lines(lines):
    result = []
    for line in lines:
        for item in line.split(','):
            values = item.split('-')

            if len(values) == 1:
                result.append(int(values[0]))
            else:
                result.extend(range(int(values[0]), int(values[1]) + 1))
    return sorted(set(result))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add highlights to GitHub-generated html.')
    parser.add_argument('--color', nargs=1)
    parser.add_argument('--filename', nargs=1)
    parser.add_argument('lines', metavar='lines', type=str, nargs='+',
                        help='lines to highlight')
    args = parser.parse_args()

    color = args.color[0]
    filename = args.filename[0]
    lines = interpret_lines(args.lines)

    with open(filename, 'r') as content_file:
        content = content_file.read()

    content = content.replace('<script ', '<!-- <script ')
    content = content.replace('</script>', '</script> -->')

    for line in lines:
        old = "<td id=\"LC{0}\"".format(line)
        new = "{0} style=\"background-color: {1};\"".format(old, color)
        content = content.replace(old, new)

    with open(filename, 'w') as content_file:
        content_file.write(content)
