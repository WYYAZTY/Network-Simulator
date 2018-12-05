import matplotlib.pyplot as plt
from link import *
from router import *
from simulator import *

class Visulization(object):
    def __init__(self, links):
        self.links = links

    def plot_link_buffer_usage(self):

        print("================================")

        plt.figure(figsize=(16, 16))
        plt.suptitle('Link_Buffer_Usage', fontsize=12)
        prefix = 610
        i = 1
        for linkid, link in self.links.items():
            if linkid[-1] != '*':
                plt.subplot(prefix+i)
                plt.scatter(link.plot_link_buffer_time, link.plot_link_buffer, s=3)
                plt.xlabel('time(s)')
                plt.ylabel(linkid + '_Buffer / KB')
                i += 1
        plt.show()

        plt.figure(figsize=(16, 16))
        plt.suptitle('Link_Rate', fontsize=12)
        prefix = 610
        i = 1
        for linkid,link in self.links.items():
            if linkid[-1] != '*':
                plt.subplot(prefix+i)
                plt.scatter(global_var.plot_link_rate_time_axis, link.plot_link_rate, s=3)
                #plt.plot(global_var.plot_link_rate_time_axis, link.plot_link_rate)
                plt.xlabel('time(s)')
                plt.ylabel(linkid + ' / Mbps')
                i += 1
        plt.show()



        # plt.figure(figsize=(16, 16))
        # plt.subplot(211)
        # plt.scatter(self.links['L1'].plot_link_buffer_time, self.links['L1'].plot_link_buffer, s=3)
        # plt.scatter(self.links['L2'].plot_link_buffer_time, self.links['L2'].plot_link_buffer, s=3)
        # plt.xlabel('time(s)')
        # plt.ylabel('_Buffer / KB')
        # plt.show()
        # plt.subplot(212)
        # plt.scatter(global_var.plot_link_rate_time_axis, self.links['L1'].plot_link_rate, s=3)
        # plt.scatter(global_var.plot_link_rate_time_axis, self.links['L2'].plot_link_rate, s=3)
        # plt.xlabel('time(s)')
        # plt.ylabel(' / Mbps')
        # plt.show()


