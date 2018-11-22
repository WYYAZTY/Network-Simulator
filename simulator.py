from router import *
from link import *
from host import *
from node import *
from flow import *
import heapq
import event_type
import global_var
import global_consts



class Simulator(object):
    def __init__(self):
        self.node = {}
        self.links = {}
        self.flow = {}

    def run(self):
        node, links = self.build_graph('test0.txt')
        flows = self.read_flow('flows.txt', node)
        print(node)
        print(links)
        H1 = node['H1']
        H2 = node['H2']

        f = flows['F1']

        #flow = self.import_flow()

        # deal with the flow, add event to queue
        #for f in flow:
        event_temp = event_type.FlowInitialize(f, f.start_time)
        heapq.heappush(global_var.queue, event_temp)
        # print(global_var.queue)
        
        while global_var.queue:
            event = heapq.heappop(global_var.queue)
            global_var.timestamp = event.start_time
            event.action()

    def import_flow(self):
        return self

    def build_graph(self, file_name):
        data = [line.strip('\n') for line in open(file_name, 'r')]
        i = 1
        node = {}
        links = {}

        # print(data)
        # read host
        while i < len(data) and data[i] != '#':
            cur = data[i].split('\t')
            node[cur[0]] = Host(cur[1])
            i += 1
        i += 1

        # read router
        while i < len(data) and data[i] != '#':
            cur = data[i].split('\t')
            node[cur[0]] = Router(cur[0])
            i += 1
        i += 1

        # read link
        while i < len(data) and data[i] != '#':
            cur = data[i].split('\t')
            links[cur[0]] = Link(cur[0], float(cur[1]), float(cur[2])*(10**-3), float(cur[3]), None, None)
            links[cur[0] + '*'] = Link(cur[0] + '*', float(cur[1]), float(cur[2])*(10**-3), float(cur[3]), None, None)
            i += 1
        i += 1

        # read graph
        while i < len(data) and data[i] != '#':
            cur = data[i].split('\t')
            # specify the link from A to B
            print(cur)
            node[cur[1]].outgoing_links.append(links[cur[0]])
            node[cur[2]].incoming_links.append(links[cur[0]])
            links[cur[0]].start = node[cur[1]]
            links[cur[0]].end = node[cur[2]]

            # specify the link from B to A
            node[cur[1]].incoming_links.append(links[cur[0] + '*'])
            node[cur[2]].outgoing_links.append(links[cur[0] + '*'])
            links[cur[0] + '*'].start = node[cur[2]]
            links[cur[0] + '*'].end = node[cur[1]]
            i += 1
        return node, links

    def read_flow(self, file_name, node):
        data = [line.strip('\n') for line in open(file_name, 'r')]
        #print(data)
        flows = {}
        i = 0
        while i < len(data):
            cur = data[i].split('\t')
            print(cur)
            flows[cur[0]] = Flow(cur[0], node[cur[1]], node[cur[2]], float(cur[3]), float(cur[4]), global_consts.PACKETSIZE)
            node[cur[1]].flows[cur[0]] = flows[cur[0]]
            i += 1
        return flows