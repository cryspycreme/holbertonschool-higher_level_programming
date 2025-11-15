import os

def generate_invitations(template, attendees):
    # check input types
    if not isinstance(template, str):
        print("Template must be a string")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Attendees must be a list of dictionaries")
        return
   
    # handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    index = 0
    required_fields = ["name", "event_title", "event_date", "event_location"]
    template_copy = template
    for attendee in attendees:
        template = template_copy
        for field in required_fields:
            value = attendee.get(field, None)
            if value is None:
                value = "N/A"
                template = template.replace('{' + field + '}', value)
            else:
                template= template.replace('{' + field + '}', value)

        # write to file
        index = index + 1
        path = "output_" + str(index) + ".txt"
        if os.path.exists(path):
            print(f"File {path} already exists")
        else:
            with open(path, "w") as file:
                file.write(template)
