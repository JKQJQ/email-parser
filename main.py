
def remove_spaces(str):
    return ''.join([ch for ch in str if ch != ' '])


d = dict()

with open("input.txt") as in_file:
    for line in in_file:
        line = remove_spaces(line.strip())
        if line.find('Trade') == -1 or line.find('channel') == -1 or line.find('Exchange') == -1:
            continue

        idx = line.find(':')
        channel = line[:idx]
        line = line[idx+2:]

        idx = line.find(':')
        trader = line[:idx]
        line = line[idx+1:]

        idx = line.find('-')
        trader_port = line[:idx]
        line = line[idx+1:]

        idx = line.find(':')
        exchange = line[:idx]
        line = line[idx+1:]

        idx = line.find(']')
        exchange_port = line[:idx]

        d[channel] = {
            trader: trader_port,
            exchange: exchange_port
        }

import pprint
pprint.pprint(d)

# format for each script

with open('output.txt', 'w') as out_file:
    out_file.write("############ Trader1 start-server.sh ##########\n")
    out_file.write('# Trade1@Trade1->Exchange1\n')
    out_file.write('LISTEN_PORT_1={}\n'.format(d['channel1']['Trade1']))
    out_file.write('LISTEN_PORT_2={}\n'.format(d['channel2']['Trade1']))
    out_file.write('LISTEN_PORT_3={}\n'.format(d['channel3']['Trade1']))
    out_file.write('\n')
    out_file.write('# Trade1@Trade1->Exchange2\n')
    out_file.write('LISTEN_PORT_4={}\n'.format(d['channel4']['Trade1']))
    out_file.write('LISTEN_PORT_5={}\n'.format(d['channel5']['Trade1']))
    out_file.write('LISTEN_PORT_6={}\n'.format(d['channel6']['Trade1']))
    out_file.write('\n\n')

    out_file.write("############# Trader2 start-server.sh ##############\n")
    out_file.write('# Trade2@Trade2->Exchange1\n')
    out_file.write('LISTEN_PORT_1={}\n'.format(d['channel7']['Trade2']))
    out_file.write('LISTEN_PORT_2={}\n'.format(d['channel8']['Trade2']))
    out_file.write('LISTEN_PORT_3={}\n'.format(d['channel9']['Trade2']))
    out_file.write('\n')
    out_file.write('# Trade2@Trade2->Exchange2\n')
    out_file.write('LISTEN_PORT_4={}\n'.format(d['channel10']['Trade2']))
    out_file.write('LISTEN_PORT_5={}\n'.format(d['channel11']['Trade2']))
    out_file.write('LISTEN_PORT_6={}\n'.format(d['channel12']['Trade2']))
    out_file.write('\n\n')

    out_file.write("############# Exchange1 start-server.sh ##############\n")
    out_file.write('# Trade1->Exchange1\n')
    out_file.write('# Trade1\n')
    out_file.write('SERVER_PORT_1={}\n'.format(d['channel1']['Trade1']))
    out_file.write('SERVER_PORT_2={}\n'.format(d['channel2']['Trade1']))
    out_file.write('SERVER_PORT_3={}\n'.format(d['channel3']['Trade1']))
    out_file.write('# Exchange1\n')
    out_file.write('LOCAL_PORT_1={}\n'.format(d['channel1']['Exchange1']))
    out_file.write('LOCAL_PORT_2={}\n'.format(d['channel2']['Exchange1']))
    out_file.write('LOCAL_PORT_3={}\n'.format(d['channel3']['Exchange1']))
    out_file.write('\n')
    out_file.write('# Trade2->Exchange1\n')
    out_file.write('# Trade2\n')
    out_file.write('SERVER_PORT_4={}\n'.format(d['channel7']['Trade2']))
    out_file.write('SERVER_PORT_5={}\n'.format(d['channel8']['Trade2']))
    out_file.write('SERVER_PORT_6={}\n'.format(d['channel9']['Trade2']))
    out_file.write('# Exchange1\n')
    out_file.write('LOCAL_PORT_4={}\n'.format(d['channel7']['Exchange1']))
    out_file.write('LOCAL_PORT_5={}\n'.format(d['channel8']['Exchange1']))
    out_file.write('LOCAL_PORT_6={}\n'.format(d['channel9']['Exchange1']))
    out_file.write('\n\n')

    out_file.write("############# Exchange2 start-server.sh ##############\n")
    out_file.write('# Trade1->Exchange2\n')
    out_file.write('# Trade1\n')
    out_file.write('SERVER_PORT_1={}\n'.format(d['channel4']['Trade1']))
    out_file.write('SERVER_PORT_2={}\n'.format(d['channel5']['Trade1']))
    out_file.write('SERVER_PORT_3={}\n'.format(d['channel6']['Trade1']))
    out_file.write('# Exchange2\n')
    out_file.write('LOCAL_PORT_1={}\n'.format(d['channel4']['Exchange2']))
    out_file.write('LOCAL_PORT_2={}\n'.format(d['channel5']['Exchange2']))
    out_file.write('LOCAL_PORT_3={}\n'.format(d['channel6']['Exchange2']))
    out_file.write('\n')
    out_file.write('# Trade2->Exchange2\n')
    out_file.write('# Trade2\n')
    out_file.write('SERVER_PORT_4={}\n'.format(d['channel10']['Trade2']))
    out_file.write('SERVER_PORT_5={}\n'.format(d['channel11']['Trade2']))
    out_file.write('SERVER_PORT_6={}\n'.format(d['channel12']['Trade2']))
    out_file.write('# Exchange2\n')
    out_file.write('LOCAL_PORT_4={}\n'.format(d['channel10']['Exchange2']))
    out_file.write('LOCAL_PORT_5={}\n'.format(d['channel11']['Exchange2']))
    out_file.write('LOCAL_PORT_6={}\n'.format(d['channel12']['Exchange2']))

