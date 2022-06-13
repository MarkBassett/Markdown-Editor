import os
formatters = {'plain': ['', '', ''],
              'bold': ['**', '**', ''],
              'italic': ['*', '*', ''],
              'header': ['#', '', '/n'],
              'link':['[]', '[]'],
              'inline-code': ['`', '`', ''],
              'new-line': ['', '', '/n'],
              'ordered-list': [],
              'unordered-list': []}

ask_for_input = True
markdown_text = ''
while ask_for_input:
    choose_formatter = input('Choose a formatter: > ')
    if choose_formatter == '!help':
        for format in formatters:
            print(format)
        print('Special commands: !help !done')
    elif choose_formatter == '!done':
        ask_for_input = False
    elif choose_formatter not in formatters:
        print('Unknown formatting type or command')
    else:
        if choose_formatter == 'header':
            level = 7
            while level < 1 or level > 6:
                level = int(input('Level: '))
                if level < 1 or level > 6:
                    print('The level should be within the range of 1 to 6')
            text = input('Text: ')
            formated_text = level * '#' + ' ' + text + '\n'
        elif choose_formatter == 'link':
            label = input('Label: ')
            url = input('URL: ')
            formated_text = f'[{label}]({url})'
        elif choose_formatter == 'new-line':
            formated_text = '\n'
        elif choose_formatter == 'ordered-list' or choose_formatter == 'unordered-list':
            rows = -2
            while rows < 1:
                rows = int(input('Number of rows: '))
                if rows <= 0:
                    print('The number of rows should be greater than zero')
            formated_text = ''
            for row in range(1, rows + 1):
                list_element = input(f'Row #{row}: ')
                if choose_formatter == 'ordered-list':
                    formated_element = f'{row}. {list_element}\n'
                else:
                    formated_element = f'* {list_element}\n'
                formated_text += formated_element

        else:
            text = input('Text: ')
            formated_text = f'{formatters[choose_formatter][0]}{text}{formatters[choose_formatter][1]}{formatters[choose_formatter][2]}'
        markdown_text += formated_text
        print(markdown_text)

with open('output.md', 'w') as output:
    markdown = output.write(markdown_text)

