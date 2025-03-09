# %%
import csv
from pathlib import Path

def vtt_to_csv(vtt_path: Path, output_dir: Path):
    """Convert VTT file to CSV with columns: Cue, Start, End, Text"""
    with open(vtt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    cues = []
    current_cue = {}
    
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
            
        if line.isdigit():
            current_cue["Cue"] = line
        elif '-->' in line:
            start, end = line.split(' --> ')
            current_cue["Start"] = start
            current_cue["End"] = end
        else:
            current_cue["Text"] = line
            cues.append(current_cue)
            current_cue = {}

    # Create output directory if needed
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create output path matching input filename
    output_path = output_dir / vtt_path.with_suffix('.csv').name
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Cue", "Start", "End", "Text"])
        writer.writeheader()
        writer.writerows(cues)
        
    print(f"Converted {vtt_path.name} to {output_path}")

# Input and output paths
input_vtt = Path("/mnt/c/Users/Som/Desktop/CHART ASIST/Study3_Analysis/processed_data/transcripts/HSRData_ZoomAudioTranscript_Trial-na_Team-TM000315_Member-na_CondBtwn-ASI-CMURI-TA1_CondWin-na_Vers-1.vtt")
output_dir = Path("/mnt/c/Users/Som/Desktop/CHART ASIST/Study3_Analysis/processed_data/csv_transcripts/")

# Execute conversion
vtt_to_csv(input_vtt, output_dir)


# %%



