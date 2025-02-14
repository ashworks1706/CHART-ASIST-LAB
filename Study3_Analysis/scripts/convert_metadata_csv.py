# import json
# import pandas as pd

# def json_to_csv(input_file, output_file):
#     entries = []
    
#     with open(input_file, 'r') as f:
#         for line in f:
#             try:
#                 data = json.loads(line)
                
#                 # Extract header information
#                 header = data.get('header', {})
                
#                 # Extract message information
#                 msg = data.get('msg', {})
                
#                 # Extract trial metadata
#                 trial_metadata = data.get('data', {}).get('metadata', {}).get('trial', {})
                
#                 # Create entry dictionary
#                 entry = {
#                     # Header data
#                     'header_timestamp': header.get('timestamp'),
#                     'header_message_type': header.get('message_type'),
#                     'header_version': header.get('version'),
                    
#                     # Message data
#                     'msg_sub_type': msg.get('sub_type'),
#                     'msg_source': msg.get('source'),
#                     'msg_experiment_id': msg.get('experiment_id'),
#                     'msg_trial_id': msg.get('trial_id'),
#                     'msg_timestamp': msg.get('timestamp'),
#                     'msg_version': msg.get('version'),
                    
#                     # Trial metadata
#                     'metadata_name': trial_metadata.get('name'),
#                     'metadata_date': trial_metadata.get('date'),
#                     'metadata_experimenter': trial_metadata.get('experimenter'),
#                     'metadata_subjects': ', '.join([s.strip() for s in trial_metadata.get('subjects', [])]),
#                     'metadata_trial_number': trial_metadata.get('trial_number'),
#                     'metadata_group_number': trial_metadata.get('group_number'),
#                     'metadata_study_number': trial_metadata.get('study_number'),
#                     'metadata_condition': trial_metadata.get('condition'),
#                     'metadata_notes': ', '.join(trial_metadata.get('notes', [])),
#                     'metadata_testbed_version': trial_metadata.get('testbed_version'),
#                     'metadata_experiment_name': trial_metadata.get('experiment_name'),
#                     'metadata_experiment_date': trial_metadata.get('experiment_date'),
#                     'metadata_experiment_author': trial_metadata.get('experiment_author'),
#                     'metadata_experiment_mission': trial_metadata.get('experiment_mission')
#                 }
                
#                 entries.append(entry)
                
#             except json.JSONDecodeError:
#                 print(f"Skipping invalid JSON line: {line.strip()}")
    
#     # Create DataFrame and save to CSV
#     df = pd.DataFrame(entries)
#     df.to_csv(output_file, index=False)
#     print(f"Successfully converted {len(entries)} entries to {output_file}")

# # Usage example:
# json_to_csv('/mnt/c/Users/Som/Desktop/CHART ASIST/Study3_Analysis/data/HSRData_TrialMessages_Trial-T000830_Team-TM000315_Member-na_CondBtwn-ASI-CMURI-TA1_CondWin-na_Vers-1.metadata', 'HSRData_TrialMessages_Trial-T000830_Team-TM000315_Member-na_CondBtwn-ASI-CMURI-TA1_CondWin-na_Vers-1.csv')

import json
import csv
from collections import defaultdict

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            items.append((new_key, ', '.join(map(str, v))))
        else:
            items.append((new_key, v))
    return dict(items)

def json_to_csv(input_file, output_file):
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            try:
                json_obj = json.loads(line.strip())
                flattened = flatten_dict(json_obj)
                data.append(flattened)
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line: {line.strip()}")

    if not data:
        print("No valid JSON objects found in the file.")
        return

    fieldnames = set()
    for entry in data:
        fieldnames.update(entry.keys())

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=sorted(fieldnames))
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

    print(f"Successfully converted {len(data)} entries to {output_file}")

# Usage
json_to_csv('/mnt/c/Users/Som/Desktop/CHART ASIST/Study3_Analysis/data/HSRData_TrialMessages_Trial-T000830_Team-TM000315_Member-na_CondBtwn-ASI-CMURI-TA1_CondWin-na_Vers-1.metadata', 'HSRData_TrialMessages_Trial-T000830_Team-TM000315_Member-na_CondBtwn-ASI-CMURI-TA1_CondWin-na_Vers-1.csv')
