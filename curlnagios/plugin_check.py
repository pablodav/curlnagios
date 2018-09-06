# plugin_check.py file with classes or functions to collect data or format messages
# This is just an example class from healthMonitor
import json
import subprocess

class curlCheck:
    def __init__(self, URL, extra_args):
        """
        :param URL: provide url to get/put data.
        :param extra_args: any argument for curl command
        """
        self.url = URL
        self.extra_args = extra_args
        
        self.std_args = '''" {\\"response_code\\": \\"%{http_code}\\",
        \\"dns_time\\": \\"%{time_namelookup}\\",
        \\"connect_time\\": \\"%{time_connect}\\",
        \\"pretransfer_time\\": \\"%{time_pretransfer}\\",
        \\"starttransfer_time\\": \\"%{time_starttransfer}\\",
        \\"total_time\\": \\"%{time_total}\\"
        "} '''

    def collect_data(self):
        """

        return: tuple
        returncode, return output, dict output with info ex:
        {'pretransfer_time': '0.000', 
        'response_code': '200', 
        'starttransfer_time': '0.182', 
        'dns_time': '0.000', 
        'connect_time': '0.000', 
        'total_time': '0.249'}
        """
        ### some code here
        ### or calling external modules
        cmdline = "curl {} --fail -s -o /dev/null {} -w \\ {}".format(self.url, self.extra_args, self.std_args)

        retrcode, retroutput = subprocess.getstatusoutput(cmdline)
        jsonoutput = json.loads(retroutput)
        return retrcode, retroutput, jsonoutput
    
    def format_perfdata(self):

        perfdata = ''
        returntuple = self.collect_data()

        for k, v in returntuple[2].items():
            # Simple format once we implement  warn;crit;min;max
            # 'label'=value[UOM];[warn];[crit];[min];[max] 
            perfdata += '{}={};;;; '.format(k, v)
        
        return perfdata
