import typing
import os


def read_requested_flow_file(path:str):
    
    fullpath = os.getcwd()+str('/firstapp/management/handler/flowfiles/') + str(path)
    with open(fullpath, 'r') as f:
        lines = f.readlines()
    return lines
    
def group_meter_items(file_lines):
    '''
    Assuming the flow file has always the same structure
    '''
    meter_group, items_of_meter = dict(), dict()
    subMeterReading = False
    for line in range(len(file_lines[1:-1])):
        # if we had a meter with two register-readings we skip
        if subMeterReading:
            subMeterReading = False
            continue
        # handling '|' delimiters and omit '/n' strings
        line_of_flow_file = file_lines[line].split('|')[:-1]
        if line_of_flow_file[0] == '026':
            mpanCore = line_of_flow_file[1]
            meter_group[mpanCore] = ''
        if line_of_flow_file[0] == '028':
            items_of_meter['meterId'] = [line_of_flow_file[1]]
        if line_of_flow_file[0] == '030':
            items_of_meter['meterRegisterId'] = [line_of_flow_file[1]]
            items_of_meter['readingDateTime'] = [line_of_flow_file[2]]
            items_of_meter['readingRegister'] = [line_of_flow_file[3]]
            if file_lines[line+1].split('|')[:-1][0] == '030':
                subMeterReading = True
                items_of_meter['meterRegisterId'].append(file_lines[line+1].split('|')[:-1][1])
                items_of_meter['readingDateTime'].append(file_lines[line+1].split('|')[:-1][2])
                items_of_meter['readingRegister'].append(file_lines[line+1].split('|')[:-1][3])
                items_of_meter['meterId'].append(items_of_meter.get('meterId')[0])
                meter_group[mpanCore] = items_of_meter
                items_of_meter = dict()
            else:
                meter_group[mpanCore] = items_of_meter
                items_of_meter = dict()
                
    return meter_group
                

def extract_data_items_from_flow_file(path):
    
    file_lines = read_requested_flow_file(path)
    meter_group = group_meter_items(file_lines)
    
    return meter_group
