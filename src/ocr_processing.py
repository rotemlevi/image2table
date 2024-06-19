import re
import pandas as pd

def extract_channel_from_line(line, channels):
    for channel in channels:
        if channel in line:
            return channel
    return None

def correct_ocr_errors(text):
    # Correct OCR errors like Q2-06-24 to 02-06-24
    corrected_text = re.sub(r'\bQ(\d{1}-\d{2}-\d{2})\b', r'0\1', text)
    return corrected_text

def process_text_to_df(extracted_text):
    channels = [
        "EDC/K SHOP",
        "Lotus's Lamai Ko Samui Branch",
        "Automatic Transfer",
        "EDC/E-Commerce",
        "K PLUS",
        "Deposit Account/ Payment/Fee",
        "Internet/Mobile BAY",
        "ATM Tesco Lotus Lamai",
        "Ko Samui Branch"
    ]
    
    lines = extracted_text.strip().split('\n')
    parsed_data = {
        "Date": [],
        "Time": [],
        "Description": [],
        "Withdrawal_Deposit": [],
        "Outstanding_Balance": [],
        "Channel": [],
        "Details": []
    }
    # Combine multi-line entries based on date patterns
    combined_lines = []
    temp_line = ""

    for line in lines:
        if re.match(r'^\d{2}-\d{2}-\d{2}', line):
            if temp_line:
                combined_lines.append(temp_line.strip())
            temp_line = line.strip()
        else:
            temp_line += " " + line.strip()

    if temp_line:
        combined_lines.append(temp_line.strip())
        
    for line in combined_lines:
        date = ""
        time = ""
        description = ""
        withdrawal_deposit = ""
        outstanding_balance = ""
        channel = ""
        details = ""

        date_match = re.match(r'^(\d{2}-\d{2}-\d{2})\s*[^\w]*\s*', line)
        if date_match:
            date_col = date_match.group(0)
            date = date_match.group(1).strip()
            remaining = line[len(date_col):].strip()
        else:
            continue
         
        time_match = re.match(r'(^\d{2}:\d{2})\s*[^\w]*\s*', remaining)
        if time_match:
            time_col = time_match.group(0)
            time = time_match.group(1).strip()
            remaining = remaining[len(time_col):].strip()
      
        description_match = re.match(r'([a-zA-Z\s]+)', remaining)
        if description_match:
            description_col = description_match.group(0)
            description = description_match.group(1).strip()
            remaining = remaining[len(description_col):].strip()
        
        withdrawal_deposit_match = re.match(r'^([\d,]+\.\d{2})\s*[^\w]*\s*', remaining)
        if withdrawal_deposit_match:
            withdrawal_deposit_col = withdrawal_deposit_match.group(0)
            withdrawal_deposit = withdrawal_deposit_match.group(1).strip()
            remaining = remaining[len(withdrawal_deposit_col):].strip()
        
        outstanding_balance_match = re.match(r'^([\d,]+\.\d{2})\s*[^\w]*\s*', remaining)
        if outstanding_balance_match:
            outstanding_balance_col = outstanding_balance_match.group(0)
            outstanding_balance = outstanding_balance_match.group(1).strip()
            remaining = remaining[len(outstanding_balance_col):].strip()
        
        channel = extract_channel_from_line(remaining, channels)
        if channel:
            remaining = remaining.replace(channel, '').strip()

        details = remaining
        
        parsed_data['Date'].append(date)
        parsed_data['Time'].append(time)
        parsed_data['Description'].append(description)
        parsed_data['Withdrawal_Deposit'].append(withdrawal_deposit)
        parsed_data['Outstanding_Balance'].append(outstanding_balance)
        parsed_data['Channel'].append(channel)
        parsed_data['Details'].append(details)

    df = pd.DataFrame(parsed_data)
    return df
